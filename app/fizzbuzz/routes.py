import json
from flask import render_template, flash, redirect, url_for
from app import app
from app.fizzbuzz.forms import ResultForm
from app.fizzbuzz import bp


@bp.route('/result/')
@bp.route('/result/<input_number>')
def result(input_number=None):
    numbers = []
    a = 3
    b = 5
    c = a * b

    for i in range(0, int(input_number) + 1):
        return_data = i
        if i == 0:
            pass
        elif i % c == 0:
            return_data = 'Fizz Buzz!'
        elif i % a == 0:
            return_data = 'Fizz'
        elif i % b == 0:
            return_data = 'Buzz'
        numbers.append(return_data)

    return render_template('fizzbuzz/result.html', title='Result', numbers=numbers, a=a, b=b, c=c)


@bp.route('/', methods=['POST', 'GET'])
def home():
    form = ResultForm()

    if form.validate_on_submit():
        flash('The Fizz Buzz results for numbers 0 and {}'.format(form.input_number.data))
        return redirect(url_for('fizzbuzz.result') + ('%d' % form.input_number.data))

    return render_template('fizzbuzz/home.html', title='Home', form=form)