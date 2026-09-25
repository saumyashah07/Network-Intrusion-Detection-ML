# AI-Based Network Intrusion Detection System

A machine learning-based Network Intrusion Detection System (NIDS) that analyzes network traffic and predicts whether it is normal or represents a known type of intrusion.

The project combines data preprocessing, multiple machine learning models, external evaluation, and a Flask web interface to provide an end-to-end intrusion detection workflow.

## Overview

Traditional network monitoring can become difficult when large amounts of traffic need to be analyzed. This project explores how machine learning can be used to identify patterns in network traffic and classify different types of attacks.

The system can:

* Classify network traffic into specific attack types
* Identify traffic as Normal or Attack
* Categorize attacks into groups such as DoS, Probe, R2L, and U2R
* Compare multiple machine learning algorithms
* Display prediction confidence through a web interface
* Evaluate the trained model on the KDDTest+ dataset

## Machine Learning Models

Three classification algorithms were explored:

| Model         | Purpose                         |
| ------------- | ------------------------------- |
| Random Forest | Primary classification model    |
| Decision Tree | Tree-based comparison model     |
| KNN           | Distance-based comparison model |

Random Forest was selected as the main model used by the web application.

## Dataset

The project uses the **NSL-KDD dataset**, including:

* `KDDTrain+.txt` — training data
* `KDDTest+.txt` — external test data

The dataset contains network-traffic features along with labels describing normal traffic and different intrusion types.

## Workflow

```text
Network Traffic Data
        ↓
Data Cleaning & Preparation
        ↓
Categorical Encoding + Feature Scaling
        ↓
Train / Test Split
        ↓
Machine Learning Models
        ↓
Model Evaluation
        ↓
Random Forest Pipeline
        ↓
Flask Web Application
        ↓
Prediction + Attack Category + Confidence
```

## Evaluation Results

The Random Forest model was evaluated using both the internal test split and the external KDDTest+ dataset.

| Evaluation          | Accuracy |
| ------------------- | -------: |
| Training/Test Split |   99.84% |
| KDDTest+ Multiclass |   72.24% |
| KDDTest+ Binary     |   75.59% |

The external KDDTest+ results show that performance differs from the internal test split, which is useful for understanding how the model behaves on unseen data.

## Web Application

The Flask-based interface allows users to enter network-traffic values and receive a prediction.

The application displays:

* Normal Traffic or Attack Detected
* Predicted attack type
* Attack category
* Model confidence

Example:

```text
Normal Traffic
Confidence: 100%
```

or

```text
Attack Detected
Attack Type: ipsweep
Category: Probe
Confidence: XX%
```

## Project Structure

```text
Network-Intrusion-Detection-ML/
│
├── dataset/
│   ├── KDDTrain+.txt
│   └── KDDTest+.txt
│
├── models/
│   ├── nids_pipeline.pkl
│   ├── random_forest_model.pkl
│   ├── preprocessor.pkl
│   ├── model_comparison.csv
│   ├── external_test_results.csv
│   ├── binary_classification_results.csv
│   ├── evaluation_summary.csv
│   └── final_results.csv
│
├── notebooks/
│   └── intrusion_detection.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Flask
* Joblib
* Jupyter Notebook
* HTML
* CSS
* JavaScript
* Git & GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/saumyashah07/Network-Intrusion-Detection-ML.git
cd Network-Intrusion-Detection-ML
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Run the Web Application

Start the Flask application:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Project Goals

This project was developed to understand the complete machine learning workflow for intrusion detection, from dataset preparation and model training to evaluation and deployment through a web interface.

## Limitations

The current system is a learning and demonstration project. Its external test performance indicates that further work is needed before considering it suitable for production network-security monitoring.

The current web form also uses a simplified set of user-editable traffic fields while the remaining model features are supplied with predefined values.

## Future Improvements

* Improve performance on unseen attack types
* Add more flexible input features
* Add real-time network traffic monitoring
* Add interactive dashboards and visual analytics
* Explore additional machine learning and deep learning models
* Improve attack-category mapping
* Deploy the application as an online service

## Disclaimer

This project is intended for educational and demonstration purposes. Predictions should not be treated as a substitute for professional network security analysis.
