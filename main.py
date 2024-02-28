import sys
import os
from openai_utils.image_genarator import OpenaiUtils
from azure_utils.azure_utils import AzureUtils
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()
openai = OpenaiUtils()
azure = AzureUtils()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Image(BaseModel):
    description: str


@app.post("/generate_image")
async def train(image: Image):
    img_url = azure.upload_image(image.description)

    return {"Img_url": img_url}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7005, proxy_headers=True)




