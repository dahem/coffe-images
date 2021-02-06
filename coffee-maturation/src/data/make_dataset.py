from imutils import paths
#import argparse
import random
import numpy as np
import cv2
import os
import pickle
from tensorflow.keras.preprocessing.image import img_to_array
from sklearn.preprocessing import MultiLabelBinarizer

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-d", "--dataset", required=True,
#	help="path to input dataset (i.e., directory of images)")
#ap.add_argument("-m", "--model", required=True,
#	help="path to output model")
#ap.add_argument("-l", "--labelbin", required=True,
#	help="path to output label binarizer")
#ap.add_argument("-p", "--plot", type=str, default="plot.png",
#	help="path to output accuracy/loss plot")
#args = vars(ap.parse_args())

def create_dataset():
	"""
	This function returns a tuple X, y
	"""
	
	# initialize the number of epochs to train for, initial learning rate,
	# batch size, and image dimensions
	IMAGE_DIMS = (70, 70, 3)
	
	# grab the image paths and randomly shuffle them
	print("[INFO] loading images...")
	path_input = "././data/raw/train/"
	imagePaths = sorted(list(paths.list_images(path_input)))
	random.seed(42)
	random.shuffle(imagePaths)
	
	# initialize the data and labels
	X = []
	labels = []
	
	# loop over the input images
	for imagePath in imagePaths:
		# load the image, pre-process it, and store it in the data list
		image = cv2.imread(imagePath)
		image = cv2.resize(image, (IMAGE_DIMS[1], IMAGE_DIMS[0]))
		image = img_to_array(image)
		X.append(image)
		# extract set of class labels from the image path and update the
		# labels list
		l = imagePath.split(os.path.sep)[-2].split("-")
		l = tuple(l)
		labels.append(l)
		
	X = np.array(X, dtype='float') / 255.0
	labels = np.array(labels)
	print(labels[5:15])

	mlb = MultiLabelBinarizer()
	mlb.fit(labels)
	y = mlb.transform(labels)
	print(y[5:15])
	
	# save the multi-label binarizer to disk
	print("[INFO] serializing label binarizer...")
	path_output = "././models/"
	f = open(path_output + "mlb.pickle", "wb")
	f.write(pickle.dumps(mlb))
	f.close()
	
	return X, y
