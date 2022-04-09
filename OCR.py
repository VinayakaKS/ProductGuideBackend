import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

image_path = 'Hair_oil.jpg'
image = cv2.imread(image_path)

reader = easyocr.Reader(['en'], gpu = False)
result = reader.readtext(image)

ingredients_list=[]
y = len(result) 
for x in range (0, y):
    OCR_text = result[x][1]
    ingredients_list.append(result[x][1])
    x = x+1
print(ingredients_list)

Chemicals_dataframe = pd.read_excel('Chemicals.xlsx', sheet_name=0) 
chemicals_list = Chemicals_dataframe['Chemical Name'].tolist()
#print(chemicals_list)
toxic_list = []
for i in range(len(chemicals_list)):
    check = chemicals_list[i]
    for j in range(len(ingredients_list)):
        if check in ingredients_list[j]:
            toxic_list.append(check)
print(toxic_list)
print(len(toxic_list))