import cv2 as cv2
img = './venv/Images/image1.jpg'
mask = cv2.imread(img,0)
res = cv2.bitwise_nd(img,img,mask = mask)