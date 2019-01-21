from flask import render_template, jsonify
from gensim.summarization import keywords

from app import app
from .forms import MainForm
from .process import summary_highlight


@app.route('/', methods=['GET'])
def index():
    form = MainForm()
    return render_template('home.html', form=form)


@app.route('/check', methods=['POST'])
def check():
    print("The form is called.")
    form = MainForm()
    if form.validate_on_submit():
        print("The form is validated.")
        title = "title"
        keyword = keywords(form.text.data, words=form.keywords_no.data)
        print("keyword", keyword)
        summary = summary_highlight(form.text.data, coref=form.coref.data, ratio=form.percentage.data/100,
                                    )
        return jsonify(data={'summary': '{}'.format(summary), 'title': '{}'.format(title),
                             'keywords': '{}'.format(keyword)})
    return jsonify(data=form.errors)
