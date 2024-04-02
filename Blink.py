from machine import Pin
import time


led = Pin('LED', Pin.OUT)

while True:
  led.value(True) 
  time.sleep(1)  
  led.value(False) 
  time.sleep(1)   