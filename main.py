import grayscale
import gaussFilter

def main():
    grayscale.grayScale('./venv/Images/img/2.jpg', './venv/Images/img/2_gray.jpg')
    gaussFilter('./venv/Images/img/2.jpg','./venv/Images/img/2_gauss.jpg')