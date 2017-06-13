import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def QuadMirror(img):
	part4 = ScaleOneFourth(img)
	part2 = cv2.flip(part4,0)
	part1 = cv2.flip(part2,1)
	part3 = cv2.flip(part1,0)
	img[0:rows/2,0:cols/2] = part1
	img[0:rows/2,cols/2:cols] = part2
	img[rows/2:rows,0:cols/2] = part3
	img[rows/2:rows,cols/2:cols] = part4
	return img

def LeftMirror(img):
	rows,cols = img.shape[:2]
	if rows%2 == 1:
		rows = rows-1
	if cols%2 == 1:
		cols = cols-1
	img[0:rows,(cols/2):cols] = cv2.flip(img[0:rows,0:(cols/2)],1)
	return img

def RightMirror(img):
	rows,cols = img.shape[:2]
	if rows%2 == 1:
		rows = rows-1
	if cols%2 == 1:
		cols = cols-1
	img[0:rows,0:(cols/2)] = cv2.flip(img[0:rows,(cols/2):cols],1)
	return img

def TopMirror(img):
	rows,cols = img.shape[:2]
	if rows%2 == 1:
		rows = rows-1
	if cols%2 == 1:
		cols = cols-1
	img[rows/2:rows,0:cols] = cv2.flip(img[0:rows/2,0:cols],0)
	return img

def BottomMirror(img):
	rows,cols = img.shape[:2]
	if rows%2 == 1:
		rows = rows-1
	if cols%2 == 1:
		cols = cols-1
	img[0:rows/2,0:cols]= cv2.flip(img[rows/2:rows,0:cols],0)
	return img

def ScaleOneFourth(img):
	return cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)

def Negative(img):
	return 255-img

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame_scaled = cv2.flip(cv2.resize(frame,None,fx=1.4,fy=1.4,interpolation=cv2.INTER_LINEAR),1)
    rows,cols = frame_scaled.shape[:2]
    #Effects
    #Quad Mirror
    #part4 = ScaleOneFourth(frame_scaled)
    #part2 = cv2.flip(part4,0)
    #part1 = cv2.flip(part2,1)
    #part3 = cv2.flip(part1,0)
    #frame_scaled[0:rows/2,0:cols/2] = part1
    #frame_scaled[0:rows/2,cols/2:cols] = part2
    #frame_scaled[rows/2:rows,0:cols/2] = part3
    #frame_scaled[rows/2:rows,cols/2:cols] = part4

    cv2.imshow('frame',QuadMirror(frame_scaled))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
