# AI-Driven Fraud Detection & Secure Transaction System

An AI-powered system for real-time fraud detection and secure transactions. This project integrates deep learning models for biometric authentication (age and gender detection) and fraud detection, ensuring secure and seamless digital transactions.

## Features
- **Real-Time Fraud Detection**: AI models analyze transaction patterns to detect anomalies.
- **Biometric Authentication**: Age and gender detection for secure KYC verification.
- **Secure Transactions**: Encrypted transaction processing with fraud prevention mechanisms.
- **Cloud & Edge Optimized**: Deployable on both cloud and edge devices.

## Tech Stack
- **Frontend**: React.js
- **Backend**: Flask (Python)
- **AI Models**: DeepFace (for age/gender detection), IsolationForest (for fraud detection)
- **Database**: SQLite
- **Real-Time Processing**: WebSockets
- **Security**: HTTPS, AES-256 encryption

## Installation
### Prerequisites
- Python 3.8+
- Node.js 14+
- TensorFlow 2.x
- OpenCV 4.x

## Project Structure
```
fraud-detection-system/
├── backend/               # Flask backend and API
│   ├── app.py             # Main Flask application
│   ├── models/            # AI models and utilities
│   └── requirements.txt   # Python dependencies
├── frontend/              # React.js frontend
│   ├── public/            # Static assets
│   ├── src/               # React components
│   └── package.json       # Node.js dependencies
├── ai_models/             # AI model scripts
│   ├── age_gender_detection.py  # Age and gender detection using DeepFace
│   └── fraud_detection.py       # Fraud detection using IsolationForest
└── README.md              # Project documentation
