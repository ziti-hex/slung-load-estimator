import numpy as np
import cv2

cap = cv2.VideoCapture(0)
def detect():
	# Read Template file	
    template = cv2.imread('/home/tobi/myfiles/pos/pos0.jpg',cv2.IMREAD_COLOR)
    # Search for template in farame 
    res = cv2.matchTemplate(frame,template, cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc=cv2.minMaxLoc(res)
    top_left=max_loc
    bottom_right =(top_left[0] + 100, top_left[1] + 100)
    cv2.rectangle(frame, top_left, bottom_right, 255, 2)
    top,left = top_left
    bottom, right = bottom_right
    bbox = top, left, 100, 100
    return bbox
    #cv2.imshow('frame',frame)

tracker = cv2.TrackerMIL_create()

ok, frame = cap.read()

bbox=detect()

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
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else :
		bbox=detect()
	# Display tracker type on frame
    cv2.putText(frame, "MIL Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
    # Display result
    cv2.imshow("Tracking", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
