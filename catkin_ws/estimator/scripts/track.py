import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Read Template file	
ok, frame = cap.read()

bbox = cv2.selectROI(frame, False)
#cv2.imshow('frame',frame)


tracker = cv2.TrackerMIL_create()




while(True):
    # Capture frame-by-frame
    ok, frame = cap.read()
    if not ok:
		print('video capture can not be opened')
		break
	# Start timer
    timer = cv2.getTickCount()
    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)
    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    # Draw bounding box
    # Tracking success
    retval, boundingBox	=	tracker.update(	frame	)
    
    cv2.rectangle(frame, boundingBox, (255,0,0), 2, 1)
	# Display tracker type on frame
    cv2.putText(frame, "MIL Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
    # Display result
    cv2.imshow("Tracking", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
