
"""
    PROJECT: CV Ball Tracking Game
    MADE BY: Mohd Ali Bin Naser
    Github : github.com/mohdalibn

"""

# Importing the required libraries for the project
import HSVColorDetector
import cv2

# Initializing the webcam input
CamVideo = cv2.VideoCapture(0)
# Setting the OpenCV Window Size
CamVideo.set(3, 640)
CamVideo.set(4, 480)

run = True  # Variable to control the while loop below

# Creating an object instance of the ColorDetector()
ColorDetector = HSVColorDetector.ColorDetector()
HSVColor = "red"
# HSVColor = {'HueMin': 147, 'SatMin': 37, 'ValMin': 58,
#             'HueMax': 179, 'SatMax': 255, 'ValMax': 255}

while run:

    success, frame = CamVideo.read()

    # This line calls the UpdateFrame Function that returns the Masked Image & Colored Image
    MaskedImage, ColoredImage = ColorDetector.UpdateFrame(frame, HSVColor)

    cv2.imshow("Ball Tracking Window", MaskedImage)

    # Stops the window if the 'q' button on the keyboard is pressed
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        run = False
        cv2.destroyAllWindows()
        break
