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
writeData = {}

for loopImg in range(1,112,1):
    vector = []
    euclidDistance = []
    vectorImg = []

    print(f"processing {loopImg}.jpg")
    grayScale(f'{image_path}/{loopImg}.jpg', f'{process_path}/{loopImg}')
    gaussFilter(f'{image_path}/{loopImg}.jpg', process_path)
    regionGrowing(f'{image_path}/{loopImg}.jpg', f'{process_path}/{loopImg}/{loopImg}_reason.jpg')
    pixel = countPixel(f'{image_path}/{loopImg}.jpg')
    square = pixel[0]/(pixel[1]+pixel[0])
    vector.append(square)
    split(f'{image_path}/{loopImg}.jpg')
    # histogram
    for i in range(1, 17, 1):
        his = histogram(f'{process_path}/{loopImg}/{i}.jpg')
        vector = vector + his
        # print(vector)

    # position
    for i in range(1, 17, 1):
        position = countPixel(f'{process_path}/{loopImg}/{i}.jpg')
        if position[0]/(position[1] + 1) > 0.4:
            vector.append(1)
        else:
            vector.append(0)
    writeData[f'{loopImg}.jpg'] = vector

json_data = json.dumps(writeData)
# print(json_data)
with open(f"{ROOT_DIR}/features.json", 'a') as f:
    f.write(json_data)
    # data = json_data.split('')
    # for wdata in writeData.items():
        # json.dump(wdata, f)
        # data = json.dumps(wdata)
        # f.write(data)
        # f.write('\n')
    f.close()

# with open(f"{ROOT_DIR}/vectorData.txt", 'r') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         line = line.split('has')[1].strip()
#         print(line)
#         vectorImg = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", line)
#         x = np.array(vectorImg)
#         savedVector = x.astype(float)
# euclid
#         dis = distance.euclidean(savedVector, testVector)
#         euclidDistance.append(dis)
        # print(dis)
        # print(savedVector)
        # print(line)
# for i in range(0, euclidDistance.len(), 1):
    # find min and images









