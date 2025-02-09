import numpy as np
import pandas as pd
from fastapi import FastAPI
import joblib

app = FastAPI()

# Load trained model
model = joblib.load("lung_cancer_model.pkl")

@app.post("/predict")
def predict_lung_cancer(data: dict):
    try:
        # Convert input data to NumPy array
        input_data = np.array([[
            data['age'], data['smoking'], data['yellow_fingers'],
            data['anxiety'], data['peer_pressure'], data['chronic_disease'],
            data['fatigue'], data['allergy'], data['wheezing'],
            data['alcohol_consumption'], data['coughing'],
            data['shortness_of_breath'], data['swallowing_difficulty'],
            data['chest_pain']
        ]])

        # If "lung_cancer" is missing, add a default value (e.g., 0)
        if 'lung_cancer' in data:
            input_data = np.append(input_data, [[data['lung_cancer']]], axis=1)
        else:
            input_data = np.append(input_data, [[0]], axis=1)  # Default to 0

        # Make prediction
        prediction = model.predict(input_data)
        return {"lung_cancer_prediction": int(prediction[0])}

    except Exception as e:
        return {"error": str(e)}
