from config import LocalConfig
from todo import create_app, socketio
from flask_migrate import MigrateCommand
from flask_script import Manager

app = create_app(LocalConfig)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def runserver():
	return socketio.run(app)

if __name__ == '__main__':
	manager.run()
