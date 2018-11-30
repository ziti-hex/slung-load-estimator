import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,640)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
	#cv2.boundingRect()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    newframe = frame[270:370,270:370]
    
    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('frame1',newframe)
    if cv2.waitKey(1) & 0xFF == ord('t'):
			filename = "pos0.jpg" 
			cv2.imwrite(filename,newframe)
			break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
