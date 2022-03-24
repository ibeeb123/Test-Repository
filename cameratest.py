import cv2

def main():
	
	camera = cv2.VideoCapture(0)
	camera.set(3,320)
	camera.set(4,240)
	
	
	while(1):
		_, frame = camera.read()		
		cv2.imshow('Frame', frame)
		
		if cv2.waitKey(1) == ord('q'):
			break
			
	camera.release()
	cv2.destroyAllWindows()
		
if __name__=='__main__':
	main()
	
