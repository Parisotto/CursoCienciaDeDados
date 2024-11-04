from flask import render_template
from siteflask import app

@app.route("/")
def home():
    return render_template('home.html', usuario='Parisotto')

@app.route("/lista")
def lista():
    lista = ['janeiro', 'fevereiro', 'março']
    return render_template('lista.html', lista=lista)
