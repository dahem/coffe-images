def sliding_window(image, stepSize, windowSize):
	# print("\n image:"+ str(image))
	print("\n step:"+ str(stepSize))
	for y in range(0, image.shape[0], stepSize):
		for x in range(0, image.shape[1], stepSize):
			print(y, x, "image[", y, y + windowSize[1], x, x + windowSize[0],"]")
            # yield (y, x, image[y:y + windowSize[1], x:x + windowSize[0]])
            