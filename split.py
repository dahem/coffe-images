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
      print(box)
      img = im.crop(box)
      img.save(filename+'-'+str(j) + '-' + str(i)+'.jpg')
  
image("./images2/cafe 8.jpg")