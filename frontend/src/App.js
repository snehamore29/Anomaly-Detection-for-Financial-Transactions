import React, { useState, useRef } from 'react';
import Webcam from 'react-webcam';

function App() {
  const [amount, setAmount] = useState('');
  const [recipient, setRecipient] = useState('');
  const [fraudStatus, setFraudStatus] = useState('');
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('');
  const webcamRef = useRef(null);

  const handleTransaction = async () => {
    try {
      const response = await fetch('http://localhost:5000/transaction', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ amount, recipient }),
      });

      const result = await response.json();
      setFraudStatus(result.status);
    } catch (err) {
      console.error("Transaction error:", err);
      alert("Transaction failed.");
    }
  };

  const handleBiometricVerification = async () => {
  const imageSrc = webcamRef.current.getScreenshot();

  if (!imageSrc) {
    alert("Webcam image not captured");
    return;
  }

  // Convert base64 → Blob
  const byteString = atob(imageSrc.split(',')[1]);
  const mimeString = imageSrc.split(',')[0].split(':')[1].split(';')[0];
  const ab = new ArrayBuffer(byteString.length);
  const ia = new Uint8Array(ab);
  for (let i = 0; i < byteString.length; i++) {
    ia[i] = byteString.charCodeAt(i);
  }
  const blob = new Blob([ab], { type: mimeString });

  const formData = new FormData();
  formData.append('image', blob, 'webcam.jpg');

  try {
    const response = await fetch('http://localhost:5000/verify', {
      method: 'POST',
      body: formData,
    });

    const contentType = response.headers.get("content-type");

    if (!response.ok || !contentType.includes("application/json")) {
      const errText = await response.text();
      throw new Error("Response error: " + errText);
    }

    const result = await response.json();
    console.log("DeepFace result:", result);
    setAge(result.age);
    setGender(result.gender);
  } catch (err) {
    console.error("Biometric verification failed:", err);
    alert("Biometric verification failed. See console for details.");
  }
};


  return (
    <div style={{ padding: '20px' }}>
      <h1>🔒 AI-Powered Secure Transaction System</h1>

      <div style={{ marginBottom: '10px' }}>
        <label>Amount: </label>
        <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} />
      </div>

      <div style={{ marginBottom: '10px' }}>
        <label>Recipient: </label>
        <input type="text" value={recipient} onChange={(e) => setRecipient(e.target.value)} />
      </div>

      <button onClick={handleTransaction}>Process Transaction</button>
      <p><strong>Status:</strong> {fraudStatus}</p>

      <hr />

      <h2>🧠 Biometric Verification</h2>
      <Webcam ref={webcamRef} screenshotFormat="image/jpeg" width={300} />
      <br />
      <button onClick={handleBiometricVerification}>Verify Identity</button>
      <p><strong>Age:</strong> {age}</p>
      <p><strong>Gender:</strong> {gender}</p>
    </div>
  );
}

export default App;
