import os
import pandas as pd
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Load Secrets from .env file
load_dotenv()

# Connet to Azure blob
blob_service = BlobServiceClient.from_connection_string(
    os.getenv("AZURE_BLOB_CONN_STR")
)
container_client = blob_service.get_container_client(os.getenv("AZURE_BLOB_CONTAINER"))


# Download the file from Azure blob storage
def download_file_from_blob(blob_name, local_path):
    with open(local_path, "wb") as file:
        blob_client = container_client.get_blob_client(blob_name)
        file.write(blob_client.download_blob().readall())


download_file_from_blob("employee_data.csv", "../data/employee_data.csv")
# Read the CSV file into a DataFrame
df = pd.read_csv("../data/employee_data.csv")
print("Data loaded successfully with shape:", df.shape)
print("Data preview:\n", df.head())
