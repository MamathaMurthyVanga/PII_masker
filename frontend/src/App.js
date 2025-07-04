
import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [maskedImage, setMaskedImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) return;

    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);



    try {
      const res = await axios.post("https://f29a-115-98-181-49.ngrok-free.app/mask-pii", formData, {
        responseType: "blob",
      });
  
      console.log("Response blob type:", res.data.type);

      const url = URL.createObjectURL(res.data);
      setMaskedImage(url);
    } catch (err) {
      console.error("Error uploading image:", err);
    }
    setLoading(false);
  };

  return (
    <div className="app-container">
      <div className="card">
        <h2>🔒 PII Masking Tool</h2>
        <form onSubmit={handleUpload} className="upload-form">
          <input
            type="file"
            accept="image/*"
            onChange={(e) => setFile(e.target.files[0])}
            className="file-input"
            required
          />
          <button type="submit" className="upload-button" disabled={loading}>
            {loading ? "Processing..." : "Upload & Mask"}
          </button>
        </form>

        {maskedImage && (
          <div className="result">
            <h3>🖼️ Masked Image:</h3>
            <img src={maskedImage} alt="Masked Result" className="masked-image" />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
