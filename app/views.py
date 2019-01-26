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
    return render_template('index.html', form=form)


@app.route('/check', methods=['POST'])
def check():
    form = MainForm()
    if form.validate_on_submit():
        text = form.data['text']
        title = "title"
        keyword = keywords(text, words=form.data['keywords_no'], lemmatize=True)
        summary = summary_highlight(text, form.data['coref'], 
            form.data['percentage']/100)
        return jsonify(data={'summary': '{}'.format(summary), 'title': '{}'.format(title),
                             'keywords': '{}'.format(keyword)})
    return jsonify(data=form.errors)
