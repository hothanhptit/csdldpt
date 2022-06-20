import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
# ./venv/Images/image1.jpg
img = mpimg.imread('./venv/Images/image1.jpg')
gray = rgb2gray(img)
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()

# img = cv2.imread("./venv/Images/image2.jpg", 0)
# plt.imshow(img)

# hist = cv2.calcHist(
#       [img],
#       channels = [0],
#       mask=None, # full image
#       histSize=[256], #full scale
#       ranges=[0,256]
# )
# plt.plot(hist)


# h2 = np.histogram(img.ravel(), bins=256, range=[0,256])
# print(h2[0].shape)
# plt.plot(h2[0])
#
# plt.show()

