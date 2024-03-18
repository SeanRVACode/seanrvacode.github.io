from flask import Flask,render_template

app = Flask(__name__)

@app.route('/index')
def home(name=None):
    return render_template('index.html',name=name)

@app.route('/about')
def about(name=None):
    return render_template('about.html',name=name)

