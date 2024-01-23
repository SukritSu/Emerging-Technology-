import os.path
from datetime import datetime
from os.path import exists
import pynmea2
import time as TIME

# now = datetime.now()
# print("Now = ", now) # Current date and time

# timestamp = now.timestamp()
# msg = pynmea2.parse("$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D")
# print(int(timestamp))

file_exists = os.path.exists("F:\SEM 4\Pyhton data\LABS\LAB 1\mygeodata\Directions.nmea")
if file_exists == True:
  print(file_exists, ": The file exists")
  file = open("F:\SEM 4\Pyhton data\LABS\LAB 1\mygeodata\Directions.nmea")
  print("Opening File")

  TIME.sleep(2)

  count = 0
  for line in file.readlines():
      text = pynmea2.parse(line)
      time = datetime.now().timestamp()
      latitude = text.lat
      longitude = text.lon
      count = count + 1
      if (count < 23):
          Json = {"count": count, "app": "gps_test", "timestamp": int(time), "latitude": latitude,
                  "longitude": longitude}
          print(Json)
          TIME.sleep(0.5)

else:
  print("The file does not exist on this path")


