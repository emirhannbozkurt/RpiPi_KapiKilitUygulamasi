from gpiozero import MotionSensor
import RPi.GPIO as GPIO
from signal import pause
import time

GPIO.setmode(GPIO.BCM)
 #buzzer
BuzzerPin = 18
GPIO.setup(BuzzerPin, GPIO.OUT)

pir = MotionSensor(4)

GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)


button = 25
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)




GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)
servo1.start(0)

DISPLAY = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]            

GPIO.setwarnings(False)           


GPIO.setup(13,GPIO.OUT)         
GPIO.setup(6,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

def PORT(pin):                    
    if(pin&0x01 == 0x01):
        GPIO.output(13,1)           
    else:
        GPIO.output(13,0)           
    if(pin&0x02 == 0x02):
        GPIO.output(6,1)            
    else:
        GPIO.output(6,0)           
    if(pin&0x04 == 0x04):
        GPIO.output(16,1)
    else:
        GPIO.output(16,0)
    if(pin&0x08 == 0x08):
        GPIO.output(20,1)
    else:
        GPIO.output(20,0)   
    if(pin&0x10 == 0x10):
        GPIO.output(21,1)
    else:
        GPIO.output(21,0)
    if(pin&0x20 == 0x20):
        GPIO.output(19,1)
    else:
        GPIO.output(19,0)
    if(pin&0x40 == 0x40):
        GPIO.output(26,1)
    else:
        GPIO.output(26,0)
    if(pin&0x80 == 0x80):
        GPIO.output(12,1)            
    else:
        GPIO.output(12,0)


while True:
    buton_durum = GPIO.input(button)
    if(buton_durum == 0 or pir.wait_for_motion()):
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(22,GPIO.LOW)

        
        #servo kodu
        duty = 2
        
        # Loop for duty values from 2 to 12 (0 to 180 degrees)
        print("kapi acildi")
        while duty <= 7:
            
            servo1.ChangeDutyCycle(duty)
            time.sleep(0.1)
            duty = duty + 1
       
            
            
            
        pin = DISPLAY[5]        
        PORT(pin);                  
        time.sleep(1)
            
        pin = DISPLAY[4]        
        PORT(pin);                  
        time.sleep(1)
            
        pin = DISPLAY[3]        
        PORT(pin);                  
        time.sleep(1)
            
        pin = DISPLAY[2]        
        PORT(pin);                  
        time.sleep(1)
            
        pin = DISPLAY[1]        
        PORT(pin);                  
        time.sleep(1)
            
        pin = DISPLAY[0]        
        PORT(pin);                  
        time.sleep(1)
        GPIO.output(BuzzerPin,1)   
            
        
        print("kapi kapandi")
        servo1.ChangeDutyCycle(2)
        time.sleep(0.5)
        
    else:
        pin = DISPLAY[0]        
        PORT(pin);                  
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(27,GPIO.LOW)
servo1.stop()
GPIO.cleanup()