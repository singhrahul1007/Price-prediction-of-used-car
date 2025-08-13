from flask import Flask, jsonify, render_template, request
import pandas as pd
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load the main cleaned data
cars = pd.read_csv('Data/cleaned_car_data.csv')

# Load the full trained pipeline
def load_pipeline():
    # E:\Machine-Learning-Projects\Used-Cars-Price-Prediction\Model\LinearRegressionModel2.pkl
    path = os.path.join('Model', 'LinearRegressionModel2.pkl')
    with open(path, 'rb') as f:
        return pickle.load(f)

pipe = load_pipeline()

# Prediction logic
def predict_price(name, company, year, kms_driven, fuel_type):
    input_df = pd.DataFrame(
        [[name, company, year, kms_driven, fuel_type]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    )
    prediction = pipe.predict(input_df)[0]
    return np.round(prediction, 2)

# Web routes
@app.route('/', methods=['GET', 'POST'])
def index():
    # Dropdown options
    name_list = sorted(cars['name'].unique())
    company_list = sorted(cars['company'].unique())
    fuel_list = sorted(cars['fuel_type'].unique())
    years = sorted(cars['year'].unique(), reverse=True)

    predicted_price = None

    if request.method == 'POST':
        company = request.form.get('company')
        car_name = request.form.get('car_model')
        car_year = int(request.form.get('year'))
        fuel = request.form.get('fuel_type')
        kms_driven = int(request.form.get('kms_driven'))

        predicted_price = predict_price(car_name, company, car_year, kms_driven, fuel)

    return render_template(
        'index.html',
        company_name=company_list,
        car_name=name_list,
        year=years,
        fuel_type=fuel_list,
        predicted_price=predicted_price
    )

@app.route('/get_models', methods=['POST'])
def get_models():
    company = request.json['company']
    model_names = sorted([name for name in cars['name'].unique() if name.startswith(company)])
    return jsonify(model_names)

if __name__ == '__main__':
    app.run(debug=True)
