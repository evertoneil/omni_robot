#!/usr/bin/env python

import rospy
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
from omni_cam.msg import object
from omni_cam.msg import jarak
import numpy as np
import imutils
import cv2
#=========================Variable==========
x = 0
y = 15
distance = 0
#=====================STREAM VIDEO JETSON NANO=================================
# gstreamer_pipeline returns a GStreamer pipeline for capturing from the CSI camera
# Defaults to 1280x720 @ 30fps
# Flip the image by setting the flip_method (most common values: 0 and 2)
# display_width and display_height determine the size of the window on the screen

def gstreamer_pipeline(
    capture_width=3240,
    capture_height=2464,
    display_width=820,
    display_height=616,
    framerate=15,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )
#==============================================================================
#========================Calculate midpoints from a line=======================
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
#===========================================================================
#>>>>>>>>>>>>>>>>>>>>MAIN PROGRAM>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#==================================================================
def face_detect():
    global distance
    pub = rospy.Publisher('camera',object,queue_size=10)
    cap = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)
    if cap.isOpened():
        cv2.namedWindow("Object Detect", cv2.WINDOW_AUTOSIZE)
        while cv2.getWindowProperty("Object Detect", 0) >= 0:
	    ret, img = cap.read()					#Open Stream Video
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)		#Convert to BW and Blur
	    gray = cv2.GaussianBlur(gray, (7, 7), 0)

            # perform edge detection, then perform a dilation + erosion to close gaps in between object edges
	    edged = cv2.Canny(gray, 50, 110)
	    edged = cv2.dilate(edged, None, iterations=1)
	    edged = cv2.erode(edged, None, iterations=1)

	    # find contours in the edge map
	    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
		   cv2.CHAIN_APPROX_SIMPLE)	
	    cnts = imutils.grab_contours(cnts)
	    #================================================
	    pixelsPerMetric = None
	    orig = img.copy()
	    # loop over the contours individually
	    for c in cnts:
            # compute the rotated bounding box of the contour
		if cv2.contourArea(c) < 1800:				#Filter small-sized object
			continue
	    #===========================================================================
		box = cv2.minAreaRect(c)
		box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
		box = np.array(box, dtype="int")
		box = perspective.order_points(box)
	    	cv2.drawContours(orig,[box.astype("int")], -1, (0, 255, 0), 2)
	        for (x, y) in box:
            		cv2.circle(img, (int(x), int(y)), 3, (0,0,255), -1)
		(tl, tr, br, bl) = box
		(tltrX, tltrY) = midpoint(tl, tr)
		(blbrX, blbrY) = midpoint(bl, br)
		# compute the midpoint between the top-left and top-right points,
		# followed by the midpoint between the top-righ and bottom-right
		(tlblX, tlblY) = midpoint(tl, bl)
		(trbrX, trbrY) = midpoint(tr, br)
		#============================================================
		#======== draw the midpoints on the image====================
		cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
		cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
		cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
		cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
		cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
			(255, 0, 255), 2)
		cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
			(255, 0, 255), 2)
		#============================================================
		#==== compute the Euclidean distance between the midpoints===
		dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
		dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

		# compute it as the ratio of pixels to supplied metric
		if pixelsPerMetric is None:				#Calculate Size
			resolution = 661.84* pow(distance,-1.002)	#Based on Calibration Data

		# compute the size of the object
		dimA = dA / resolution
		dimB = dB / resolution
 	    	#=============Send the value through rostopic==============
		size = object()
 	    	size.width = dimB
	    	size.height = dimA
		pub.publish(size)
		#============================================================
		#=========Display the object sizes on the image(optional)====
		cv2.putText(orig, "{:.1f}cm".format(dimA),
			(int(tltrX), int(tltrY)), cv2.FONT_HERSHEY_SIMPLEX,
				0.7, (255, 255, 255), 2)
		cv2.putText(orig, "{:.1f}cm".format(dimB),
			(int(trbrX), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
			0.7, (255, 255, 255), 2)
		#============================================================
	    cv2.imshow("Object Detect" ,orig)
            keyCode = cv2.waitKey(30) & 0xFF
            # Stop the program on the ESC key
            if keyCode == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Unable to open camera")

def callback (data):		#Receive Distance data from IR Sensor
    global distance
    distance = data.cm

def talker():
    rospy.init_node('jetson', anonymous=True)
    while not rospy.is_shutdown():
 	face_detect()

if __name__ == '__main__':
    try:
        rospy.Subscriber('distance',jarak, callback)
	talker()
    except rospy.ROSInterruptException:
        pass
