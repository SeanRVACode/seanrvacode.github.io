from datetime import date
from flask import Flask, abort, render_template, redirect,url_for,flash,jsonify
from flask_bootstrap import Bootstrap5
import random

app = Flask(__name__)
Bootstrap5(app)

@app.route('/')
def home():
    thumb_path = '.static/assets/img/portfolio/thumbnails/'
    full_path = '.static/assets/img/portfolio/fullsize/'
    return render_template('index.html',thumb_path=thumb_path,full_path=full_path)

# Handles the redirect for thumbnail images so I don't have to type url_for a ton
@app.route('assets/img/portfolio/thumbnails/<img>')
def thumbnails(img):
    return redirect(f'/static/assets/portfolio/thumbnails/{img}')

@app.route('assets/img/portfolio/fullsize/<img>')
def fullsize(img):
    return redirect(f'/static/assets/portfolio/fullsize/img')

@app.route('/returnChecker')
def taxReturnChecker():

    return render_template('taxReturnChecker.html',status="In Progress")
@app.route('/getStatus')
def getStatus():
    status_messages = ['How fast do these people expect us to get this done? We are working on it!','In the Dumpster on Fire','Sent to the wrong Client','Still waiting for you to sign that Engagement Letter.']
    status = random.choice(status_messages)
    return jsonify(status=status)