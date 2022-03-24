#-*- coding:utf-8 -*-

import cv2 						# opencv 
import pyzbar.pyzbar as pyzbar	# bacode
import pygame					# 소리 출력
import RPi.GPIO as GPIO

import requests
import json
import time 

GPIO.setmode(GPIO.BCM)									#버튼 설정
GPIO.setwarnings(False)
button_pin = 15
GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

pygame.mixer.pre_init(44100,-16,2,512)
pygame.mixer.init()
p1 = pygame.mixer.Sound("qrbarcode_beep.wav")			# 소리파일 설정
p2 = pygame.mixer.Sound("error_beep.wav")

cap = cv2.VideoCapture(0)		# 비디오 파일이나 카메라 연동
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

while True:						# 비디오에서 이미지를 한 장씩 가져옴 
    success, frame = cap.read()	# success 이미지를 잘 읽었으면 true 반환
                                # frame cap.read(읽은 이미지) 저장 	
    break_point = False
    cv2.imshow('cam', frame) 	# 읽은 이미지 출력(새 창을 띄어서 출력)
	
    if success:        
        for code in pyzbar.decode(frame):	# 이미지에서 바코드를 찾고 디코딩
            my_code = str(code.data.decode('utf-8'))           
            o1 = int(my_code[0:1])
            e1 = int(my_code[1:2])
            o2 = int(my_code[2:3])
            e2 = int(my_code[3:4])
            o3 = int(my_code[4:5])
            e3 = int(my_code[5:6])
            o4 = int(my_code[6:7])
            e4 = int(my_code[7:8])
            o5 = int(my_code[8:9])
            e5 = int(my_code[9:10])
            o6 = int(my_code[10:11])
            e6 = int(my_code[11:12])
            checknum = int(my_code[12:13])
            
            odd = o1+o2+o3+o4+o5+o6
            even = (e1+e2+e3+e4+e5+e6)*3
            bar = (odd + even + checknum)%10

            if bar == 0:
                print(bar)
                print("인식성공")
                print(my_code)             
                

                if GPIO.input(button_pin) == GPIO.HIGH:
                    
                    country = my_code[0:3]
                    manufactor = my_code[3:7]
                    item = my_code[7:12]
                    checknum = str(my_code[12:13])
                    #http://192.168.0.79:4000/api/test
                    response = requests.post("http://192.168.0.79:4000/managerPage/registration",data ={'data1': json.dumps(country),'data2' : json.dumps(manufactor),'data3' : json.dumps(item),'data4' : json.dumps(checknum)})
                    server_response = int(response.status_code)

                    if server_response == 200:
                        print("전송완료")
                        p1.play(1)
                        time.sleep(1)
                        p1.stop()
                        print(my_code)
                        my_code =" "                 
                        break;

                    else:
                        p2.play(1)
                        print("인식실패")
                        time.sleep(1)
                        p2.stop()
                        break;                                                              
               
                
        key = cv2.waitKey(1)		# 사용자가 key를 누를때 까지 대기
        if key == 27:
            break;

cap.release()						# 비디오 종료
cv2.destroyAllWindows()			# 띄운 새 창을 모두 닫아준다.
