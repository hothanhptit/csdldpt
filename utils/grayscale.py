from PIL import Image
import os
def grayScale(path, savePath):
    imgName = os.path.basename(path).split('.')[0]
    dir = f'{savePath}'
    isExist = os.path.exists(dir)
    if not isExist:
        os.makedirs(dir)
        print("The new directory is created!")
    os.chdir(dir)
    img = Image.open(path).convert('L')
    img.save(f'{dir}/{imgName}_gray.jpg')