import numpy as np
import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while(cap.isOpened()):
# Capture frame-by-frame
	ret, frame = cap.read()
# Our operations on the frame come here
	if ret == True:
		frame = cv2.flip(frame,1)
		font = cv2.FONT_HERSHEY_SIMPLEX
		faces = face_cascade.detectMultiScale(frame, 1.1, 5, minSize=(10, 10))
		for (x, y, w, h) in faces:
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(frame,'1991',(x,y), font, 4,(255,0,0),2,cv2.LINE_AA)
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
		

		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break	
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
