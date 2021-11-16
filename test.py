import cv2
import os 
import requests
from io import BytesIO
from PIL import Image

# cmd = 'wget http://0.0.0.0/pic/Venice_3840x2160_60fps_10bit_420_1920x1080_BC.png'
# os.system(cmd)
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
re = requests.get('http://0.0.0.0:80/pic/Venice_3840x2160_60fps_10bit_420_1920x1080_BC.png',headers=headers).content
re = BytesIO(re)
re = Image.open(re)
re.show()
print(re)

img = cv2.imread('http://0.0.0.0/pic/Venice_3840x2160_60fps_10bit_420_1920x1080_BC.png')
print(img.shape)
cv2.imshow('tet',img)