from time import time
from SimpleCV import Camera, Image, Color, Display
import numpy as np
import cv2


class MyCamera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    lastTime = 0
    def __init__(self):
        self.usbCam = cv2.VideoCapture(0)
    self.usbCam.set(3,400)
    self.usbCam.set(4,300)
    ret, frame = self.usbCam.read()
    self.cache = cv2.imencode('.jpg',frame)[1].tostring()
    #self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    def get_frame(self):
    diff = time()*1000 - self.lastTime;
    #if diff<30 and self.cache!=None:
    #   return self.cache
    ret, frame = self.usbCam.read()
    self.cache = cv2.imencode('.jpg',frame)[1].tostring()
    self.lastTime = time()*1000
    return self.cache
    