from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# ========== Load Models & Scalers ==========
models = {}
scalers = {}
for name in ['flood', 'cyclone', 'heatwave']:
    models[name] = pickle.load(open(f"models/{name}_model.pkl", "rb"))
    scalers[name] = pickle.load(open(f"models/{name}_scaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    disaster_type = request.form['disaster_type']
    features = [float(x) for x in request.form['features'].split(',')]
    features = np.array(features).reshape(1, -1)
    features_scaled = scalers[disaster_type].transform(features)
    prediction = models[disaster_type].predict(features_scaled)[0]
    return render_template('index.html', prediction_text=f"{disaster_type.capitalize()} Risk: {prediction}")

if __name__ == "__main__":
    app.run(debug=True)
