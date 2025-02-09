🚀 Lung Cancer Prediction API

📌 Author: Tesfaye Samson  
📌 Student ID: 1402506  


📖 Overview
This project provides a **Machine Learning API** to predict lung cancer based on input symptoms. The model is trained using a dataset and deployed using **FastAPI**.

🔹 Key Features:
- Machine learning model training.
- API deployment using FastAPI.
- Interactive Swagger UI for testing.
- Well-documented dataset and process.


 📂 Project Structure

| 📁 File/Folder | 📌 Description |
|--------------|-------------|
| `unitedMODEL.py` | Python script for training and creating the ML model. |
| `united.py` & `app.py` | FastAPI code to deploy the model. |
| `updated_survey_lung_cancer.csv` | Dataset used for training. (See **ML_DOC** for details). |
| `lung_cancer_model.pkl` | Pre-trained ML model. |
| `input_case2.json` | Sample input JSON file for testing predictions. |


🚀 How to Deploy the API

Follow these simple steps to run the API on your local machine:

🛠 1. Setup Environment
1️⃣ Navigate to the project folder:

cd path/to/folder

2️⃣ Install dependencies (Ensure you have FastAPI and Uvicorn installed):

pip install fastapi uvicorn

 🚀 2. Run the API Server
Start the FastAPI server using the following command:

uvicorn app:app --host 0.0.0.0 --port 8000 --reload


📌 Note: Run this inside your Anaconda environment if necessary.



## 🎯 Test the API

### 🔎 **Interactive Testing with Swagger UI**
Once the server is running, open your browser and go to:
📌 **[Swagger UI Docs](http://127.0.0.1:8000/docs)**

### 📝 **Test Prediction with Input File**
1️⃣ Find the **POST /predict** endpoint.
2️⃣ Click **Try it out**.
3️⃣ Paste the content of `input_case2.json`.
4️⃣ Click **Execute** and check the prediction response.

---

## 🎯 Example API Request
### 🔹 Request (JSON Input)
```json
{
    "age": 55,
    "smoking": 1,
    "yellow_fingers": 0,
    "anxiety": 1,
    "peer_pressure": 1,
    "chronic_disease": 0,
    "fatigue": 1,
    "allergy": 0,
    "wheezing": 1,
    "alcohol_consumption": 0,
    "coughing": 1,
    "shortness_of_breath": 1,
    "swallowing_difficulty": 0,
    "chest_pain": 1,
    "lung_cancer": 1  
}

```
### 🔹 Response (Prediction Output)
```json
{
    "prediction": "Positive"
}
```

---

## 📌 Additional Notes
- The dataset and ML process are fully explained in **ML_DOC**.
- Ensure all dependencies are installed before running.
- The trained model (`lung_cancer_model.pkl`) is already included.

---

### 🎉 **Enjoy Predicting Lung Cancer with AI!** 🚀


