""" Forms
	------------------------------------------
	It doesn't really required in this case
	because its not that huge project but
	assume that additinal things will come in.
"""

from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf import FlaskForm
from .models import User


class RegistrationForm(FlaskForm):
	name = StringField(validators=[DataRequired(message='Name is required.')])
