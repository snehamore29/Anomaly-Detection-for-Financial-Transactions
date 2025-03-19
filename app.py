from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import numpy as np
from ai_models.age_gender_detection import detect_age_gender
from ai_models.fraud_detection import detect_fraud

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# SQLite Database Setup
def init_db():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (id INTEGER PRIMARY KEY, amount REAL, recipient TEXT, fraud_flag INTEGER)''')
    conn.commit()
    conn.close()

init_db()

# Endpoint for Transaction Processing
@app.route('/transaction', methods=['POST'])
def process_transaction():
    data = request.json
    amount = data['amount']
    recipient = data['recipient']

    # Fraud Detection
    fraud_flag = detect_fraud(amount)
    if fraud_flag:
        return jsonify({"status": "Fraud Detected", "fraud_flag": 1})

    # Save Transaction to Database
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute("INSERT INTO transactions (amount, recipient, fraud_flag) VALUES (?, ?, ?)",
              (amount, recipient, fraud_flag))
    conn.commit()
    conn.close()

    return jsonify({"status": "Transaction Successful", "fraud_flag": 0})

# Endpoint for Biometric Verification
@app.route('/verify', methods=['POST'])
def verify_biometric():
    image = request.files['image'].read()
    age, gender = detect_age_gender(image)
    return jsonify({"age": age, "gender": gender})

if __name__ == '__main__':
    app.run(debug=True)
