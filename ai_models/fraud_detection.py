import sqlite3
import numpy as np
from sklearn.ensemble import IsolationForest

def detect_fraud(amount):
    try:
        conn = sqlite3.connect('transactions.db')
        c = conn.cursor()
        c.execute("SELECT amount FROM transactions")
        data = c.fetchall()
        conn.close()

        if len(data) < 5:
            return 0  # not enough data to detect fraud

        X = np.array(data).reshape(-1, 1)

        model = IsolationForest(contamination=0.1, random_state=42)
        model.fit(X)

        prediction = model.predict([[float(amount)]])[0]
        return int(prediction == -1)
    except Exception as e:
        print("Fraud detection error:", e)
        return 0
