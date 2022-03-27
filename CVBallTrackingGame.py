
"""
    PROJECT: CV Ball Tracking Game
    MADE BY: Mohd Ali Bin Naser
    Github : github.com/mohdalibn

"""

# Importing the required libraries for the project
import HSVColorDetector
import cv2


# A function that's going to return the ball contours
def GetBallContours(frame, findFrame, minArea=1000, sort=True, filter=0, DrawContour=True, c=(255, 0, 0)):

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
                    cv2.DrawContourtours(ImageContours, contour, -1, c, 3)
                x, y, w, h = cv2.boundingRect(approx)
                cx, cy = x + (w // 2), y + (h // 2)
                cv2.rectangle(ImageContours, (x, y), (x + w, y + h), c, 2)
                cv2.circle(ImageContours, (x + (w // 2),
                           y + (h // 2)), 5, c, cv2.FILLED)
                ContoursFound.append({"contour": contour, "area": area, "bbox": [
                                     x, y, w, h], "center": [cx, cy]})

    # Executes if the sorted flag is true
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
