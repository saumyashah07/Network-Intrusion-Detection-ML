from flask import Flask, render_template, request, jsonify
import pandas as pd

import joblib

app = Flask(__name__)

model = joblib.load("models/nids_pipeline.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    confidence = max(probabilities) * 100

    return jsonify({
        "prediction": prediction,
        "confidence": round(confidence, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)