import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load Excel dataset
df = pd.read_csv("insurance.csv")

# Encode categorical variables
df["claim_type"] = df["claim_type"].map({
    "Accident": 0,
    "Theft": 1,
    "Fire": 2
})

df["accident_severity"] = df["accident_severity"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})

X = df.drop("is_fraud", axis=1)
y = df["is_fraud"]

# Stratified split ensures fraud is present in test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# Random Forest with class balancing
model = RandomForestClassifier(
    n_estimators=150,
    max_depth=10,
    min_samples_split=5,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("✅ Model Accuracy:", round(accuracy * 100, 2), "%")
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred))

# Save model
with open("fraud_model.pkl", "wb") as f:
    pickle.dump(model, f)