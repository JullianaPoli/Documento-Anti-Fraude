import os
from dotenv import load_dotenv # type: ignore
load_dotenv()

class Config:
    blob_url = os.getenv("ENDPOINT")
    KEY = os.getenv("SUBSCRIPTION_KEY")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME") 
 
    