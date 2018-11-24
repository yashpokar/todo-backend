from setuptools import setup, find_packages

setup(
	name='todo',
	description='TODO app.',
	version='0.0.1-dev',
	install_requires=(
		'Flask',
		'Flask-SQLALchemy',
		'Flask-Migrate',
		'Flask-Script',
		'Flask-WTF',
		'psycopg2-binary',
		'flask-socketio',
		'flask-cors',
	),
)
