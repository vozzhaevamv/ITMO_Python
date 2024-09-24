birth_day = int(input('Введите день вашего рождения (от 1 до 31):'))
birth_month = int(input('Введите месяц вашего рождения(от 1 до 12):'))
birth_year = int(input('Введите год вашего рождения:'))
if birth_month <= 3:
    print('Первый квартал')
elif birth_month <= 6:
    print('Второй квартал')
elif birth_month <= 9:
    print('Третий квартал')
elif birth_month <= 12:
    print('Четвертый квартал')
if (birth_year % 4 == 0 and birth_year % 100 != 0) or birth_year % 400 == 0:
   print('Год вашего рождения високосный') 
else:
    print('Год вашего рождение не високосный')
this_day = int(input('Введите текущий день:'))
this_month = int(input('Введите текущий месяц (число от 1 до 12):'))
this_year = int(input('Введите текущий год:'))
day_Birthday=(birth_year* 365.25) + (birth_month * 30.44) + (birth_day) #Сколько дней с 0 н.э прошло до дня рождения
today=(this_year * 365.25) + (this_month * 30.44 ) + this_day #Сколько дней с 0 н.э прошло до текущего дня
days =today - day_Birthday  #При длине года в 365.25 дней Среднее количество дней в месяце = 30.44.
print(f"С момента вашего рождения прошло примерно {int(days)} дней.")
