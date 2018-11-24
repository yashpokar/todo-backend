from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
socketio = SocketIO()
migrate = Migrate(db=db)
cors = CORS()

def create_app(config):
	app = Flask(__name__)
	app.config.from_object(config)

	db.init_app(app)
	migrate.init_app(app)
	# TODO :: change this from * to server in production
		# also use it from config not hardcoding here
	cors.init_app(app, resources={r'*': {'origins': '*'}})
	socketio.init_app(app)

	from .main.views import main

	app.register_blueprint(main)

	return app
