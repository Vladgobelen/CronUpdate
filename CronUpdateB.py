#!/usr/bin/python
import datetime

crontab = r'''
{min1} {hours1} * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh
{min2} {hours2} * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh
10 11 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh
10 23 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh
14 03 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh
14 15 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh
{min1} {hours1} * * * env DISPLAY=:0 python /home/diver/Скрипты/CronUpdate/CronUpdate.py
'''

now = datetime.datetime.now()
time1 = now + datetime.timedelta(hours=2, minutes=30)
time2 = now + datetime.timedelta(hours=0, minutes=5)

with open('/home/diver/Скрипты/temp/test', 'w') as f:
    f.write(crontab.format(
        min1=time1.strftime("%M"),
        hours1=time1.strftime("%H"),
        min2=time2.strftime("%H"),
        hours2=now.strftime("%H")
    ))
