#-*- coding:utf-8 -*-

import cv2 						# opencv 
import pyzbar.pyzbar as pyzbar	# bacode
#from playsound import playsound	#sound 


cap = cv2.VideoCapture(0)		# 비디오 파일이나 카메라 연동 

while True:						# 비디오에서 이미지를 한 장씩 가져옴 
	success, frame = cap.read()	# success 이미지를 잘 읽었으면 true 반환
								# frame cap.read(읽은 이미지) 저장 
	if success:
		for code in pyzbar.decode(frame):	# 이미지에서 바코드를 찾고 디코딩
								
			my_code = code.data.decode('utf-8') # ?
			print("success: ", my_code)
			#store = my_code[1:4]		# 지점명
			#item = my_code[4:8]			# 제품명			
			#print(store)
			#print(item)				
			#playsound("/home/pi/hee/python_qrbarcode_reader/qrbarcode_beep.mp3")
			
		cv2.imshow('cam', frame) 	# 읽은 이미지 출력(새 창을 띄어서 출력)
		
		key = cv2.waitKey(1)		# 사용자가 key를 누를때 까지 대기 
		if key == 27:
			break

cap.release()						# 비디오 종료
cv2.destroyAllWindows()			# 띄운 새 창을 모두 닫아준다. 

