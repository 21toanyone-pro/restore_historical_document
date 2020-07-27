import numpy as np
import os
import glob
import random
import cv2 as cv
import natsort
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import shutil
import re

bground_path = './img/'
bground_list = os.listdir(bground_path)



save = open('텍스트.txt', 'w', encoding='utf-8')
kernel_3 = np.ones((3,3),np.uint8)
for q in bground_list:  #글자 이름
    #num = 23
    real_path = bground_path + str(q)
    # 이미지 불러오는 곳
    gray_img = Image.open(real_path).convert("RGBA")
    gray_img = np.array(gray_img)
    gray = cv.cvtColor(gray_img, cv.COLOR_BGR2GRAY)
    ret, gray_img = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+ cv.THRESH_OTSU)
    gray_img= cv.dilate(gray_img, kernel_3,iterations=1)
    gray_img=Image.fromarray(gray_img)
    
    datas = gray_img.getdata()
    newData = []
    cutOff = 150
    for item in datas:
        if item[0] >= cutOff and item[1] >= cutOff and item[2] >= cutOff:
            newData.append((150, 150, 150, 0))
            # RGB의 각 요소가 모두 cutOff 이상이면 transparent하게 바꿔줍니다.
        else:
            newData.append(item)
            # 나머지 요소는 변경하지 않습니다.
    gray_img.putdata(newData)

    str_path = str(q)
    str_path = str_path.replace('.png', '')
    str_path = str_path.replace('_fake_B', '')
    str_path = re.sub('[0-9]','',str_path)
    floder_name = str_path
    gray_img= gray_img.resize((120,120))

    save_path = './save3/' + str(floder_name)
    save.write(str(floder_name))
    gray_img.save(save_path+'.png')  
