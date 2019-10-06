from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')

def index():
    name = 'stackoverflow'
    return render_template('View.html', name = name)