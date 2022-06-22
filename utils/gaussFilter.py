import cv2 as cv
import os
from matplotlib import pyplot as plt

def median(path, savePath):
    img = cv.imread(rf'{path}')
    imgName = os.path.basename(path).split('.')[0]
    # Convert color from bgr (OpenCV default) to rgb
    # img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    blur2 = cv.blur(cv.imread(path), (2, 2))
    median = cv.cvtColor(blur2, cv.COLOR_RGB2BGR)
    plt.imsave(f'{savePath}/{imgName}/{imgName}_median.jpg', median)
    # cv.imwrite(f'{savePath}/{imgName}/{imgName}_median.jpg', median)

