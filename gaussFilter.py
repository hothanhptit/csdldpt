import cv2 as cv
from matplotlib import pyplot as plt

def gaussFilter(imgPath, savePath):
    img = cv.imread(imgPath)
    # img = cv.imread('imgPath')
    # blur = cv.blur(img,(5,5))
    # Convert color from bgr (OpenCV default) to rgb
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # blur_rgb = cv.cvtColor(blur, cv.COLOR_BGR2RGB)
    img_rgb.save(savePath)

    # Display
    # plt.subplot(221),plt.imshow(img_rgb),plt.title('Gauss Noise')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(222),plt.imshow(blur_rgb),plt.title('Gauss Noise - Blurred')
    # plt.xticks([]), plt.yticks([])
