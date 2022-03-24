import pygame
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button_pin = 15
GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

pygame.mixer.init()
p1 = pygame.mixer.Sound("qrbarcode_beep.wav")
p2 = pygame.mixer.Sound("error_beep.wav")

while(1):
	if GPIO.input(button_pin) == GPIO.HIGH:
		p1.play(1)
		time.sleep(2.5)
		#p.stop()
	
	else:		
		p2.play(5)
		time.sleep(5)
		break
	
	
	
	
