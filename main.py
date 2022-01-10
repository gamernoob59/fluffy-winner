import cv2
import numpy as np
import time


bg = cv2.imread('bg.png') 
frame = cv2.VideoCapture('Countdown Timer.mov')

bg= cv2.resize(bg, (640,480))
frame= cv2.resize(frame, (640,480))
