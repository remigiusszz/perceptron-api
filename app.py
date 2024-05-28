# app.py
from flask import Flask, request, jsonify
import numpy as np
from model import Perceptron

app = Flask(__name__)

# Inicjalizacja modelu perceptronu
model = Perceptron(input_size=2)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    x = np.array(data['input'])
    prediction = model.predict(x)
    return jsonify({'prediction': prediction})

@app.route('/train', methods=['POST'])
def train():
    data = request.get_json()
    X = np.array(data['inputs'])
    y = np.array(data['outputs'])
    model.train(X, y)
    return jsonify({'status': 'Model trained successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
