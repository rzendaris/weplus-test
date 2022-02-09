import json
from flask import render_template, flash, redirect, url_for, request
from app import app
from app.readmymind.forms import QuestionForm
from app.utils.utils import CustomUtils
from app.connection.db import Database
from app.readmymind import bp
from config import Config


@bp.route('/read-my-mind', methods=['POST', 'GET'])
def home():
    form = QuestionForm()
    db = Database()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.number.data >= 0:
                if form.answer.data == 'NO':
                    db.create_read_my_mind(form.number.data, form.answer.data)
                else:
                    flash('Your Number Is {}'.format(form.number.data))
                    db.delete_read_my_mind()
            else:
                flash('Over Probabilities!')

            return redirect(url_for('readmymind.home'))

    data = db.fetch_read_my_mind()
    form.number.data = CustomUtils.generate_random_number(data)
    return render_template('readmymind/readmymind.html',
                           title='Read My Mind',
                           form=form,
                           data=data,
                           count_data=len(data),
                           max_number=int(Config.MAX_NUMBER)
                           )