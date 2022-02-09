import json
from flask import render_template, flash, redirect, url_for, request
from app import app
from app.readmymind.forms import QuestionForm
from app.readmymind import bp
from app.constants.readmymind_enum import QuestionEnum
from config import Config


@bp.route('/read-my-mind', methods=['POST'])
def create():
    form = QuestionForm()
    data = app.db.fetch_read_my_mind()
    numbers = app.db.fetch_numbers()
    if form.number.data >= 0:
        if len(numbers) > 3:
            if form.answer.data == 'NO':
                if len(data) % 2 == 0:
                    app.db.delete_number(form.number.data, greater_than=True)
                else:
                    app.db.delete_number(form.number.data, greater_than=False)

            else:
                if len(data) % 2 == 0:
                    app.db.delete_number(form.number.data, greater_than=False)
                else:
                    app.db.delete_number(form.number.data, greater_than=True)

            app.db.create_read_my_mind(form.number.data, form.answer.data)

        else:
            app.db.delete_number(form.number.data, equal=True)
            if form.answer.data == 'YES':
                flash('Your Number is {0}'.format(form.number.data))
                app.db.delete_read_my_mind()
                app.db.delete_number_all()
                app.db.create_numbers()

    else:
        flash('Over Probabilities!')
        app.db.delete_read_my_mind()
        app.db.create_numbers()

    return redirect(url_for('readmymind.home'))


@bp.route('/read-my-mind', methods=['GET'])
def home():
    form = QuestionForm()
    data = app.db.fetch_read_my_mind()
    numbers = app.db.fetch_numbers()

    form.number.data = app.utils.generate_random_number(numbers)
    if len(numbers) <= 3:
        form.number.label.text = QuestionEnum.EQUAL.value.format(form.number.data)
    else:
        if len(data) % 2 == 0:
            form.number.label.text = QuestionEnum.GREATER_THAN.value.format(form.number.data)
        else:
            form.number.label.text = QuestionEnum.LESS_THAN.value.format(form.number.data)

    return render_template('readmymind/readmymind.html',
                           title='Read My Mind',
                           form=form,
                           data=data,
                           count_data=len(data),
                           max_number=int(Config.MAX_NUMBER)
                           )