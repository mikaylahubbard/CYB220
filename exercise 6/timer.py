#! /usr/bin/python3
from datetime import datetime
import time

while True:
    current_time = datetime.now()
    current_time = str(current_time)
    with open('timeLog.txt', 'a') as file:
        file.write(f"{current_time}\n")
    time.sleep(5)
   
