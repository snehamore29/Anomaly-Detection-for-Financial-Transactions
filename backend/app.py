import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import numpy as np
import cv2
from ai_models.age_gender_detection import detect_age_gender
from ai_models.fraud_detection import detect_fraud

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def init_db():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (id INTEGER PRIMARY KEY, amount REAL, recipient TEXT, fraud_flag INTEGER)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/transaction', methods=['POST'])
def process_transaction():
    data = request.json
    amount = float(data.get('amount', 0))
    recipient = data.get('recipient', '')

    fraud_flag = detect_fraud(amount)

    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute("INSERT INTO transactions (amount, recipient, fraud_flag) VALUES (?, ?, ?)",
              (amount, recipient, int(fraud_flag)))
    conn.commit()
    conn.close()

    status = "Fraud Detected" if fraud_flag else "Transaction Successful"
    return jsonify({"status": status, "fraud_flag": int(fraud_flag)})

@app.route('/verify', methods=['POST'])
def verify_biometric():
    if 'image' not in request.files:
        print("❌ No image uploaded in request.files")
        return jsonify({"error": "No image uploaded"}), 400

    try:
        file = request.files['image']
        print("✅ Image received:", file.filename)

        npimg = np.frombuffer(file.read(), np.uint8)
        image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        if image is None:
            print("❌ Image decoding failed")
            return jsonify({"error": "Invalid image"}), 400

        age, gender = detect_age_gender(image)
        print("✅ DeepFace result:", age, gender)
        return jsonify({"age": age, "gender": gender})
    except Exception as e:
        print("❌ Error in /verify route:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
