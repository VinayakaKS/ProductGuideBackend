import base64
import requests
import json

test_image = open('Image.jpg','rb')
files = {'image': test_image}
BASE = "localhost:5000"

with open("Image.jpg", "rb") as image2string:
    converted_string = base64.b64encode(image2string.read())
response = requests.post(BASE, json = {'image_string':converted_string})
print(response.text)
