class Config:
	DEBUG = False
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = b'gQsm%Fy%TCJv/*7A*K.pU)AFHW>r6QT>;Xh(P0yL7VB-KC0yc(2E](J,H_Xc?G]'
	WTF_CSRF_ENABLED = False


class LocalConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'postgres://postgres:yourpassword@127.0.0.1:5432/todo'


class ProductionConfig(Config):
	pass
