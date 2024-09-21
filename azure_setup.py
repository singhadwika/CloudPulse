from azureml.core import Workspace, Dataset, Datastore
from azureml.core.authentication import InteractiveLoginAuthentication

# Azure login and workspace creation
interactive_auth = InteractiveLoginAuthentication()
ws = Workspace.create(name='my_azure_workspace',
                      subscription_id='<SUBSCRIPTION_ID>',
                      resource_group='my_resource_group',
                      create_resource_group=True,
                      location='eastus',
                      auth=interactive_auth)

# Upload data to Azure Blob Storage
datastore = Datastore.get(ws, datastore_name='workspaceblobstore')
datastore.upload(src_dir='../data/', target_path='predictive-maintenance-data/', overwrite=True)

# Register the dataset
dataset = Dataset.File.from_files(path=(datastore, 'predictive-maintenance-data/'))
dataset.register(workspace=ws, name='turbofan_data')
print("Data uploaded to Azure and dataset registered.")
