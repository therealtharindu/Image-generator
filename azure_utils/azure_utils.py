from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv
from openai_utils.image_genarator import OpenaiUtils
from PIL import Image
import io
from constants.constants import *
import requests

load_dotenv()
openai = OpenaiUtils()

class AzureUtils:

    def __init__(self) -> None:
        self.storage_connection_string = CONNECTION_STRING
        self.blob_service_client = BlobServiceClient.from_connection_string(self.storage_connection_string)


    def upload_image(self, description, user_id, img_name):
        try:
            blob_name = f"{img_name}.jpg"
            container_name = user_id
            image_url = openai.generate_image(description)
            generated_image = requests.get(image_url).content
            image = Image.open(io.BytesIO(generated_image))
            image.show()

            # Check if the container exists and create it if it doesn't
            container_client = self.blob_service_client.get_container_client(container_name)
            if not container_client.exists():
                self.blob_service_client.create_container(container_name)


            # Create a blob client using the local file name as the name for the blob
            blob_client = self.blob_service_client.get_blob_client(container_name, blob_name)

            # Upload the created file
            blob_client.upload_blob(generated_image, overwrite=True)
            print("Image has been uploaded successfully.")

            blob_url = f"https://{self.blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}"
            print(blob_url)

            return blob_url

        except Exception as e:
            print("Error uploading image to Azure Blob Storage: ", e)

        
