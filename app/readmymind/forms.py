from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField
from wtforms.validators import NumberRange

ANSWER_CHOICES = [('NO', 'NO'), ('YES', 'YES')]

class QuestionForm(FlaskForm):
    number = IntegerField('Apakah X adalah ', render_kw={'readonly': True})
    answer = SelectField('Answer', choices=ANSWER_CHOICES)
    submit = SubmitField('View Results')