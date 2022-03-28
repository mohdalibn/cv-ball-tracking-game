
"""
    PROJECT: CV Ball Tracking Game
    MADE BY: Mohd Ali Bin Naser
    Github : github.com/mohdalibn

"""

# Importing the required libraries for the project
import HSVColorDetector
import cv2
import socket

# A function that's going to return the ball contours


def GetBallContours(frame, findFrame, minArea=1000, sort=True, filter=0, DrawContour=True, c=(0, 255, 0)):

    ContoursFound = []
    ImageContours = frame.copy()
    contours, _ = cv2.findContours(
        findFrame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > minArea:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

            if len(approx) == filter or filter == 0:
                if DrawContour:
                    cv2.drawContours(ImageContours, contour, -1, c, 3)
                x, y, w, h = cv2.boundingRect(approx)
                cx, cy = x + (w // 2), y + (h // 2)
                cv2.rectangle(ImageContours, (x, y), (x + w, y + h), c, 2)
                cv2.circle(ImageContours, (x + (w // 2),
                           y + (h // 2)), 5, c, cv2.FILLED)
                ContoursFound.append({"contour": contour, "area": area, "bbox": [
                                     x, y, w, h], "center": [cx, cy]})

    # Executes if the sorted flag is true. The Sorting occurs in decending order
    if sort:
        ContoursFound = sorted(
            ContoursFound, key=lambda x: x["area"], reverse=True)

    # Returning the lists created above
    return ImageContours, ContoursFound


# Initializing the webcam input
CamVideo = cv2.VideoCapture(0)
# Setting the OpenCV Window Size
CamVideo.set(3, 640)
CamVideo.set(4, 480)

# Reading in the first frame to get the Image Width & Height
success, frame = CamVideo.read()
FrameWidth, FrameHeight, _ = frame.shape

run = True  # Variable to control the while loop below

# Creating an object instance of the ColorDetector()
ColorDetector = HSVColorDetector.ColorDetector()
HSVColor = "red"
# HSVColor = {'HueMin': 147, 'SatMin': 37, 'ValMin': 58,
#             'HueMax': 179, 'SatMax': 255, 'ValMax': 255}


# Using the sockets module, we'll send the contour data to Unity using the UDP Protocol(socket.SOCK_DGRAM)
GameSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ServerIPAddressPort = ("127.0.0.1", 2001)


while run:

    success, frame = CamVideo.read()

    # This line calls the UpdateFrame Function that returns the Masked Image & Colored Image
    MaskedImage, ColoredImage = ColorDetector.UpdateFrame(frame, HSVColor)

    ImageContours, ContoursFound = GetBallContours(frame, MaskedImage)

    # This executes if there are contours available
    if ContoursFound:

        """

            This variable stores the Center X & Y, and the Area of the Contour Respectively
            Because OpenCV uses a different convention for coordinates, we will have to subtract the Center Y from the FrameHeight. Doing this will match the convention of Unity which will require this data in the game.

         """
        ContourData = ContoursFound[0]['center'][0], FrameHeight - ContoursFound[0]['center'][1], int(
            ContoursFound[0]['area'])

        # Filtering the data & before sending it to Unity
        ContourData = str(ContourData)
        ContourData = str.encode(ContourData)
        GameSocket.sendto(ContourData, ServerIPAddressPort)

    cv2.imshow("Ball Tracking Window", ImageContours)

    # Stops the window if the 'q' button on the keyboard is pressed
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        run = False
        cv2.destroyAllWindows()
        break
