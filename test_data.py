from datetime import datetime, timedelta
# Приводим дату и время в читабельный вид
now = str(datetime.now())[:-7]
time = datetime.strftime(datetime.strptime(str(timedelta(milliseconds = 5818400))[:-7], 
                            "%H:%M:%S"), "%H:%M:%S")
result = [now, time]
duration = datetime.time(datetime.strptime(result[1], "%H:%M:%S"))
# Конвертируем обратно в миллисекунды
req = timedelta(hours=int(duration.hour), 
        minutes=int(duration.minute),
        seconds=int(duration.second)+1) / timedelta(milliseconds=1)
x = datetime.strptime(result[0], "%Y-%m-%d %H:%M:%S")
y = timedelta(milliseconds = int(req))
print("Дата: ",x)
print("Время: ",y)
print("Результат: ",x+y)