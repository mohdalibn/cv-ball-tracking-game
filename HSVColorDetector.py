
# Importing the Required Libraries to use this custom library
import numpy as np
import logging
import cv2


# Class that contains all the relevant methods to use this file in other projects
class ColorDetector:
    def __init__(self, ColorControls=False):
        self.ColorControls = ColorControls

        if self.ColorControls:
            self.OpenControls()

    # This function will the color controls window
    def OpenControls(self):

        cv2.namedWindow("Color Controls")
        cv2.resizeWindow("Color Controls", 640, 250)
        cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, self.empty)
        cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, self.empty)
        cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, self.empty)
        cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, self.empty)
        cv2.createTrackbar("Val Min", "TrackBars", 0, 255, self.empty)
        cv2.createTrackbar("Val Max", "TrackBars", 255, 255, self.empty)
