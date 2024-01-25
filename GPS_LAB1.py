import os.path
from datetime import datetime
from os.path import exists
import pynmea2
import time as TIME
import threading
import keyboard
global_stop = 0
def print_coord_string():
    try:
        if global_stop != 1:
            file = open("./Directions_from_72_Hoffman_Street_Kitchener_ON_to_Conestoga_College_Cambridge_-_Fountain_Street_campus_Fountain_Street_South_Cambridge_ON.nmea")
            print("Opening File")
            TIME.sleep(2)
            count = 0
            for line in file.readlines():
                text = pynmea2.parse(line)
                time = datetime.now().timestamp()
                latitude = text.lat
                longitude = text.lon
                count = count + 1
                Json = {"count": count, "app": "gps_test", "timestamp": int(time), "latitude": latitude,"longitude": longitude}
                print(Json)
                TIME.sleep(0.5)
                if global_stop == 1:
                    exit()
    except Exception as err:
        print(f"{type(err).__name__} was reached")


def wait_for_close():
    global global_stop
    while(global_stop != 1):
        if keyboard.is_pressed('space'):
            global_stop = 1
            print("Closing Program")
            exit()
        
if __name__ == "__main__":
    global_stop = 0
    print("Booting up program")
    if os.path.exists("./Directions_from_72_Hoffman_Street_Kitchener_ON_to_Conestoga_College_Cambridge_-_Fountain_Street_campus_Fountain_Street_South_Cambridge_ON.nmea"):
        print("File Exists continuing with software")
        t1 = threading.Thread(target=print_coord_string)
        t2 = threading.Thread(target=wait_for_close)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    else:
        print("File does not exist")
    print("\nProgramming Ending")
