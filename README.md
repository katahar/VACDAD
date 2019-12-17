# Portable Gas Sensor
A portable unit that records CO2/VOC data and exports it to a CSV (Excel, etc.) and .txt file. 
Originally developed as a payload for a drone to take gas samples over a lake. 
 
 
 #### Goals
 Update 11.15.19:
 While originally designed for one lab , I want to make this and similar hardware accessible to all research labs, so if you come up with a new way to use this or have started using this in your research, please let me know what you think! 
 #### Current Uses:
  - Lake Draining Study
  - Alzheimer's Study
  - Huntington's Disease Study
  - Emotion Tracking in Dogs
  - Student Learning Tracking in the Classroom
  
  #### Future Uses:
  - Algae Growth Study
 ------
  #### Instructions 
  ##### Before Collecting Data/Notes
  - ___Be sure to "burn in" the sensor for at least 12 hours before using for actual data collection by running the script for 12 hours, per manufacturer instructions___
  - My recommendation is to burn in the sensor for at least the hour before each subsequent data collection. This ensures that it will be a little more accurate. 
  - The first 10-20 data points will be nonsense (recording as TVOC 0 ppb/eCO2 400 ppm), so be sure to start recording for a few seconds before actual data is needed.
  - Each file is named subsequently (ie. data1.txt, data2.txt, etc.) If you want to reset the count, modify the count.data file. 
  
  ##### Instructions for Recording
 - Connect power to Raspberry Pi, wait for red and green LEDs to light up
 - When ready to record, flip the data acquisition switch. The yellow LED should turn on with a slight delay. You are now recording!
 - When data collection is complete, turn the switch off. This will end the recording and save the data as a new .CSV and .txt file. 
  ##### Instructions for Retrieving Data 
- All data is saved on the desktop of the Raspberry Pi under the data folder. All  you need to do is connect it to a mouse, keyboard, and monitor like a normal computer and move them to an external USB drive for further analysis. 
- If you would like to reset the count for the file names, open the count.data file and change the number back to 1 (or whatever number you want the next file to be named) and save. 

##### LED Key
- Red: Power is Connected
- Green: Recording Script is Active, Ready to Record
- Yellow: Device is Recording Data

-------



#### How its Built:
 This is a basic circuit that connects a Raspberry Pi Zero to a gas sensor via I2C communication and records the data output if the switch is set to on, and indicates the state of recording at all times via three LEDs. The Raspberry Pi runs a Python script on startup that is responsible for recording these values.  The entire unit is powered by an external portable phone charger. 
 
#### Hardware
- Rasbperry Pi Zero W
- [Adafruit SGP30 Air Quality Sensor](https://www.adafruit.com/product/3709)
- Portable Charger
- Red, Yellow, and Green LEDs
- 10 kOhm Resistors  (3)
- Soldering Board
- 3 Pin/2 Position Switch
- Micro USB Cable
- Wires

#### Software
 __All required software is on the disk image, but you can follow these instructions if you would like to make your own scratch build__
- Latest build of Raspbian on a microSD card
- Python 3.x.x


#### Planned Additions
 - STL for case to reduce load times
 - Smaller Battery
 - Power switch
 - Burn in switch and LED
 - ___Built-in calibration curve___
 
#### Notes
- Keep in mind that this project is in progress, and will be upgraded over time. 
 
