import datetime;
minNew = (datetime.datetime.now() + datetime.timedelta(hours=2, minutes=30)).strftime("%M");
hourNew = (datetime.datetime.now() + datetime.timedelta(hours=2, minutes=30)).strftime("%H");
minNewB = (datetime.datetime.now() + datetime.timedelta(hours=0, minutes=5)).strftime("%M");
hourNewB = (datetime.datetime.now() + datetime.timedelta(hours=0, minutes=0)).strftime("%H");

cronNew = open('/home/diver/Скрипты/temp/cron', 'w');

cronNew.write(minNew + " " + hourNew + " * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh" + "\n");
cronNew.write(minNewB + " " + hourNewB + " * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh" + "\n");
cronNew.write("10 11 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh" + "\n");
cronNew.write("10 23 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh" + "\n");
cronNew.write("14 03 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh" + "\n");
cronNew.write("14 15 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh" + "\n");
cronNew.close();
