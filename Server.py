
from flask import Flask, request
import os
from PIL import Image
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd 

app = Flask("__name__")
app.config["Debug"] = True

@app.route('/', methods = ["POST"])
def OCR():

    #Reciving the image from client
    file = request.files['image']
    image = Image.open(file)
    
    #Easy OCR
    reader = easyocr.Reader(['en'], gpu = False)
    result = reader.readtext('Image.jpg')
    
    #Putting the result to ingredients list
    ingredients_list=[]
    y = len(result) 
    for x in range (0, y):
        OCR_text = result[x][1]
        ingredients_list.append(result[x][1])
        x = x+1
    
    #Checking if the ingredients list has any toxic substances
    Chemicals_dataframe = pd.read_excel('Chemicals.xls', sheet_name=0) 
    chemicals_list = Chemicals_dataframe['Chemical Name'].tolist()
    toxic_list = []
    for i in range(len(chemicals_list)):
        check = chemicals_list[i]
        for j in range(len(ingredients_list)):
            if check in ingredients_list[j]:
                toxic_list.append(check)
    print(ingredients_list)
    #Recommendation
    recommendation = "Buy"
    if (len(toxic_list) != 0):
        recommendation = "Don't Buy"
    #Returning the result in JSON format           
    res = {"Toxic": toxic_list, "Recommendation": recommendation}
    return res

if __name__ == '__main__':
    app.run()
