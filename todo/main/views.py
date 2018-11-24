from flask import Blueprint, jsonify
from .models import User, Task, RecordNotFoundError
from todo import socketio, db
from .forms import RegistrationForm
from todo.utils import get_json, get_dict
from flask_socketio import emit

main = Blueprint('main', __name__)

@main.route('/')
def home():
	return 'Hello World!'

@main.route('/register', methods=['POST'])
def register():
	form = RegistrationForm(get_json())

	if not form.validate():
		return jsonify(errors=form.errors, message='Validation fail.', success=False), 403

	try:
		user = User.query.filter_by(name=form.name.data).first()

		if user:
			return jsonify(message='Your account already exists.', success=True, data=dict(name=user.name, id=user.id))

		user = User(name=form.name.data)

		db.session.add(user)
		db.session.commit()
	except:
		return jsonify(success=False, message='Internal server error.'), 500

	return jsonify(message='Your account has been created.', data=dict(name=form.name.data, id=user.id), success=True)

@main.route('/tasks/<name>')
def tasks(name):
	try:
		tasks = User.get_tasks(name=name)
	except RecordNotFoundError as e:
		return jsonify(message=str(e), success=False), 301
	except Exception:
		return jsonify(message='Internal server Error.', success=False), 500

	return jsonify(success=True, data=dict(tasks=tasks))

@socketio.on('addNewTask')
def add_new_task(response):
	description = response['description']
	name = response['name']

	try:
		creator = User.query.filter_by(name=name).first()

		if not creator:
			emit('error', 'User not found.')

		task = Task(description=description, creator=creator)

		db.session.add(task)
		db.session.commit()
	except:
		emit('error', 'Couldn\'t add new task.', broadcast=True)

	task = get_dict(task)
	task['name'] = name

	emit('newTaskadded', task, broadcast=True)
