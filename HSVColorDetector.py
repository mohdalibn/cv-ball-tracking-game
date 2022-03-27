
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

    # This method will the color controls window
    def OpenControls(self):

        cv2.namedWindow("Color Controls")
        cv2.resizeWindow("Color Controls", 640, 250)

        # The following 6 lines will create 6 trackbars that will allow the user to control
        cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, self.empty)
        cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, self.empty)
        cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, self.empty)
        cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, self.empty)
        cv2.createTrackbar("Val Min", "TrackBars", 0, 255, self.empty)
        cv2.createTrackbar("Val Max", "TrackBars", 255, 255, self.empty)

    # This method will
    def GetColorControlVals(self):
        HueMin = cv2.getTrackbarPos("Hue Min", "TrackBars")
        SatMin = cv2.getTrackbarPos("Sat Min", "TrackBars")
        ValMin = cv2.getTrackbarPos("Val Min", "TrackBars")
        HueMax = cv2.getTrackbarPos("Hue Max", "TrackBars")
        SatMax = cv2.getTrackbarPos("Sat Max", "TrackBars")
        ValMax = cv2.getTrackbarPos("Val Max", "TrackBars")

        HSVValues = {"HueMin": HueMin, "SatMin": SatMin, "ValMin": ValMin,
                     "HueMax": HueMax, "SatMax": SatMax, "ValMax": ValMax}

        # this line will print all the values above onto the terminal at runtime
        print(HSVValues)

        # This will return the the values
        return HSVValues
