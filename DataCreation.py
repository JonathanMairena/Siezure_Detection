#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:47:40 2020
@author: jonathanmairena

Creates Training Labels:
    Random action labels 0 or1 

Creates Training Videos:
    
    Reduce Video Quality on terminal

    Split Video on Terminal

    Make Split Videos Extracts Frames from Split Videos into their own directory
"""


## TRAIN ACTIONS
#30 fps 
# 
import numpy as np
import pickle
num_data = 44
actions = np.empty([num_data,1])

for i in range(0,num_data):
    if i <= 3 and i >=0 :
        actions[i] = 0
    else:
        actions[i] = 1

        
with open('action_labels_moving.pkl','wb') as f:
    pickle.dump(actions, f)

#Reduce quality from 1080 to 340 for faster run time need the video in your cwd

'''ffmpeg -i input.avi -s 320x240 -b:v 16k -b:a 8k output.avi'''

#Split Videos using ffmpeg

#Go to directory you want with video and ffmpeg-split.py                   
#-example splits videos into 200 equal frame size chuncks
'''python ffmpeg-split.py -f bigvideo.avi -c 200'''             

# Make more train video files Format 1 file per 28 frames with frames extraced entire directory gets thrown into 3dcnn

from os import listdir
import os
from os.path import isfile, join
import cv2
import numpy as np
mypath = '/Users/jonathanmairena/Documents/Spring2020/LabNotebook/TrackingPhase2/video-classification-master/ResNetCRNN/Data_Creation/Video_Data_Moving'

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
vids = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  vids[n] = cv2.VideoCapture( join(mypath,onlyfiles[n]) , 0)
 
# Make all the files in a directory
# Opens the Video file 
j = 0
path = os.getcwd()
for vid in vids:
    i = 0
    name = str(j) + ' Video'
    os.mkdir(name,mode=0o777,dir_fd=None)
    os.chdir(name)
    while(vid.isOpened()):
        ret, frame = vid.read()
        if ret == False:
            break
        cv2.imwrite(str(i)+'.jpg',frame)
        i += 1
        
    os.chdir(path)
    j += 1
    
    
    vid.release()
    cv2.destroyAllWindows()
    
    
    
  