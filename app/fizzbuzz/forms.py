from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import NumberRange

class ResultForm(FlaskForm):
	input_number = IntegerField('Input Number : ')
	submit = SubmitField('View Results')