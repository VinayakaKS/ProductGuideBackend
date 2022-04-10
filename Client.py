import base64
import requests
import json

img = open('Image.png', 'rb')
files = {'image': img}
BASE = "http://127.0.0.1:5000/"

with open("Image.png", "rb") as image2string:
    converted_string = base64.b64encode(image2string.read())

response = requests.post(BASE, json = {'string1':converted_string})
print(response.text)