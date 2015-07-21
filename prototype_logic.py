#imports
import RPi.GPIO as GPIO
from threading import Thread
import time

#init 
print('start')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

#declaring inputs
buttonLeftSwitch  = 17
buttonRightSwitch = 18
buttonGarbageUnit = 21

#declaring outputs
LedBlue   = 22                                        
LedYellow = 25
LedGreen  = 23
LedRed = 24

#declaring variables
ParkingState = 'Unparked'
Dumping = False
GreenLedStatus = 0
YellowLedStatus = 0
BlueLedStatus = 0
blinking = False

#configure inputs
GPIO.setup(buttonLeftSwitch,  GPIO.IN, GPIO.PUD_UP)
GPIO.setup(buttonRightSwitch, GPIO.IN, GPIO.PUD_UP) 
GPIO.setup(buttonGarbageUnit, GPIO.IN, GPIO.PUD_UP)

#configure outputs
GPIO.setup(LedBlue,   GPIO.OUT)
GPIO.setup(LedYellow, GPIO.OUT)
GPIO.setup(LedGreen,  GPIO.OUT)
GPIO.setup(LedRed,    GPIO.OUT)

GPIO.output(LedGreen,  0)
GPIO.output(LedBlue,  0)
GPIO.output(LedYellow, 0)
GPIO.output(LedGreen,  0)
GPIO.output(LedRed,    1)

#Functions
class BlinkThread(Thread):
    
    def __init__(self, pin):
        self.pin = pin
        self.delay = 0.5
        self.running = True
        super(BlinkThread, self).__init__()
        
    def run(self):
        while (self.running):
            GPIO.output(self.pin, True)
            time.sleep(self.delay)
            GPIO.output(self.pin, False)
            time.sleep(self.delay)
        
    def stop(self):
        self.running = False

    def running(self):
        return running

class CheckContainer(Thread):
    
    def __init__(self, pin):
        self.blinkingPin = pin
        self.delay = 1
        self.running = True
        super(CheckContainer, self).__init__()
        
    def run(self):
        container = None
        while (self.running):
            if(GPIO.input(buttonGarbageUnit)== True):
                if(container == None):
                    container = BlinkThread(self.blinkingPin)
                    container.name = 'container missing blinking'
                    container.start()
            else:
                if(not container == None):
                    container.stop()
                container = None
                GPIO.output(self.blinkingPin, True)
            time.sleep(0.05)       
    def stop(self):
        self.running = False
            
#Program
while (True):
#There are 4 possibilities:
    #The Car is Parking
    #The car is Parked
    #The car is Unparking
    #The car is UnParked

    containerCheck = CheckContainer(LedGreen)
    containerCheck.start()
                
    if((ParkingState == 'Parking')):
        print(ParkingState)
        #EDIT: Start both motors forwards
        while(True):
            if((GPIO.input(buttonLeftSwitch) == False)and(GPIO.input(buttonRightSwitch)==False)):
                ParkingState = 'Parked'
                #EDIT: Timeout error
                break

    if((ParkingState == 'Parked')):
        print(ParkingState)
        #EDIT: Stop both motors
        
        while(True):
            Command = input ('Give command "Dump" or "Unpark" or "Charge": ')
            if(Command == 'Unpark'):
                ParkingState = 'Unparking'
                break
            elif(Command == 'Dump'):
                if(GPIO.input(buttonGarbageUnit)== False):
                    print('Dumping')
                    print('.....')
                    print('Dumping Finished')
                elif(GPIO.input(buttonGarbageUnit)== True):
                    print('Place Garbage Unit back')
            elif(Command == 'Charge'):
                print('Charging')
                print('.....')
                
                blink = BlinkThread(LedBlue)
                blink.name = 'robot charging'
                blink.start()
                time.sleep(5)
                print('Charged')
                blink.stop()
                GPIO.output(LedBlue, True)

    if((ParkingState == 'Unparking')):
        print(ParkingState)
        #EDIT: Start both motors backwards
        while(True):
            if((GPIO.input(buttonLeftSwitch) == True)and(GPIO.input(buttonRightSwitch)== True)):
                ParkingState = 'Unparked'
                #EDIT: Timeout error
                break        

    if((ParkingState == 'Unparked')):
        print(ParkingState)
        GPIO.output(LedGreen, 0)
        #EDIT: Let robot do its task
        while(True):
            if(buttonGarbageUnit==False):
                GPIO.output(LedGreen, False)
            elif(buttonGarbageUnit==True):
                GPIO.output(LedGreen, True)
            Command = input ('Give command "Park": ')
            if(Command == 'Park'):
                ParkingState = 'Parking'
                break

GPIO.cleanup()
