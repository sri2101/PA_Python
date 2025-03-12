import requests
import webbrowser
from monsterapi import client
from dotenv import load_dotenv
load_dotenv()
import os

api_key = os.getenv('YOUR_MONSTERAPI_APIKEY') 
monster_client = client(api_key)

def text_to_image(text):
    model = 'txt2img'
    input_data = {
        'prompt': text,
        'negprompt': 'deformed, bad anatomy, disfigured, poorly drawn',
        'samples': 1,  
        'steps': 50,
        'aspect_ratio': 'square',
        'guidance_scale': 7.5,
        'seed': 2414,
    }
    
    result = monster_client.generate(model, input_data)
    image_url = result['output'][0]  
    file_name = "generated_image.jpg"
    
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded as {file_name}")
        webbrowser.open(file_name)  
    else:
        print("Failed to download the image.")


