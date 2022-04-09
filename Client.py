import requests
import json

img = open('Image.jpg', 'rb')
files = {'image': img}
BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE, files = files)
print(response.text)
