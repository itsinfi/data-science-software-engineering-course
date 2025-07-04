import numpy as np
import pandas as pd

def predict(model, vars):
    # Encode categorical features
    # vars['model'] = le_model.transform([vars['model']])[0]
    # vars['fuelType'] = le_fuelType.transform([vars['fuelType']])[0]

    # Create DataFrame with correct feature order
    features = ['model', 'year', 'transmission', 'mileage', 'fuelType']
    X_new = pd.DataFrame([[vars[f] for f in features]], columns=features)

    # Predict
    prediction = model.predict(X_new)
    print("Prediction:", prediction)