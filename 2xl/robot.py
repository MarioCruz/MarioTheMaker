from EmulatorGUI import GPIO
import RPi.GPIO as GPIO
import time
import os
from datetime import datetime
import random , glob , subprocess

GPIO.setmode(GPIO.BCM)


GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

previous = None
previoush = None


def rndhmp3 (previous):
   pattern = "../mp3h/*.mp3" # (or "*.*")
   randomfile = random.choice(glob.glob(pattern))
   if randomfile == previoush:
    return rndhmp3 (previoush)
   else:
    return randomfile
 
def rndmp3 (previous):
   pattern = "../mp3/*.mp3" # (or "*.*")
   randomfile = random.choice(glob.glob(pattern))
   if randomfile == previous:
    return rndhmp3 (previous)
   else:
    return randomfile
  

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        random.seed(datetime.now())
        print (random.seed)
        time.sleep(0.2)
        file = rndhmp3 (previoush)
        previous = file
        print ("1111111")
        print(file)
        os.system ('mpg123 ' + file)
        print('Button Stoped')
        
    input_state = GPIO.input(23)
    if input_state == False:
        random.seed(time.time())
        print (random.seed)
        print('Button Pressed')
        time.sleep(0.2)
        file = rndmp3 (previous)
        previous = file
        print ("1111111")
        print(file)
        os.system ('mpg123 ' + file)
        print('Button Stoped')
                
GPIO.cleanup() 
        
        
