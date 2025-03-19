from sklearn.ensemble import IsolationForest

# Placeholder Fraud Detection Model
def detect_fraud(amount):
    # Train a simple Isolation Forest model (in real-world, use historical data)
    X = [[100], [200], [300], [1000], [5000]]  # Example transaction amounts
    y = [0, 0, 0, 1, 1]  # 1 = Fraud, 0 = Legitimate
    model = IsolationForest(contamination=0.1)
    model.fit(X)

    # Predict Fraud
    fraud_flag = model.predict([[amount]])[0]
    return int(fraud_flag == -1)  # -1 = Fraud, 1 = Legitimate
