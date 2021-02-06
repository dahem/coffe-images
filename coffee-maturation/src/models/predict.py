# import the necessary packages
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

import src.models.sliding_window as slidewin

# load the trained convolutional neural network and the multi-label
# binarizer
print("[INFO] loading network...")
out_model = "././models/coffematuration.h5"
model = load_model(out_model)
path_labelbin = "././models/mlb.pickle"
mlb = pickle.loads(open(path_labelbin, "rb").read())
print(mlb.classes_)
# ['back' 'green' 'leaf' 'noise' 'purple' 'red' 'sky' 'yellow']

min_prob_0 = 0.3
min_prob_1 = 0.4
min_prob_2 = 0.7
min_prob_3 = 0.35
min_prob_4 = 0.2
min_prob_5 = 0.45
min_prob_6 = 0.2
min_prob_7 = 0.2



step = 70
path_img_val = "././data/raw/validation/cafe727.jpg"
filename = "cafe727"
# load the image
image = cv2.imread(path_img_val)
w, h = image.shape[0], image.shape[1]
print("IMAGE: ", path_img_val)
print(w, h)

img_copy = np.array(image, dtype='uint8')

rec_0 = []
rec_1 = []
rec_2 = []
rec_3 = []
rec_4 = []
rec_5 = []
rec_6 = []
rec_7 = []

try:    
    img_copy_0 = image.copy()
    img_copy_1 = image.copy()
    img_copy_2 = image.copy()
    img_copy_3 = image.copy()
    img_copy_4 = image.copy()
    img_copy_5 = image.copy()
    img_copy_6 = image.copy()
    img_copy_7 = image.copy()
    img_copy_8 = image.copy()
except:
    raise Exception("The following file ({}) is not an image!".format(img_color))

for (x, y, roi) in slidewin.sliding_window(img_copy, int(step), (w, h)):
    print(x, y)
    # print("roi shape: ", roi.shape)
    # if roi.shape[1] != w or roi.shape[0] != h:
    #         continue
    rxx, ryy, rxx2, ryy2 = int(x), int(y), int((x+w)), int((y+h))
    # coord.append([rx,ry,rx2,ry2,roi])

    if roi.shape == (step,step,3):
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        
        roi = np.expand_dims(roi, axis=0)

        
        classess = model.predict(roi)[0]
        # idxs = np.argsort(classess)[::-1][:2]
        print(classess)
        if (classess[0] > min_prob_0):
            rec_0.append([rxx, ryy, rxx2, ryy2, classess[0]])
        if (classess[1] > min_prob_1):
            rec_1.append([rxx, ryy, rxx2, ryy2, classess[1]])
        if (classess[2] > min_prob_2):
            rec_2.append([rxx, ryy, rxx2, ryy2, classess[2]])
        if (classess[3] > min_prob_3):
            rec_3.append([rxx, ryy, rxx2, ryy2, classess[3]])
        if (classess[4] > min_prob_4):
            rec_4.append([rxx, ryy, rxx2, ryy2, classess[4]])
        if (classess[5] > min_prob_5):
            rec_5.append([rxx, ryy, rxx2, ryy2, classess[5]])
        if (classess[6] > min_prob_6):
            rec_6.append([rxx, ryy, rxx2, ryy2, classess[6]])
        if (classess[7] > min_prob_7):
            rec_7.append([rxx, ryy, rxx2, ryy2, classess[7]])
    else:
        continue

windows_0 = np.array(rec_0)
windows_1 = np.array(rec_1)
windows_2 = np.array(rec_2)
windows_3 = np.array(rec_3)
windows_4 = np.array(rec_4)
windows_5 = np.array(rec_5)
windows_6 = np.array(rec_6)
windows_7 = np.array(rec_7)

save_path = "././data/processed"

for (x, y, x2, y2, prob) in windows_0:
    cv2.rectangle(img_copy_0, (int(x),int(y)), (int(x2),int(y2)), (0,0,0), 2)
    cv2.rectangle(img_copy_8, (int(x),int(y)), (int(x2),int(y2)), (0,0,0), 2)
