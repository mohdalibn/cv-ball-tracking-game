
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

    # This method will get all the control values from the trackbars
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

    # This method will get HSV Values of the color that's passed as an argument to this function
    def GetColorHSVVals(self, Color):

        if Color.lower() == 'red':
            OutputHSV = {'HueMin': 146, 'SatMin': 141, 'ValMin': 77,
                         'HueMax': 179, 'SatMax': 255, 'ValMax': 255}
        elif Color.lower() == 'green':
            OutputHSV = {'HueMin': 44, 'SatMin': 79, 'ValMin': 111,
                         'HueMax': 79, 'SatMax': 255, 'ValMax': 255}
        elif Color.lower() == 'blue':
            OutputHSV = {'HueMin': 103, 'SatMin': 68, 'ValMin': 130,
                         'HueMax': 128, 'SatMax': 255, 'ValMax': 255}
        else:
            # Setting the OutputHSV to None if the argument color is not present above
            OutputHSV = None
            logging.warning("Color Not Defined")
            logging.warning("Available colors: red, green, blue ")

        # Returning the resulting HSV values
        return OutputHSV

    # This method updates the Image frame according to the HSV Color Value that's passed as a parameter to this function
    def UpdateFrame(self, frame, Color=None):

        # Variable to store the Masked Image and the Color Detected Image
        MaskedImage = []  # The Masked Image will highlight the detected color in white
        ColoredImage = []  # The Colored Image will only show the major detected color

        # If the Color Control Trackbars flag is set to true, this statement executes
        if self.ColorControls:
            Color = self.GetColorControlVals()

        # This statement executes if only the name of the color is specified as the Color parameter to this function
        if isinstance(Color, str):
            Color = self.GetColorHSVVals(Color)

        # If the passed Color argument is not none nor a string, this block of code is executed
        if Color is not None:
            ImageHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            LowerHSVVals = np.array(
                [Color['HueMin'], Color['SatMin'], Color['ValMin']])
            UpperHSVVals = np.array(
                [Color['HueMax'], Color['SatMax'], Color['ValMax']])
            MaskedImage = cv2.inRange(ImageHSV, LowerHSVVals, UpperHSVVals)
            ColoredImage = cv2.bitwise_and(frame, frame, mask=MaskedImage)

        # Return the Masked & Colored Images
        return MaskedImage, ColoredImage
