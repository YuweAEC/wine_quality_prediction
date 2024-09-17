import pickle
from flask import Flask
from flask import request
from flask import render_template
import joblib

app = Flask(__name__)

# Load the prediction model
model = joblib.load("model_predict")

@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/result', methods=['GET', 'POST'])
def get_value():
    if request.method == "POST":
        try:
            # Get form values and convert them to float
            fixed_acidity = float(request.form.get('fixed_acidity'))
            volatile_acidity = float(request.form.get('volatile_acidity'))
            citric_acid = float(request.form.get('citric_acid'))
            residual_sugar = float(request.form.get('residual_sugar'))
            density = float(request.form.get('density'))
            pH = float(request.form.get('pH'))
            alcohol = float(request.form.get('alcohol'))

            # Make prediction
            predict_value = model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, density, pH, alcohol]])

            # Render the results page with the prediction
            return render_template('results.html', prediction=predict_value[0])
        except Exception as e:
            # Handle exceptions like missing input or conversion error
            return render_template('error.html', error=str(e))

    # Default return for GET requests (not likely to be used in this route)
    return render_template('index.html')

if __name__ == "__main__":
    app.run()