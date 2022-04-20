from flask import Flask, render_template, request
import numpy as np
# import only the function from the ml_model.py
from ml_model import model_prediction
import os

app = Flask(__name__)
port = int(os.environ.get('PORT', 8000))


@app.route('/', methods=['POST', 'GET'])
def ml_model_function():
    '''This function receives 4 parameters from the front end
    makes a prediction based on them, and sends the result back to the frontend.'''

    if request.method == 'POST':

        # save the inputs from the front end
        Weight = float(request.form['Weight'])
        Length1 = float(request.form['Length1'])
        Length2 = float(request.form['Length2'])
        Length3 = float(request.form['Length3'])
        Height = float(request.form['Height'])
        Width = float(request.form['Width'])

        # call the ml function to make a prediction
        prediction = model_prediction(Weight, Length1, Length2,Length3,Height, Width)

        # send the prediction back to the front end
        return render_template('index.html', output=prediction)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
    #app.run(host='0.0.0.0', port=8000)
    #app.run(debug=True, host='0.0.0.0')
