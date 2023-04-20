import datetime;
minNew = (datetime.datetime.now() + datetime.timedelta(hours=2, minutes=30)).strftime("%M")
hourNew = (datetime.datetime.now() + datetime.timedelta(hours=2, minutes=30)).strftime("%H")
minNewB = (datetime.datetime.now() + datetime.timedelta(hours=0, minutes=5)).strftime("%M")
hourNewB= (datetime.datetime.now() + datetime.timedelta(hours=0, minutes=5)).strftime("%H")
cronNew = open('/var/spool/cron/crontabs/diver', 'w')
#отладочный файл
#cronNew = open('/home/diver/Скрипты/temp/testCron', 'w')

cronNew.write(minNew + " " + hourNew + " * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh" + "\n")
cronNew.write(minNewB + " " + hourNewB + " * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh" + "\n")
cronNew.write("15 13 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh" + "\n")
cronNew.write("15 01 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh" + "\n")
cronNew.write("14 04 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh" + "\n")
cronNew.write("14 16 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh" + "\n")
cronNew.write(minNew + " " + hourNew + " * * * env DISPLAY=:0 python /home/diver/Скрипты/CronUpdate/CronUpdate.py" + "\n")

cronNew.close();
