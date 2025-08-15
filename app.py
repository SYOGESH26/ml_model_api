from flask import Flask, request, jsonify
import torch
import os
import numpy as np

app = Flask(__name__)

# Load the trained model
model = torch.load("model/model.pt")
model.eval()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    # Input should be list of last n days temperatures
    inputs = torch.tensor(data["inputs"], dtype=torch.float32).reshape(-1, 1)
    
    with torch.no_grad():
        predictions = model(inputs)
    
    return jsonify({"predictions": predictions.numpy().flatten().tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

