from grayscale import grayScale
from gaussFilter import gaussFilter
from reason_growing import regionGrowing
from split import split
from countPixel import countPixel
import os

vector = []
ROOT_DIR = os.path.abspath(os.curdir)
gaussFilter('./venv/Images/img/88.jpg')
print('ok')
grayScale('C:/Users/Admin/PycharmProjects/CSDLDPT/venv/Images/img/2.jpg', 'C:/Users/Admin/PycharmProjects/CSDLDPT/venv/Images/img/2_gray.jpg')
print('ok')
regionGrowing('C:/Users/Admin/PycharmProjects/CSDLDPT/venv/Images/img/2.jpg', 'C:/Users/Admin/PycharmProjects/CSDLDPT/venv/Images/img/2_rea.jpg')
print('ok')
pixel = countPixel('C:/Users/Admin/PycharmProjects/CSDLDPT/venv/Images/img/2.jpg')
square = pixel[0]/(pixel[1]+1)
print(pixel)
vector.append(square)
split('C:/Users/Admin/PycharmProjects/CSDLDPT/venv/Images/img/2_gray.jpg')
print('ok')
path = 'C:/Users/Admin/PycharmProjects/CSDLDPT/2'
for i in range(1, 17, 1):
    position = countPixel(f'{path}/{i}.jpg')
    if position[0]/(position[1] + 1) > 0.4:
        vector.append(1)
    else:
        vector.append(0)
print(vector)







