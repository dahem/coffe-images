def sliding_window(image, stepSize, windowSize):
	# print("\n image:"+ str(image))
	print("\n step:"+ str(stepSize))
	for x in range(0, image.shape[0], stepSize):
		for y in range(0, image.shape[1], stepSize):
			yield (x, y, image[x:x + stepSize, y:y + stepSize])
            # print(y, x, "image[", y, y + stepSize, x, x + stepSize,"]")
            