from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    hewwo_message = 'dnd amirite fellas'
    return render_template('index.html', message = hewwo_message)