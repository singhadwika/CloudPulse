# Predictive Maintenance for Cloud Infrastructure

This project aims to predict failures in cloud infrastructure, specifically cloud servers, by leveraging machine learning techniques to monitor system performance data. Predictive maintenance can help optimize cloud resource allocation and reduce downtime, which is critical in cloud services like Microsoft Azure.

## Dataset
We utilize the NASA Turbofan Engine Degradation Simulation Dataset, which simulates equipment degradation over time. This dataset has been adapted to reflect cloud infrastructure by drawing parallels between hardware wear in engines and cloud servers.

- **Dataset Link:** [NASA Turbofan Dataset](https://data.nasa.gov/Aerospace/Turbofan-engine-degradation-simulation-data-set/2dqk-8jzv)

## Architecture
1. **Data Preprocessing:** Feature extraction and scaling are applied to the raw dataset.
2. **Modeling:** A random forest regressor is trained to predict remaining time to failure.
3. **Azure Integration:** Azure Machine Learning and Azure Blob Storage are used for data storage, model deployment, and inference.

## Features
- Predicts the remaining time to failure based on historical data.
- Handles time-series sensor data for accurate maintenance predictions.
- Real-time inference capabilities using Azure services.

## Model Training
The model is trained using a Random Forest algorithm, and the training script is located at `scripts/model_training.py`. Model evaluation is performed using Mean Squared Error (MSE).

## Deployment
The model can be deployed as an Azure Web Service using the `azure_deployment/azure_setup.py` script. It also supports local inference.

### Steps to deploy on Azure:
1. Run `azure_setup.py` to upload data and connect to Azure workspace.
2. Register the model using `model_register.py`.
3. Deploy the model using Azure Machine Learning Service.

## Azure Integration
The project integrates with the following Microsoft Azure services:
- **Azure Machine Learning Service:** Used to train and deploy the predictive maintenance model.
- **Azure Blob Storage:** Used to store datasets and model artifacts.

## Results
- **Mean Squared Error:** Achieved a MSE of 0.035 on the test set.
- The model is capable of real-time predictions to optimize server maintenance.

## Future Work
- Implement real-time streaming data for dynamic predictive maintenance.
- Explore different models like LSTMs for better time-series prediction.
- Extend the system to other cloud infrastructure components (e.g., networking equipment).

## Contributing
We welcome contributions! Please open an issue or create a pull request.
