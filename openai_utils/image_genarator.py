import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import json
from PIL import Image
import requests
from constants.constants import *
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from prompts.prompts import Prompts

load_dotenv()
system_message = Prompts()

class OpenaiUtils:
    def __init__(self) -> None:
        
        self.client = AzureOpenAI(
            api_key=OPENAI_API_KEY,
            api_version=OPENAI_API_VERSION,
            azure_endpoint=AZURE_OPENAI_ENDPOINT
        )

        
    def generate_image(self, description):

        # print(payload)
        prompt = system_message.system_message(description)
        

        try:
            result = self.client.images.generate(
                        model=os.environ.get("MODEL"),
                        prompt=prompt,
                        n=1
                        )
        
            # print the response
            json_response = json.loads(result.model_dump_json())

            image_url = json_response["data"][0]["url"]  # extract image URL from response
            generated_image = requests.get(image_url).content

            return generated_image


        except Exception as e:
            print(e)
        
    # def generate_image(self, description):
    #     try:
    #         result = self.client.images.generate(
    #                     model=os.environ.get("MODEL"),
    #                     prompt=description,
    #                     n=1
    #                     )
        
    #         json_response = json.loads(result.model_dump_json())
    #         image_url = json_response["data"][0]["url"]  # extract image URL from response
    #         return image_url


    #     except Exception as e:
    #         print(e) 


# ai = OpenaiUtils()
# ai.generate_image("A picture of a pizza")