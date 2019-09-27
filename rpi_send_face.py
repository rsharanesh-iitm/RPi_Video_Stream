"""test_3_rpi_send_jpg.py -- send PiCamera jpg stream.

A Raspberry Pi test program that uses imagezmq to send image frames from the
PiCamera continuously to a receiving program on a Mac that will display the
images as a video stream. Images are converted to jpg format before sending.

This program requires that the image receiving program be running first. Brief
test instructions are in that program: test_3_mac_receive_jpg.py.
"""

# import imagezmq from parent directory

import socket
import time
import cv2
from imutils.video import VideoStream
import imagezmq

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# use either of the formats below to specifiy address of display computer
# sender = imagezmq.ImageSender(connect_to='tcp://jeff-macbook:5555')
sender = imagezmq.ImageSender()

rpi_name = 'It\'s Me'   # send RPi hostname with each image
picam = VideoStream(0).start()
time.sleep(2.0)  # allow camera sensor to warm up
jpeg_quality = 95  # 0 to 100, higher is better quality, 95 is cv2 default
while True:  # send images as stream until Ctrl-C
    image = picam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
    	cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    ret_code, jpg_buffer = cv2.imencode(
        ".jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality])
    sender.send_jpg(rpi_name, jpg_buffer)
