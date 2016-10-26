import pandas as pd
import os

def process_data(f):
    """
    Read in the raw csv file and return a 3-column dataframe
        | source | target | value |
    the dataframe will be used for drawing the sankey chart
    """
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

    return(df)

files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt')]
print(files)
for f in files:
    formatted = process_data(f)
    title = os.path.splitext(os.path.basename(f))[0]
    formatted.to_csv(title+'.csv', index=False)

