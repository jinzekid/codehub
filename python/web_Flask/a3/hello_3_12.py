# Author: Jason Lu
from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime
app = Flask(__name__)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index_3_12.html', current_time=datetime.utcnow())

@app.route('/base_ico')
def base_icon():
    return render_template('base3_10.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)