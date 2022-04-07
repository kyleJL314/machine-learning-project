from PIL import Image
import sys
import numpy as np
import os
def randomCrop(image,width,height):
    sizeX= image.size[0]
    sizeY= image.size[1]
    randX = np.random.randint(0,sizeX+1-width)
    randY = np.random.randint(0,sizeY+1-height)
    return image.crop((randX,randY,randX+width,randY+height))

def createRandomSamples(image,saveName,saveDirectory,amount,width,height):
   
    saveName = os.path.splitext(saveName)
    for i in range(amount):
        
        im_crop = randomCrop(image,width,height)
        savePath = saveDirectory+"/"+saveName[0]+"-"+str(i)+saveName[1]
        im_crop.save(savePath, quality=95)


if(len(sys.argv)<3):
    print("please type input folder and output folder")
    sys.exit()

try:     
    os.mkdir(sys.argv[2])
except OSError as error: 
    pass
images = os.listdir(sys.argv[1])


images.pop(0)
for i in images:
    image = Image.open(sys.argv[1]+'/'+i)
    createRandomSamples(image,i,sys.argv[2],10,300,300)
    
