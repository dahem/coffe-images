import os.path
from os import path
import json
from shutil import copyfile
f = open('taggeimages.json',) 
data = json.load(f) 
# cropfiles =  [f for f in listdir(cropedpath) if isfile(join(cropedpath, f))]
# print(data)
def make_dir(item):
  folder = 'to_train/'
  keys = []
  for key in item:
    if item[key] == True:
      keys.append(key)
  path_imgs = '-'.join(keys)
  if not path.exists(folder+path_imgs):
     os.mkdir(folder+path_imgs)
  return folder+path_imgs + '/'

for item in data:
  dirpath = make_dir(item)
  pre_path = './croped/' + item['name']
  print(pre_path, dirpath + item['name'])
  copyfile(pre_path, dirpath + item['name'])


