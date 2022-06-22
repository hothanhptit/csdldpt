from grayscale import grayScale
from gaussFilter import gaussFilter
from reason_growing import regionGrowing
from split import split
from countPixel import countPixel
import os
from histogram6Color import histogram
import json
import re
import numpy as np
from scipy.spatial import distance

ROOT_DIR = os.path.abspath(os.curdir).replace('\\', '/')
image_path = f'{ROOT_DIR}/Images'
process_path = f'{ROOT_DIR}/ProcessedImages'
# writeData = {}

def exactVector(path):
    vector = []
    # ROOT_DIR = os.path.abspath(os.curdir)
    imgName = os.path.basename(path).split('.')[0]
    # dir = f'{ROOT_DIR}/ProcessedImages'
    # isExist = os.path.exists(dir)
    # if not isExist:
    #     os.makedirs(dir)
    #     print("The new directory is created!")
    # os.chdir(dir)
    print(f"processing user image...")
    grayScale(f'{image_path}/{imgName}.jpg', f'{process_path}/{imgName}')
    gaussFilter(f'{image_path}/{imgName}.jpg', process_path)
    regionGrowing(f'{image_path}/{imgName}.jpg', f'{process_path}/{imgName}/{imgName}_reason.jpg')
    pixel = countPixel(path)
    square = pixel[0]/(pixel[1]+pixel[0])
    vector.append(square)
    split(f'{image_path}/{imgName}.jpg')
    # histogram
    for i in range(1, 17, 1):
        his = histogram(f'{process_path}/{imgName}/{i}.jpg')
        vector = vector + his
        # print(vector)

    # position
    for i in range(1, 17, 1):
        position = countPixel(f'{process_path}/{imgName}/{i}.jpg')
        if position[0]/(position[1] + 1) > 0.4:
            vector.append(1)
        else:
            vector.append(0)
    return vector










