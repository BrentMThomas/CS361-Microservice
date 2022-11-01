# Author: Brent Thomas
# CS 361_400 - Assignment 8 Microservice for Dacin Titus
# 10/31/2022
# Referenced code for this from: https://www.programiz.com/python-programming/datetime/current-time

import pytz
from datetime import datetime


# read time zone from the time_read.txt file
time_service = open('time_read.txt', 'r')
time_zone_read = time_service.readline()
time_service.close()

# write time to the time_write.txt file
time_zone = pytz.timezone(time_zone_read) 
datetime_rqt = datetime.now(time_zone)
time_rqt = datetime_rqt.strftime("%H:%M")
datetime_str = str(time_rqt)
time_write = open('time_write.txt', 'w')
time_write.write(datetime_str)
time_write.close()
