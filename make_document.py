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
import csv

char_C =[]
img_C = []
img_I = []
filename = '광해군정초본.txt' #kor_data.txt #chin_chosen.txt
img_path = './characters/'
bground_list = os.listdir(img_path)

def create_an_image(bground_path):
    bground_list = os.listdir(bground_path)
    bground_a = Image.open(bground_path+str(bground_list[0]))
    bground_b = Image.open(bground_path+str(bground_list[1]))
    return bground_a, bground_b
#432

page_a = [2060, 1926, ]

#page_b = [2060-(k*130)-4*k]

#페이지 a에 그려주는 함수
def creat_img_A(img, back_img, k, n):
    if k ==15:
        back_img.paste(img, (int(2070-(k*130)-(3.5*15)), 435 + 105*n),img)
    else:
        back_img.paste(img, (2060-(k*130)-4*(int(k*0.9)), 435 + 105*n),img)
    return back_img

#페이지 b에 그려주는 함수
def creat_img_B(img, back_img, k, n):
    back_img.paste(img, (2060-(k*135)+(3*k), 435 + 105*n),img)
    return back_img

def main_fc():
    qq = []
    del qq[:]
    main =[]
    del main[:]
    poly =[]
    del poly[:]
    append_Poly = poly.append
    append_Main = main.append

    for k in bground_list:
        real_path = img_path + str(k) #이미지 주소
        gray_img = Image.open(real_path).convert("RGB") # 이미지 오픈
        str_path = str(k)
        
        str_path = str_path.replace('.jpg', '')
        str_path = str_path.replace('.png', '')
        floder_name = str_path

        img_C.append(floder_name)
        img_I.append(real_path)


    Dic = {}
    for i in range(len(bground_list)):
        Dic[img_C[i]] =  img_I[i]

    with open(filename, 'r', encoding='utf-8') as file_object:
        contents = file_object.read()

    for j in range(len(contents)):
        char_C.append(contents[j])
    # 글자를 이미지에 매칭 하는 작업

    #배경 이미지 로드
    back_img_a, back_img_b  = create_an_image('./background/') 

    n = 0 #계산용 수
    k = 0 #줄 수
    c = 0
    k = int(n //27)
    p = 0 #페이지 수
    line = 16

    ll = []
    for k in range(0,len(qq)): # C에 있는 값 중 0과 1의 값만 중요하기 때문에 이 값을 main에 저장
        append_Poly(qq[k])
        real =[int(poly[k][0]),int(poly[k][1])]
        append_Main(real)


    print(ll)
    for q in range(len(char_C)):
        kk = Dic[char_C[q]]
        img = Image.open(kk)
        k = int(int(n //27) % line)  #페이지 수
        c = c + 1
        if p % 2 ==0: 
            back_img_a =creat_img_A(img, back_img_a, k, int(n%27))
            if c == 432:
                back_img_a.save('./광해군일기/'+str(p)+'_a.jpg') 
                back_img_a, _  = create_an_image('./background/') 
                p = p+1
                c =0
        elif p % 2 ==1:
            back_img_b =creat_img_B(img, back_img_b, k, int(n%27))
            if c == 432:
                back_img_b.save('./광해군일기/'+str(p)+'_b.jpg') 
                _, back_img_b  = create_an_image('./background/') 
                p = p+1
                c =0
        n = n+1

if __name__ == "__main__":
    main_fc()

## 세로 27, 가로 16












