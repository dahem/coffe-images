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

step = 70
path_img_val = "././data/raw/validation/cafe700.jpg"
# load the image
image = cv2.imread(path_img_val)
w, h = image.shape[0], image.shape[1]
print("IMAGE: ", path_img_val)
print(w, h)

img_copy = np.array(image, dtype='uint8')

coord = []

for (x, y, roi) in slidewin.sliding_window(img_copy, int(step), (w, h)):
    print(x, y)
    # print("roi shape: ", roi.shape)
    # if roi.shape[1] != w or roi.shape[0] != h:
    #         continue
    rx, ry, rx2, ry2 = int(x), int(y), int((x+w)), int((y+h))
    # coord.append([rx,ry,rx2,ry2,roi])

    if roi.shape == (step,step,3):
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        
        roi = np.expand_dims(roi, axis=0)

        
        classes_prob = model.predict(roi)[0]
        # idxs = np.argsort(classes_prob)[::-1][:2]
        print(classes_prob)
    else:
        continue

    