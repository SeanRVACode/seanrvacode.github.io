from flask import Flask,render_template,redirect

app = Flask(__name__)

@app.route('/index')
def home(name=None):
    return render_template('index.html',name=name)

@app.route('/about')
def about(name=None):
    return render_template('about.html',name=name)

@app.route("/images/<img>")
def images(img):
    return redirect(f'/static/images/{img}')

@app.route('/assets/css/<file>')
def css(file):
    return redirect(f'/static/assets/css/{file}')
@app.route('/assets/js/<file>')
def js(file):
    return redirect(f'/static/assets/js/{file}')
# @app.route('/favicon.ico')
# def favicon():
#     return redirect('/static/favicon.ico')