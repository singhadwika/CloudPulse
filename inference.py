import joblib
import pandas as pd

# Load model
model = joblib.load('../models/rf_model.pkl')

# Load test data
test_data = pd.read_csv('../data/test_data.csv')

# Make predictions
predictions = model.predict(test_data)
print(predictions)
