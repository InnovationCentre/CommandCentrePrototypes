import RPi.GPIO as GPIO
import time
import example_file

print('start')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button17 = 17
button18 = 18
button21 = 21

global a
a = 5

led22 = 22
led23 = 23                                     
led24 = 24
led25 = 25

statusled22 = 0
statusled23 = 0
statusled24 = 0
statusled25 = 0

GPIO.setup(led22, GPIO.OUT)
GPIO.setup(led23, GPIO.OUT)
GPIO.setup(led24, GPIO.OUT)
GPIO.setup(led25, GPIO.OUT)
GPIO.setup(button17, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button18, GPIO.IN, GPIO.PUD_UP) 
GPIO.setup(button21, GPIO.IN, GPIO.PUD_UP)

GPIO.output(led22, 0) 
GPIO.output(led23, 0)
GPIO.output(led24, 0)
GPIO.output(led25, 0)



#start logic
while (True):

#test blinking leds
    '''
    GPIO.output(led22, not statusled22)
    statusled22 = not statusled22
    GPIO.output(led24, not statusled23)
    statusled23 = not statusled23
    time.sleep(1)
    GPIO.output(led23, not statusled24)
    statusled24 = not statusled24
    GPIO.output(led25, not statusled25)
    statusled25 = not statusled25
    time.sleep(1)
    '''

#test buttons
    
    if(GPIO.input(button17)== False):
        print('statusbutton17')
    
    elif(GPIO.input(button18)== False):
        print('statusbutton18')

    elif(GPIO.input(button21)== False):
        print('statusbutton21')

    else:
        print('niks')
        

#cleanup and finish
GPIO.cleanup()
print('end')
'''
def testa():
    global a
    a = 20
'''
