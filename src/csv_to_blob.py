from azure.storage.blob import BlobClient
from azure.identity import DefaultAzureCredential

# This script uploads a file to Azure Blob Storage using Azure Identity for authentication.
##################################################################################################3
# Define storage account and blob details
account_url = "https://employeedata001.blob.core.windows.net"
container_name = "hr-data"
blob_name = "employee_data_v2.csv"

# Authenticate with Azure AD
credential = DefaultAzureCredential()

# Create BlobClient
blob = BlobClient(
    account_url=account_url,
    container_name=container_name,
    blob_name=blob_name,
    credential=credential,
)

# Upload the file
with open(
    r"C:\Users\AbiolaLawani\my_workspace\employee_attrition_model\attrition_\ai_powered_attriton_system\employee_data.csv",
    "rb",
) as data:
    blob.upload_blob(data, overwrite=True)

print("Upload successful with Azure Identity!")
