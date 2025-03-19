import React, { useState } from 'react';
import Webcam from 'react-webcam';

function App() {
  const [amount, setAmount] = useState('');
  const [recipient, setRecipient] = useState('');
  const [fraudStatus, setFraudStatus] = useState('');
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('');
  const webcamRef = React.useRef(null);

  const handleTransaction = async () => {
    const response = await fetch('http://localhost:5000/transaction', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ amount, recipient }),
    });
    const result = await response.json();
    setFraudStatus(result.status);
  };

  const handleBiometricVerification = async () => {
    const image = webcamRef.current.getScreenshot();
    const formData = new FormData();
    formData.append('image', image);

    const response = await fetch('http://localhost:5000/verify', {
      method: 'POST',
      body: formData,
    });
    const result = await response.json();
    setAge(result.age);
    setGender(result.gender);
  };

  return (
    <div>
      <h1>Secure Transaction System</h1>
      <div>
        <label>Amount:</label>
        <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} />
      </div>
      <div>
        <label>Recipient:</label>
        <input type="text" value={recipient} onChange={(e) => setRecipient(e.target.value)} />
      </div>
      <button onClick={handleTransaction}>Process Transaction</button>
      <p>{fraudStatus}</p>

      <h2>Biometric Verification</h2>
      <Webcam ref={webcamRef} screenshotFormat="image/jpeg" />
      <button onClick={handleBiometricVerification}>Verify</button>
      <p>Age: {age}, Gender: {gender}</p>
    </div>
  );
}

export default App;
