from azureml.core import Model
from azureml.core import Workspace

# Connect to Azure workspace
ws = Workspace.from_config()

# Register the model
model = Model.register(workspace=ws, 
                       model_path="../models/rf_model.pkl", 
                       model_name="predictive_maintenance_rf_model")

print("Model registered in Azure ML workspace.")
