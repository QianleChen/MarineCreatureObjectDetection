'''
Explanation :

In cv2.VideoCapture(‘video.mp4’), we just have to mention the video name with it’s extension.
Here my video name is “video.mp4”. You can set frame rate which is widely known as fps (frames per second).
Here I set 0.5 so it will capture a frame at every 0.5 seconds, means 2 frames (images) for each second.

It will save images with name as image1.jpg, image2.jpg and so on.
'''

import cv2
import os
vidcap = cv2.VideoCapture('1min.mp4')
#path = 'SlicedPicture/1minJellyFish'
path = 'data/images/val'
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(os.path.join(path, "image"+str(count)+".jpg"), image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.1 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
    print(success, ' create frame at ', sec, '; Total Frame Count: ', count)