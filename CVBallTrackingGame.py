
"""
    PROJECT: CV Ball Tracking Game
    MADE BY: Mohd Ali Bin Naser
    Github : github.com/mohdalibn

"""

# Importing the required libraries for the project
from HSVColorDetector import ColorDetector
import cv2

# Initializing the webcam input
CamVideo = cv2.VideoCapture(0)
# Setting the OpenCV Window Size
CamVideo.set(3, 640)
CamVideo.set(4, 480)
