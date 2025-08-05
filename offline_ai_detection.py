import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

MODEL_PATH = 'models/isolation_forest_model.pkl'

def train_model(train_file):
    df = pd.read_csv(train_file)
    # Example: Assuming logs have numeric features to detect anomalies
    features = df.select_dtypes(include=['float64', 'int64'])
    model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
    model.fit(features)
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model trained and saved at {MODEL_PATH}")

def detect_anomalies(test_file):
    if not os.path.exists(MODEL_PATH):
        print("Model not found! Train the model first.")
        return
    df = pd.read_csv(test_file)
    features = df.select_dtypes(include=['float64', 'int64'])
    model = joblib.load(MODEL_PATH)
    preds = model.predict(features)
    df['anomaly'] = preds
    # -1 is anomaly, 1 is normal
    anomalies = df[df['anomaly'] == -1]
    print(f"Detected {len(anomalies)} anomalies:")
    print(anomalies)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: python offline_ai_detection.py train <train_csv> | detect <test_csv>")
        exit(1)
    mode = sys.argv[1]
    file = sys.argv[2]
    if mode == 'train':
        train_model(file)
    elif mode == 'detect':
        detect_anomalies(file)
    else:
        print("Invalid mode! Use 'train' or 'detect'.")
