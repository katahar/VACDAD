#Things to add
# Run on startup
# Print "calibration" instead of 400 and 0
#elapsed time
# script LED
# Numbers indicator, Binary?


import RPi.GPIO as GPIO
import board
import busio
import adafruit_sgp30

import time
from time import sleep

import datetime
from datetime import datetime
from datetime import timedelta

from sys import argv


GPIO.setmode(GPIO.BCM)

#scriptLED = 1111111111111111111111111111111111
logLED = 19
scriptLED = 4
switch = 26

GPIO.setup(scriptLED,GPIO.OUT) #script LED


GPIO.setup(logLED,GPIO.OUT) #logging LED
GPIO.setup(switch,GPIO.IN,pull_up_down=GPIO.PUD_UP) #status switch input
#will probably need to setup other pins

#starts i2c instance
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

#starts up sensor
sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8aae)
 
GPIO.output(scriptLED,GPIO.HIGH)
#power on blink
for x in range(0,3):
    GPIO.output(logLED,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(logLED,GPIO.HIGH)
    time.sleep(0.5)
    
while True: #big constant loop
    state = GPIO.input(switch)
    if state: #checks if switched on or off
        #turns off LED
        GPIO.output(logLED,GPIO.LOW)
        print("Off\n")
        time.sleep(1)
    else: #logic inverted for flow of code
       
       print("ON\n")
       #turns on LED
       GPIO.output(logLED,GPIO.HIGH)
        
       print("checking counter\n")
       #opens counter.data file to check which log instance will be run next
       with open("/home/pi/Documents/TestingFiles/FinalScript/counter.data", "r") as counter:
           count = int( counter.read() )
           print("Current count: %d \n" % (count) )
           counter.close()
       #updates counter.data file to show which will be the next instance    
       with open("counter.data", "w") as counter:
           counter.write(str(count+1))
           counter.close()
           
           
       #creates log file labelled with instance
       filename = "datalog" + str(count) +".txt"
       writeFile = open(filename, "w+")
       print("creating file: " +filename)
       
       #gets the date and time of the start of the log
       startTime = datetime.now()
       timestr = startTime.strftime("%m/%d/%Y, %H:%M:%S") #converts timestamp to string using specified format
       
       #titles and records time of log
       writeFile.write("-------------------- Log Instance %d -------------------- \n" % (count) )
       writeFile.write("Began at: " + timestr + "\n")
       print("-------------------- Log Instance %d -------------------- \n" % (count) )
       print("Began at: " + timestr + "\n")
       
       #starts a count to report time every x seconds
       ct = 1
       x = 10
       while state == False: #had to be changed because of the logic inversion before
           #writes sensor value
           writeFile.write("Reading: %d \t eCO2 = %d ppm \t TVOC = %d ppb \n" % (ct, sgp30.eCO2, sgp30.TVOC))
           print("Reading: %d \t eCO2 = %d ppm \t TVOC = %d ppb \n" % (ct, sgp30.eCO2, sgp30.TVOC))
           ct = ct + 1
           #reports time every x seconds
           if (ct%x == 0):
               curTime = datetime.now()
               timestr = curTime.strftime("%H:%M:%S") #converts timestamp to string using specified format
               writeFile.write("Current Time:" + timestr + "\n")
               print("Current Time:" + timestr + "\n")
           state = GPIO.input(switch) #updates switch value every iteration
           time.sleep(1) # delay between reads
           
       print("----------------- End of Log Instance %d ----------------- \n" % (count) )
       
       #gets and records endtime
       curTime = datetime.now()
       timestr = curTime.strftime("%m/%d/%Y, %H:%M:%S") #converts timestamp to string using specified format
       writeFile.write("Log ended at: " + timestr + "\n")
       print("Log ended at: " + timestr + "\n")
       
       #time elapsed has to be fixed
        #calculates and records elapsed time
       timeElapsed = startTime - curTime
       strTimeElapsed = str(timeElapsed.seconds)
       
       #writeFile.write("Time Elapsed: " + strTimeElapsed + " seconds \n")
       #print("Time Elapsed: " + strTimeElapsed + " seconds \n")
       print("\n\n\n")
       writeFile.close()
       #turns off LED
       GPIO.output(logLED,GPIO.LOW)          

GPIO.cleanup()
