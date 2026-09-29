from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("models/nids_pipeline.pkl")

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


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No input data received."
        }), 400

    input_data = pd.DataFrame([data])

    try:

        prediction = model.predict(input_data)[0]
        prediction = str(prediction).lower()

        category = attack_category_map.get(
            prediction,
            "Other"
        )

        probabilities = model.predict_proba(
            input_data
        )[0]

        confidence = max(probabilities) * 100

        return jsonify({
            "prediction": prediction,
            "category": category,
            "confidence": round(confidence, 2)
        })

    except Exception as error:

        return jsonify({
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)