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

    attack_category_map = {
        "normal": "Normal",
        "back": "DoS",
        "land": "DoS",
        "neptune": "DoS",
        "pod": "DoS",
        "smurf": "DoS",
        "teardrop": "DoS",
        "ipsweep": "Probe",
        "nmap": "Probe",
        "portsweep": "Probe",
        "satan": "Probe",
        "ftp_write": "R2L",
        "guess_passwd": "R2L",
        "imap": "R2L",
        "multihop": "R2L",
        "phf": "R2L",
        "spy": "R2L",
        "warezclient": "R2L",
        "warezmaster": "R2L",
        "buffer_overflow": "U2R",
        "loadmodule": "U2R",
        "perl": "U2R",
        "rootkit": "U2R"
    }

    category = attack_category_map.get(prediction, "Other")

    probabilities = model.predict_proba(input_data)[0]
    confidence = max(probabilities) * 100

    return jsonify({
        "prediction": prediction,
        "category": category,
        "confidence": round(confidence, 2)
    })
if __name__ == "__main__":
    app.run(debug=True)