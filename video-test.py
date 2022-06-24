from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv


# initialise the camera
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow camera to warm up
time.sleep(0.1)

#use continuous capture to access raw video feed
for frame in camera.capture_continuous(
    rawCapture, 
    format="bgr", 
    use_video_port=True
    ):

    image=frame.array

    # apply a colourmask
    mask = cv.inRange(image, (50,0,0),(255,150,150))

    #display live mask
    cv.imshow("Frame", mask)
    key = cv.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        break

