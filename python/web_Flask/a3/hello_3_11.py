# Author: Jason Lu
from flask import Flask
from flask.ext.moment import Moment
app = Flask(__name__)
moment = Moment(app)