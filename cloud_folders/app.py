from flask import Flask, render_template, request
import numpy as np
import pickle
import boto3
import json
from datetime import datetime

app = Flask(__name__)

# LOAD TRAINED MODEL
with open("fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

print("✅ Model loaded successfully")

# S3 CONFIGURATION
s3 = boto3.client("s3")
BUCKET_NAME = "insurance-fraud-predictions"  

# FLASK ROUTES
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    claim_amount = int(request.form["claim_amount"])
    policy_age = int(request.form["policy_age"])
    claim_type = request.form["claim_type"]
    previous_claims = int(request.form["previous_claims"])
    customer_age = int(request.form["customer_age"])
    vehicle_age = int(request.form["vehicle_age"])
    claim_delay = int(request.form["claim_delay"])

    # Encode claim type
    claim_type_encoded = {
        "Accident": 0,
        "Theft": 1,
        "Fire": 2
    }[claim_type]

    # Encode accident severity
    if claim_type == "Accident":
        accident_severity_encoded = {
            "Low": 0,
            "Medium": 1,
            "High": 2
        }[request.form["accident_severity"]]
    else:
        accident_severity_encoded = -1

    input_data = np.array([[  
        claim_amount,
        policy_age,
        claim_type_encoded,
        accident_severity_encoded,
        previous_claims,
        customer_age,
        vehicle_age,
        claim_delay
    ]])

    # Predict probability
    fraud_prob = model.predict_proba(input_data)[0][1]
    probability = round(fraud_prob * 100, 2)

    # Classification logic
    if fraud_prob > 0.6:
        result = "❌ Fraudulent Claim"
    elif fraud_prob >= 0.35:
        result = "⚠️ Suspicious Claim"
    else:
        result = "✅ Genuine Claim"

    # STORE RESULT IN S3
    prediction_data = {
        "timestamp": str(datetime.now()),
        "claim_amount": claim_amount,
        "policy_age": policy_age,
        "claim_type": claim_type,
        "previous_claims": previous_claims,
        "customer_age": customer_age,
        "vehicle_age": vehicle_age,
        "claim_delay": claim_delay,
        "prediction": result,
        "fraud_probability_percent": probability
    }

    file_name = f"prediction_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    try:
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=json.dumps(prediction_data),
            ContentType="application/json"
        )
        print("✅ Prediction saved to S3:", file_name)
    except Exception as e:
        print("❌ Error uploading to S3:", str(e))

    # Return result to frontend
    return render_template(
        "index.html",
        prediction=result,
        probability=probability
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)