echo "sh /home/diver/Скрипты/alarm.sh" |at now +5 minutes
echo "sh /home/diver/Скрипты/alarm.sh" |at now +150 minutes
/home/diver/Скрипты/CronUpdate/CronUpdate.sh |at now +150 minutes
date > /home/diver/Скрипты/temp/date |at now +150 minutes
python -c 'import datetime; print(datetime.datetime.now() + datetime.timedelta(hours=2, minutes=30))' > /home/diver/Скрипты/dateNew
