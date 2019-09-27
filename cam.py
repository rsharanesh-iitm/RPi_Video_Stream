import cv2,sys
cap = cv2.VideoCapture(0)
while True:
	ret,frm = cap.read()
	sys.stdout.write( frm.tostring() )