from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load('../model/trained_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = pd.DataFrame(data, index=[0])
    
    prediction = model.predict(input_data)
    return jsonify({'quality': int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)
