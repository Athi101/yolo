import cv2, time
cap = cv2.VideoCapture("rtsp://username:pass@ip:port") 
time.sleep(2) 
while(True):
	ret, frame = cap.read()
	print (ret)
	if ret == 1:
		cv2.imshow('frame',frame)
	else:
		print ("no video")
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
