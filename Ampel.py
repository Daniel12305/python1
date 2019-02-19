import RPi.GPIO as GPIO
import time
from signal import pause
from gpiozero import Button #, Buzzer

GPIO.setmode(GPIO.BCM)

button = Button(2)
#buzzer = Buzzer(18)

# 26 rot Auto
# 14 gelb Auto
# 15 grün Auto
# 21 rot Foßgänger
# 20 grün Fußgänger

GPIO.setup(26, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

GPIO.output(21, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)
         
def Fußgänger():
    print("pressed")
    time.sleep(10)
    giveRedToCars()
    giveGreenToPeds()
    time.sleep(10)
    giveRedToPeds()
    time.sleep(2)
    giveGreenToCars()
    
    
    
def giveRedToCars():
    GPIO.output(15, GPIO.LOW)
    GPIO.output(14, GPIO.HIGH)
    time.sleep(4)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(26, GPIO.HIGH)

def giveGreenToPeds():
    time.sleep(2)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(20, GPIO.HIGH)
    #buzzer.on()
    
def giveRedToPeds():
    #buzzer.off()
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.HIGH)
    
def giveGreenToCars():
    GPIO.output(14, GPIO.HIGH)
    time.sleep(4)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(15, GPIO.HIGH)
  

button.when_pressed = Fußgänger





    
pause()

