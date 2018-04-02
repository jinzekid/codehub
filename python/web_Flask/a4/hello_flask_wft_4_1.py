# Author: Jason Lu
from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/')
def index():
    return render_template('index_flask_wft_4_1.html', name="jason")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7777, debug=True)



