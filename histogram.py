import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

# read image
image = cv2.imread('./venv/Images/img/1.jpg')
# # calculate mean value from RGB channels and flatten to 1D array
# vals = im.mean(axis=2).flatten()
# # calculate histogram
# counts, bins = np.histogram(vals, range(255))
# # plot histogram centered on values 0..255
# plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
# plt.xlim([-0.5, 255.5])
# # print (bin)
# print (counts[0])
# print (counts)
# plt.show()

# colors = ("red", "green", "blue", "orange", "yellow", "purple")
# channel_ids = (0, 1, 2, 3, 4, 5)
colors = ("red", "green", "blue")
channel_ids = (0, 1, 2)

# create the histogram plot, with three lines, one for
# each color
plt.figure()
plt.xlim([0, 256])
for channel_id, c in zip(channel_ids, colors):
    histogram, bin_edges = np.histogram(
        image[:, :, channel_id], bins=256, range=(0, 256)
    )
    plt.plot(bin_edges[0:-1], histogram, color=c)
    print (histogram)
    # plt.xlim([-0.5, 255.5])

plt.title("Color Histogram")
plt.xlabel("Color value")
plt.ylabel("Pixel count")


plt.show()
