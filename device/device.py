import RPi.GPIO as GPIO
import time

accept_button=10
decline_button=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(accept_button, GPIO.IN)
GPIO.setup(decline_button, GPIO.IN)

import requests
import playsound

raw_quest = requests.get("http://127.0.0.1:5000/quest")
newquest=raw_quest.text

if newquest=='ARRIVE':
    playsound.playsound('./audio/canwe.wav')
    while True:
        accept = GPIO.input(accept_button)
        decline = GPIO.input(decline_button)
        if accept == 0:
            requests.get("http://127.0.0.1:5000/update")
            playsound.playsound('./audio/yes.wav')
            break
        if decline == 0:
            playsound.playsound('./audio/no.wav')
            break
        
        
            
                  
    

