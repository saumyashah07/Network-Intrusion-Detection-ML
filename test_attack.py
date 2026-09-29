import pandas as pd
import joblib

model = joblib.load("models/nids_pipeline.pkl")

columns = [
    "duration",
    "protocol_type",
    "service",
    "flag",
    "src_bytes",
    "dst_bytes",
    "land",
    "wrong_fragment",
    "urgent",
    "hot",
    "num_failed_logins",
    "logged_in",
    "num_compromised",
    "root_shell",
    "su_attempted",
    "num_root",
    "num_file_creations",
    "num_shells",
    "num_access_files",
    "num_outbound_cmds",
    "is_host_login",
    "is_guest_login",
    "count",
    "srv_count",
    "serror_rate",
    "srv_serror_rate",
    "rerror_rate",
    "srv_rerror_rate",
    "same_srv_rate",
    "diff_srv_rate",
    "srv_diff_host_rate",
    "dst_host_count",
    "dst_host_srv_count",
    "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate",
    "dst_host_srv_serror_rate",
    "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate"
]

values = [[
    0, "tcp", "private", "S0", 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 123, 6, 1.0, 1.0, 0.0, 0.0, 0.05, 0.07,
    0.0, 255, 26, 0.1, 0.05, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0
]]

input_data = pd.DataFrame(values, columns=columns)

prediction = model.predict(input_data)[0]
probabilities = model.predict_proba(input_data)[0]
confidence = max(probabilities) * 100

print("\nMODEL TEST RESULT")
print("-----------------")
print("Prediction:", prediction)
print("Confidence:", round(confidence, 2), "%")