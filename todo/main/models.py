from todo import db
from ..utils import get_dict


class RecordNotFoundError(Exception):
	pass


class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False, unique=True)

	@staticmethod
	def get_tasks(name):
		user = User.query.filter_by(name=name).first()

		if not user:
			raise RecordNotFoundError('User not found.')

		return [get_dict(task) for task in user.tasks]


class Task(db.Model):
	__tablename__ = 'tasks'

	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.Text, nullable=False)
	completed_on = db.Column(db.DateTime)
	created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	creator = db.relationship('User', backref='tasks')
