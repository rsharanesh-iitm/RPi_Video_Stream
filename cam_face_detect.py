import cv2,sys
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
while True:
	ret,frm = cap.read()
	# Convert to grayscale
    	gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
    	# Detect the faces
    	faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    	# Draw the rectangle around each face
    	for (x, y, w, h) in faces:
        	cv2.rectangle(frm, (x, y), (x+w, y+h), (255, 0, 0), 2)
	sys.stdout.write( frm.tostring() )
