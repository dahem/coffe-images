# Improting Image class from PIL module 
from PIL import Image
import os
  

def image(path):
  imgheight = 70
  imgwidth = 70
  name = os.path.basename(path)
  filename = './croped/'+name.split('.')[0]
  print(filename) 
  im = Image.open(path)
  
  width, height = im.size 
  for i in range(height//imgheight):
    for j in range(width//imgwidth):
      box = (j*imgwidth, i*imgheight, (j+1)*imgwidth, (i+1)*imgheight)
      img = im.crop(box)
      img.save(filename+'-'+str(j) + '-' + str(i)+'.jpg')

from os import listdir
from os.path import isfile, join

mypath = './to-crop'

# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(onlyfiles)
# errors = []
# for x in onlyfiles:
#   try:
#     image(mypath + '/' + x)
#   except:
#     errors.append(x)
# print(errors)
# image("./to-crop/cafe 2.jpg")

cropedpath = './croped2'

cropfiles =  [f for f in listdir(cropedpath) if isfile(join(cropedpath, f))]
print(cropfiles)