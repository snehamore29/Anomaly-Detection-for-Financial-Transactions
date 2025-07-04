 How It Works
User enters a transaction (amount & recipient)

Flask API detects if the transaction is fraudulent

User verifies biometric identity via webcam

DeepFace predicts age and gender

Transaction is securely logged in database



fraud-detection-system/
├── backend/ # Flask backend & API
│ ├── app.py # Main API server
│ ├── models/ # (optional AI model storage)
│ └── requirements.txt # Python dependencies
├── frontend/ # React.js frontend
│ ├── public/ # Static assets
│ ├── src/ # React components
│ └── package.json # NPM dependencies
├── ai_models/ # AI model logic
│ ├── age_gender_detection.py
│ └── fraud_detection.py


How to Run the Project

Step 1: Run the Backend (Flask API)
bash
Copy
Edit
# 1. Go to the backend directory
cd backend

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the environment
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1


# 4. Install dependencies
pip install -r requirements.txt

# pip install flask flask-cors deepface opencv-python scikit-learn numpy tf-keras

# 5. Start the backend server
python app.py
The backend will run at: http://localhost:5000

⚛️ Step 2: Run the Frontend (React App)
bash
Copy
Edit
# 1. Open a new terminal and go to the frontend folder
cd ../frontend

# 2. Install frontend dependencies
npm install
npm install react-webcam

# 3. Start the React development server
npm start

Step 3: Test the App
Enter transaction amount and recipient, then click "Process Transaction".

Use your webcam to verify identity via "Verify Identity".

The backend will return age, gender, and fraud status in real-time.