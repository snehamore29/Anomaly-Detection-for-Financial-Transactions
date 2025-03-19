import sqlite3
import numpy as np
from sklearn.ensemble import IsolationForest

def detect_fraud(amount):
    # Fetch transaction data from the database
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute("SELECT amount FROM transactions")
    data = c.fetchall()
    conn.close()

    # If there's not enough data, assume no fraud
    if len(data) < 5:
        return 0

    # Train the model on transaction data
    X = np.array(data).reshape(-1, 1)
    model = IsolationForest(contamination=0.1)
    model.fit(X)

    # Predict fraud
    fraud_flag = model.predict([[amount]])[0]
    return int(fraud_flag == -1)  # -1 = Fraud, 1 = Legitimate
