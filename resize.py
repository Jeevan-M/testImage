import os
from PIL import Image
import math
imagePath = [os.path.join("./",f) for f in os.listdir("./")]

for index, path in enumerate(imagePath):
    if(".jpg" in path):
        image = Image.open(path)
        x, y = image.size
        x1, y1 = math.floor(x/2), math.floor(y/2)
        newImg = image.resize((x1,y1),Image.ANTIALIAS )
        newImg.save("converted/"+path.split("/")[1],optimize=True)
        print(index,image.size,newImg.size)