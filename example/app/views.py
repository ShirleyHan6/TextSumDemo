# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import render_template, jsonify
from gensim.summarization import keywords

from app import app
from .forms import MainForm
from .process import summary_highlight


@app.route('/', methods=['GET'])
def index():
    form = MainForm()
    return render_template('index2.html', form=form)


@app.route('/check', methods=['POST'])
def check():
    print("The form is called.")
    form = MainForm()
    if form.validate_on_submit():
        print("The form is validated.")
        text = form.data['text']
        title = "title"
        keyword = keywords(text, words=form.data['keywords_no'])
        summary = summary_highlight(text, form.data['coref'], 
            form.data['percentage']/100)
        print(form.data['percentage']/100)
        return jsonify(data={'summary': '{}'.format(summary), 'title': '{}'.format(title),
                             'keywords': '{}'.format(keyword)})
    return jsonify(data=form.errors)
