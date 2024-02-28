import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import json
from PIL import Image
import requests

load_dotenv()

class OpenaiUtils:
    def __init__(self) -> None:
        
        self.client = AzureOpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
            api_version=os.environ.get("API_VERSION"),
            azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT")
        )

        
    def generate_image(self):

        # print(payload)

        try:
            result = self.client.images.generate(
                        model=os.environ.get("MODEL"),
                        prompt="a close up image of a pizza having ingredients as pepperoni and three basil leaves",
                        n=1
                        )

            # print the response
            json_response = json.loads(result.model_dump_json())

            # Set the directory for the stored image
            image_dir = os.path.join(os.curdir, 'images')

            # If the directory doesn't exist, create it
            if not os.path.isdir(image_dir):
                os.mkdir(image_dir)

            # Initialize the image path (note the filetype should be png)
            image_path = os.path.join(image_dir, 'generated_image.png')

            # Retrieve the generated image
            image_url = json_response["data"][0]["url"]  # extract image URL from response
            generated_image = requests.get(image_url).content  # download the image
            with open(image_path, "wb") as image_file:
                image_file.write(generated_image)

            # Display the image in the default image viewer
            image = Image.open(image_path)
            image.show()

        except Exception as e:
            print(e)


dalle = OpenaiUtils()
dalle.generate_image()