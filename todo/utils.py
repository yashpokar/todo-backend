from flask import request
from werkzeug.datastructures import ImmutableMultiDict

def get_json():
	try:
		return ImmutableMultiDict(request.json)
	except:
		# Json decode fail.
		pass

def get_dict(record):
	return { column.name: getattr(record, column.name) for column in record.__table__.columns }
