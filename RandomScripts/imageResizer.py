"""
Created by: Alex J. Gatz
Date: 1/8/2019
"""
import sys 
import cv2
import os

width = int(1920/2)
height = int(1080/2)
dim = (width, height)

def resizeImages(folder):
    for filename in os.listdir(folder):
        print(filename)
        img = cv2.imread(os.path.join(folder,filename))
        print('Original Dimensions : ',img.shape)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        print('Resized Dimensions : ',resized.shape)
        resizedFileName = f'{filename}_resized.jpg'
        cv2.imwrite(resizedFileName, resized)
        print(resizedFileName)

def main():
    path = "/home/neo/Code/PythonStuff/PythonFor100Days/testImages"
    resizeImages(path)

if __name__ == "__main__":
    main()
