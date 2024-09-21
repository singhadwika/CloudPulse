import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load dataset
def load_data(file_path):
    data = pd.read_csv(file_path, delim_whitespace=True, header=None)
    data.columns = ['unit_number', 'time_in_cycles', 'operational_setting_1', 'operational_setting_2',
                    'operational_setting_3', 'sensor_measurement_1', 'sensor_measurement_2', 'sensor_measurement_3',
                    # Add more sensor columns as per the dataset
                    'sensor_measurement_21']
    return data

# Data scaling
def scale_data(data):
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)
    return pd.DataFrame(data_scaled)

# Feature extraction
def feature_engineering(data):
    data['time_to_failure'] = data.groupby('unit_number')['time_in_cycles'].transform(max) - data['time_in_cycles']
    return data

if __name__ == "__main__":
    file_path = "../data/nasa_turbofan_dataset.csv"
    data = load_data(file_path)
    data = feature_engineering(data)
    data_scaled = scale_data(data)
    data_scaled.to_csv('../data/processed_data.csv', index=False)
    print("Data preprocessing complete.")
