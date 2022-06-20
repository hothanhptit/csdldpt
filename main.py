import grayscale
import gaussFilter
import reason_growing

def main():
    grayscale.grayScale('./venv/Images/img/2.jpg', './venv/Images/img/2_gray.jpg')
    # gaussFilter('./venv/Images/img/2.jpg','./venv/Images/img/2_gauss.jpg')
    reason_growing.regionGrow('./venv/Images/img/2.jpg', 1, 256)

