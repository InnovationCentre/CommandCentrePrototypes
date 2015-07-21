#imports
import RPi.GPIO as GPIO
import time

#init script

print('start')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

buttonBack = 17
buttonFront = 18
buttonReset = 21

ledGreen = 22
ledRed = 23                                       
ledWhite = 24

GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledWhite, GPIO.OUT)
GPIO.setup(buttonBack, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(buttonFront, GPIO.IN, GPIO.PUD_UP) 
GPIO.setup(buttonReset, GPIO.IN, GPIO.PUD_UP)

#init, set start situation
GPIO.output(ledRed,0) 
GPIO.output(ledGreen, 0)
GPIO.output(ledWhite, 0)
redOn = False

#start logic
while (True):
    if((GPIO.input(buttonReset) == False)):
        break
    if((GPIO.input(buttonFront) == True) and (GPIO.input(buttonBack) == False)) :
       print('Back detected, drive forward')
       GPIO.output(ledWhite, 0)
       GPIO.output(ledRed, 0 if (redOn) else 1)
       redOn = not redOn
       time.sleep(0.5)
       
    if((GPIO.input(buttonFront) == False) and (GPIO.input(buttonBack) == True)) :
       print('Front detected, drive backwards')
       GPIO.output(ledWhite, 0)
       GPIO.output(ledRed, 0 if (redOn) else 1)
       redOn = not redOn
       time.sleep(0.5)

    if((GPIO.input(buttonFront) == False) and (GPIO.input(buttonBack) == False)) :
       print('positioned correctly')
       GPIO.output(ledGreen, 1)
       GPIO.output(ledRed, 0)
       GPIO.output(ledWhite, 0)
    elif((GPIO.input(buttonFront) == True) and (GPIO.input(buttonBack) == True)):
       print('OVC Station available for usage')
       GPIO.output(ledWhite, 1)
       GPIO.output(ledRed, 0)
       redOn = False
       GPIO.output(ledGreen, 0)
    else:
       GPIO.output(ledGreen, 0)

#cleanup and finish
GPIO.cleanup()
print('end')
