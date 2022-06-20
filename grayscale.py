from PIL import Image
def grayScale(fromPath, savePath):
    img = Image.open(fromPath).convert('L')
    img.save(savePath)