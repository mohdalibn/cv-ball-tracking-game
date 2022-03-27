
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
