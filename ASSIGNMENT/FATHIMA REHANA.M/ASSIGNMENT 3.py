Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library  from time import sleep  
... GPIO.setwarnings(False)  
... GPIO.setmode(GPIO.BOARD)  
... GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)  
... while True:  
... GPIO.output(8, GPIO.HIGH)  
... sleep(1)  
... GPIO.output(8, GPIO.LOW)  
... sleep(1)  
... import RPi.GPIO as GPIO 
... from time import sleep  
... GPIO.setwarnings(False)  
... GPIO.setmode(GPIO.BOARD)  
... GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)  
... while True:  
... GPIO.output(8, GPIO.HIGH)  
... sleep(1)  
... GPIO.output(8, GPIO.LOW)  
... sleep(1)
