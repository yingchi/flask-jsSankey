import os
from flask import Flask
from flask import request, render_template, jsonify


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    datafiles = []
    for root, dirs, files in os.walk('./static/data'):
        for filename in [os.path.join(root, name) for name in files]:
            if not filename.endswith('.txt'):
                continue
            datafiles.append(os.path.basename(filename))

    return render_template('index.html', **{
        'datafiles': datafiles
    })



if __name__ == '__main__':
    app.debug = False
    app.run()
