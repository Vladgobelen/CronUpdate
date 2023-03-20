#! /bin/env lua
--получаем текущие минуты
local minut = io.popen("date +%M", 'r');
local minut_data = tonumber(minut:read('*a'));
--получаем текущие часы
local hour = io.popen("date +%H", 'r');
local hour_data = tonumber(hour:read('*a'));
--статичная прибавка времени
local minut_plus = 30;
local minut_plus_b = 5;
local hour_plus = 2;
local hour_plus_b = 3;
--переменые для требуемого времени
local hour_new;
local minut_new;
local minut_new_b;
--проверяем количество минут
if minut_data >= 30 then
--если количество текущих минут больше 30, то к часам прибавляем 3, а от текущего времени отнимаем 30 минут
    hour_new = hour_data + hour_plus_b;
    minut_new = minut_data - minut_plus;
    minut_new_b = minut_new + minut_plus_b;
else
--если количество текущих минут меньше 30, то к часам прибавляем 2, а к текущим минутам 30
    hour_new = hour_data + hour_plus;
    minut_new = minut_data + minut_plus;
    minut_new_b = minut_new + minut_plus_b;
end

if hour_new >= 23 then
    hour_data = 0
else
end

---формируем строки для крона
local cron_time = minut_new .. " " .. hour_new .. " * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh";
local cron_time1 = minut_new_b .. " " .. hour_new .. " * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh";
local cron_time2 = "07 11 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh";
local cron_time3 = "07 23 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh";
local cron_time4 = "14 03 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh";
local cron_time5 = "14 15 * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh";
--local cron_time6 = minut_new .. " " .. hour_new .. " * * * env DISPLAY=:0 /home/diver/Скрипты/CronUpdate/CronUpdate.lua";

---записать переменную в файл
local cronFile = io.open("/var/spool/cron/crontabs/diver", "w");
cronFile:write (cron_time, '\n');
cronFile:write (cron_time1, '\n');
cronFile:write (cron_time2, '\n');
cronFile:write (cron_time3, '\n');
cronFile:write (cron_time4, '\n');
cronFile:write (cron_time5, '\n');
--cronFile:write (cron_time6, '\n');

cronFile:close();
--os.execute("chmod -R 777 /var/spool/cron/crontabs/diver");
