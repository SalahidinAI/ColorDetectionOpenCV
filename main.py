# Original video and code:
# https://www.youtube.com/watch?v=aFNDh5k3SjU&list=PLb49csYFtO2HAdNGChGzohFJGnJnXBOqd&index=4
# https://github.com/computervisioneng/color-detection-opencv/blob/master/requirements.txt

# If you have issues with dependencies then do next
# pip install --upgrade pip setuptools wheel
# pip install --upgrade -r req.txt
# pip install -r req.txt

from util import get_limits
from PIL import Image
import cv2

yellow = [0, 255, 255]  # yellow in BGR colorspace
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()
    # print(bbox)
    # bbox returns 4 values:
    # a – distance from screen’s right edge to object’s right edge
    # b – distance from top of screen to top of object
    # c – distance from screen’s right edge to object’s left edge
    # d – distance from top of screen to bottom of object
    # (a, b, c, d) = (489, 676, 879, 720)

    if bbox:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)  # you can try mask instead frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
