import cv2
import glob

inputFolder = "dataCardImages"
outputFolder = "dataCardEdges"

for filepath in glob.iglob(inputFolder+'/*.png'):
	img = cv2.imread(filepath,0)
	edges = cv2.Canny(img,100,200)

	#print(filepath)
	outputFile = filepath.replace(inputFolder, outputFolder)
	#print(outputFile)
	cv2.imwrite(outputFile, edges)