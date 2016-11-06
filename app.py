from flask import Flask
from flask import request, render_template, jsonify
import os
import pandas as pd


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.debug = True
    app.run()
