#-*- coding:utf-8 -*-

from click import pass_obj
import cv2 						# opencv 
import pyzbar.pyzbar as pyzbar	# bacode
import pygame					# 소리 출력

import requests
import json
import time


class bacode:
	pass

 

data_list =[]											# 배열 생성
f = open("/home/pi/hee/qrbarcode_data.txt","r")			# 바코드가 저장된 텍스트 파일 열기 
data_list = f.readlines()								# 배열에 바코드 값 저장



pygame.mixer.init()
p = pygame.mixer.Sound("qrbarcode_beep.wav")			# 소리파일 설정 

cap = cv2.VideoCapture(0)		# 비디오 파일이나 카메라 연동
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)




while True:						# 비디오에서 이미지를 한 장씩 가져옴	


	success, frame = cap.read()	# success 이미지를 잘 읽었으면 true 반환
								# frame cap.read(읽은 이미지) 저장 	
	break_point = False	
	

	if success:
		for code in pyzbar.decode(frame):	# 이미지에서 바코드를 찾고 디코딩

				
			Send_my_code = str(code.data.decode('utf-8'))
			my_code = code.data.decode('utf-8')			
			check = Send_my_code[0:3]				
			store = Send_my_code[3:7]		# 지점명
			item = Send_my_code[7:12]		# 제품명
			count = Send_my_code[12:13]
			
			
			for i in range(0, len(data_list),1):		# 배열의 길이 만큼 반복 => 저장된 바코드를 찾기 위해 

				#my_code = code.data.decode('utf-8') 	# ?
							
				b = data_list[i]
				Splitb = b[0:13]						# 배열 값에서 얖자리 2자리 추출 				

				if	Send_my_code == Splitb:
					while True:
						p.play()				# 소리 출력 
						time.sleep(0.1)						
						break;
					print("인식성공")					
																		
					if bacode.check == str(880):
						break_point = True	
						print("escape1")										
						break;

			if break_point == True:
				print("escape2")				
				break;				
		
		response = requests.post("http://192.168.0.79:4000/api/test",data ={'data1': json.dumps(check),'data2' : json.dumps(store),'data3' : json.dumps(item),'data4' : json.dumps(count)})
		Send_my_code =""
		print(Send_my_code)
		

		cv2.imshow('cam', frame) 	# 읽은 이미지 출력(새 창을 띄어서 출력)

		key = cv2.waitKey(1)		# 사용자가 key를 누를때 까지 대기 
		if key == 27:
			break;

		

cv2.release()
cv2.destroyAllWindows()			# 띄운 새 창을 모두 닫아준다. 

