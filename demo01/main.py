#-*-coding: utf-8-*-
## 表情包制作
import os
# use pillow lib
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# read the number to add 
num = input('enter the string you want to add: ')
# calculate the length shall we drawback
strlen = int(len(num)) * 18

# get the absolute path of target image
imgPath = os.getcwd()

# open target image
targetImg = Image.open(imgPath + '\\demo.jpg')
# set font family and size
font = ImageFont.truetype('font/msyh.ttc', 18)
# calculate the position
w, h = targetImg.size
# add subscribe to target
draw = ImageDraw.Draw(targetImg);
draw.text(((w - strlen)/2, h - 30), num, (255, 0, 0), font)
draw = ImageDraw.Draw(targetImg)
# save changes
targetImg.save("result.jpg")

# show result image with self control
targetImg.show()