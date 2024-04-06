from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('model.pkl', "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict_price():
    # Retrieve form data
    carat = float(request.form.get('carat'))
    cut = request.form.get('cut')
    color = request.form.get('color')
    clarity = request.form.get('clarity')
    depth = float(request.form.get('depth'))
    table = float(request.form.get('table'))
    x = float(request.form.get('x'))
    y = float(request.form.get('y'))
    z = float(request.form.get('z'))

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'carat': [carat],
        'cut': [cut],
        'color': [color],
        'clarity': [clarity],
        'depth': [depth],
        'table': [table],
        'x': [x],
        'y': [y],
        'z': [z]
    })

    # Make predictions
    prediction = model.predict(input_data)

    # Return the predicted value
    return render_template("index.html", prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
