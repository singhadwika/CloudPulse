import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load processed data
data = pd.read_csv('../data/processed_data.csv')

# Splitting data
X = data.drop(['time_to_failure'], axis=1)
y = data['time_to_failure']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Save the model
import joblib
joblib.dump(model, '../models/rf_model.pkl')

print(f"Model Training Complete. Mean Squared Error: {mse:.4f}")
