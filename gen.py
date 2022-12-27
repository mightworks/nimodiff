import requests
import json
from PIL import Image
import base64
from io import BytesIO

def decodeBase64Image(imageStr: str, name: str) -> Image:
    #image = Image.open(BytesIO(base64.decodebytes(bytes(imageStr, "utf-8"))))
    #print(f'Decoded image "{name}": {image.format} {image.width}x{image.height}')
    with open('try.png', 'wb') as f:
        f.write(base64.decodebytes(bytes(imageStr, "utf-8")))
    
    image = "blah"

    return image

config = {
  "modelInputs": {
    "prompt": "me",
    "num_inference_steps": 20,
    "guidance_scale": 7.5,
    "width": 512,
    "height": 512,
    "seed": 3239022079,
  },
  "callInputs": {
    "MODEL_ID": "runwayml/stable-diffusion-v1-5",
    #"PIPELINE": "StableDiffusionPipeline",
    "PIPELINE": "lpw_stable_diffusion",
    "safety_checker": "false",
    "custom_pipeline_method": "text2img",
  },
}

res = requests.post('http://127.0.0.1:8000', json=config)

res = json.loads(res.text)

image = decodeBase64Image(res['image_base64'], 'whocares')

image.save('test.png')