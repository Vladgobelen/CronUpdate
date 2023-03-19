#! /bin/env lua
--получаем текущие минуты
local minut = io.popen("date +%M", 'r');
local minut_data = tonumber(minut:read('*a'));
--получаем текущие часы
local hour = io.popen("date +%H", 'r');
local hour_data = tonumber(hour:read('*a'));
--статичная прибавка времени
local minut_plus = 30;
local hour_plus = 2;
local hour_plus_b = 3;
--переменые для требуемого времени
local hour_new;
local minut_new

--отладка
print (minut_data);
print (hour_data);
--отладка

--проверяем количество минут
if minut_data >= 30 then
--если количество текущих минут больше 30, то к часам прибавляем 3, а от текущего времени отнимаем 30 минут
    hour_new = hour_data + hour_plus_b;
    minut_new = minut_data - minut_plus;
else
--если количество текущих минут меньше 30, то к часам прибавляем 2, а к текущим минутам 30
    hour_new = hour_data + hour_plus;
    minut_new = minut_data + minut_plus;
end

--отладка
print (minut_new);
print (hour_new);
-- отладка

---формируем строку для крона
local cron_time = minut_new .. " " .. hour_new .. " * * * env DISPLAY=:0 sh /home/diver/Скрипты/alarm.sh";

--отладка
print (cron_time);
--отладка

---записать переменную в файл
local cronFile = io.open("/home/diver/Скрипты/temp/cronf", "r")
cronFile:write (cron_time, '\n')
cronFile:close()





