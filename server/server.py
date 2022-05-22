import base64
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
    file = request.json['image_string']
    # return {"Toxic": ['1','2','3'], "Recommendation": "recommendation"}
    decodeit = open('recieved_image.jpg', 'wb')
    decodeit.write(base64.b64decode((file)))
    received_image_var = cv2.imread('recieved_image.jpg',0)

    #Preprocessing
    # kernel = np.ones((5,5),np.uint8)
    # erosion = cv2.erode(received_image_var,kernel,iterations = 1)

    #Easy OCR
    reader = easyocr.Reader(['en'], gpu = False)
    ocr_result = reader.readtext(received_image_var)

    #Putting the result to ingredients list
    ocr_result_list=[]
    check_list=[]
    y = len(ocr_result) 
    for x in range (0, y):
        OCR_text = ocr_result[x][1]
        ocr_result_list.append(ocr_result[x][1])
        check_list.append(ocr_result[x][1].lower())
        x = x+1
    
    #Checking if the ingredients list has any toxic substances
    Chemicals_dataframe = pd.read_excel('Chemicals_list.xls', sheet_name=0) 
    chemicals_list = Chemicals_dataframe['Chemical Name'].tolist()
    toxic_list = []
    for i in range(len(chemicals_list)):
        check = chemicals_list[i].lower()
        for j in range(len(check_list)):
            if check in check_list[j]:
                toxic_list.append(check)
    print(ocr_result_list)

    #Recommendation
    recommendation = "Safe"
    if (len(toxic_list) != 0):
        recommendation = "Not Safe"
        
    #Returning the result in JSON format           
    final_result = {"Toxic": toxic_list, "Recommendation": recommendation}
    return final_result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
