# Author: Jason Lu
from flask import Flask, render_template, make_response
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    return resp;


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)