from flask import Flask
from flask import request, render_template, jsonify
import os
import pandas as pd


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', inputDate='20150809', inputID=790)


def validate_date(inputDate):
    files = [f for f in os.listdir('static/data') if os.path.isfile(f) and f.endswith('.txt')]

    for f in files:
        title = os.path.splitext(os.path.basename(f))[0]
        if inputDate == title:
            return true
    return false


def already_processed(inputDate):
    files = [f for f in os.listdir('static/data') if os.path.isfile(f) and f.endswith('.csv')]

    for f in files:
        title = os.path.splitext(os.path.basename(f))[0]
        if inputDate == title:
            return true
    return false


def process_data(inputDate):
    """
    Read in the inputDate, match it to the txt file
    Create a 3-column dataframe
        | source | target | value |
    Save the dataframe as a csv file
    """
    f = '/static/data/' + inputDate + '.txt'
    df = pd.DataFrame(columns=['source', 'target', 'value'])
    i = 0
    file = open(f,'r')
    for line in file:
        data = line.split(',')
        target = data[0]
        data.pop(0)
        for j in range(0, int(len(data)/2)):
            df.loc[i] = [data[2*j], target, float(data[2*j+1])]
            i += 1
    df.to_csv(inputDate+'.csv', index=False)



@app.route('/submit', method=['POST'])
def submit():
    try:
        inputDate = request.form['field1']
        inputID = request.form['field2']
    except:
        errors.append('Unable to get the inputs. Please make sure they are valid and try again!')
        return redirect(url_for('index'))
    
    if validate_date(inputDate)==False:
        flash('The data for that input date is not available!')
        return redirect(url_for('index'))
    elif already_processed(inputDate)==False:
        process_data(inputDate)
    else:
        pass


    return render_template('index.html',inputDate=inputDate, inputID=inputID)


if __name__ == '__main__':
    app.debug = False
    app.run()
