'''
from ultralytics import YOLO

model = YOLO('yolov8m.pt')
results = model('1min.mp4', save=True)
'''

from ultralytics import YOLO
import cv2
import os
from os import listdir

vidcap = cv2.VideoCapture('1min.mp4')
# path = 'SlicedPicture/1minJellyFish'
path = 'data/images/val'


count = 1
path = 'data/images/valTooBig'
modelPath = 'runs/detect/train2/weights'
folderDir = 'data/images/valTooBig'

modelPath = os.path.join(modelPath, "last" + ".pt")
model = YOLO(modelPath)

# Not using images attribute, no in order for some reason.
# Only needs to know total number of images in folder
# Algo can be improved, wasting too much resource
for images in os.listdir(folderDir):
    ImageFormatPath = os.path.join(path, "image" + str(count) + ".jpg")
    results = model(ImageFormatPath, save=True)
    count += 1

