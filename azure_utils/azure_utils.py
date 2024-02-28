from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv
from openai_utils.image_genarator import OpenaiUtils
from PIL import Image
import io
from constants.constants import *

load_dotenv()
openai = OpenaiUtils()

class AzureUtils:

    def __init__(self) -> None:
        self.storage_connection_string = CONNECTION_STRING
        self.blob_service_client = BlobServiceClient.from_connection_string(self.storage_connection_string)
        self.container_name = "images"
        self.blob = "pizza.png"

    
    def upload_image(self, description):
        try:
            generated_image = openai.generate_image(description)

            # Optionally display the image (comment this if not needed)
            image = Image.open(io.BytesIO(generated_image))
            image.show()
            # Upload the image data directly to blob storage
            with self.blob_service_client.get_blob_client(container=self.container_name, blob=self.blob) as blob_client:
                blob_client.upload_blob(generated_image, overwrite=True)

            # Print the blob URL
            blob_url = f"https://{self.blob_service_client.account_name}.blob.core.windows.net/{self.container_name}/{self.blob}"
            print(f"Image has been uploaded to: {blob_url}")

            return blob_url
            
        except Exception as e:
            print(e)

# azure = AzureUtils()
# azure.upload_image()