sv = os.path.join(save_path,"negro")
os.makedirs(sv, exist_ok=True)
cv2.imwrite(sv + '/' + filename + '.jpg' ,img_copy_0)

for (x, y, x2, y2, prob) in windows_1:
    cv2.rectangle(img_copy_1, (int(x),int(y)), (int(x2),int(y2)), (0,255,0), 2)
    cv2.rectangle(img_copy_8, (int(x),int(y)), (int(x2),int(y2)), (0,255,0), 2)
sv = os.path.join(save_path, "verde")
os.makedirs(sv, exist_ok=True)
cv2.imwrite(sv + '/' + filename + ".jpg",img_copy_1)

for (x, y, x2, y2, prob) in windows_2:
    cv2.rectangle(img_copy_2, (int(x),int(y)), (int(x2),int(y2)), (0,100,0), 2)
    # cv2.rectangle(img_copy_8, (int(x),int(y)), (int(x2),int(y2)), (0,100,0), 2)
sv = os.path.join(save_path, "hoja")
os.makedirs(sv, exist_ok=True)
cv2.imwrite(sv + '/' + filename + ".jpg",img_copy_2)

for (x, y, x2, y2, prob) in windows_3:
    cv2.rectangle(img_copy_3, (int(x),int(y)), (int(x2),int(y2)), (19,69,139), 2)
    # cv2.rectangle(img_copy_8, (int(x),int(y)), (int(x2),int(y2)), (19,69,139), 2)
sv = os.path.join(save_path, "ruido")
os.makedirs(sv, exist_ok=True)
cv2.imwrite(sv +'/'+ filename + ".jpg",img_copy_3)

for (x, y, x2, y2, prob) in windows_4:
    cv2.rectangle(img_copy_4, (int(x),int(y)), (int(x2),int(y2)), (225,0,255), 2)
    cv2.rectangle(img_copy_8, (int(x),int(y)), (int(x2),int(y2)), (255,0,255), 2)
sv = os.path.join(save_path, "cereza")
os.makedirs(sv, exist_ok=True)
cv2.imwrite(sv+'/'+  filename + ".jpg",img_copy_4)

for (x, y, x2, y2, prob) in windows_5:
    cv2.rectangle(img_copy_5, (int(x),int(y)), (int(x2),int(y2)), (0,0,255), 2)
    cv2.rectangle(img_copy_8, (int(x),int(y)), (int(x2),int(y2)), (0,0,255), 2)
sv = os.path.join(save_path, "rojo")
os.makedirs(sv, exist_ok=True)
cv2.imwrite(sv + '/'+  filename + ".jpg",img_copy_5)

for (x, y, x2, y2, prob) in windows_6:
    cv2.rectangle(img_copy_6, (int(x),int(y)), (int(x2),int(y2)), (40,0,0), 2)
    # cv2.rectangle(img_copy_8, (int(x),int(y)), (int(x2),int(y2)), (40,0,0), 2)
sv = os.path.join(save_path, "cielo")
os.makedirs(sv, exist_ok=True)
cv2.imwrite(sv + '/'+  filename + ".jpg", img_copy_6)

for (x, y, x2, y2, prob) in windows_7:
    cv2.rectangle(img_copy_7, (int(x),int(y)), (int(x2),int(y2)), (0,255,255), 2)
    cv2.rectangle(img_copy_8, (int(x),int(y)), (int(x2),int(y2)), (0,255,255), 2)
sv = os.path.join(save_path, "amarillo")
os.makedirs(sv, exist_ok=True)
cv2.imwrite(sv + '/'+  filename + ".jpg", img_copy_7)

sv = os.path.join(save_path, "grano")
os.makedirs(sv, exist_ok=True)
cv2.imwrite(sv + '/'+  filename + ".jpg",img_copy_8)