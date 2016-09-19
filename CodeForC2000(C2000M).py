#!/usr/bin/env python

#Скрипт расчёта идеальной комбинаций кода для С2000 (С2000М)
#В коде должно быть задействовано 10 цифр, и при этом одна цифра должна
#быть задействована лишь единожды.
#Начало: 11 декабря 2015 г. 01:44

#Версия скрипт
CodeForC2000Version = '1.3.1'

#Исправлено в ver.1.3.1
#--------------------
#1.Убраны лишнии пробелы при выводе информации на экран (print (sep = ''))
#2.По производительности, разница между ver.1.1 и ver.1.2, примерно, в 2 раза.
#3.Добавил вывод времени работы скрипта с форматированием. Значительной потери производительности не замечено.

#План работ на ver.1.X
#---------------------
#1.Проверить, влияют ли коменты в программе на её производительность (удалить все коменты и сравнить время выполнения).
#2.Разработать часть кода вычисляющего полное время работы скрипта.
#3.Рассмотреть возможность сохранения результатов работы в файл.
#4.Рассмотреть возможность продолжения работы с момента последней записи в файл.

#Подключаем модули (в данном случае - модуль времени)
from time import strftime, localtime, time, gmtime

#Время начала работы скрипта
StartScript = time ()

#Функция расчёта символов в числе (разрядность)
def Digit (Number):
   int (Number)
   Counter = 0
   while Number > 9:
      Counter += 1
      Number /= 10
      int (Number)
   return Counter

#Функция расчёта времени работы скрипта
def TimeScriptWork ():
   Minutes = Hours = Days = 0					#Зададим переменные для подсчёта времени.
   Seconds = int (time () - StartScript)			#Вычислим время работы в секундах.
   SecondsLiter = MinutesLiter = HoursLiter = DaysLiter = ''	#Добавление цифры "0" перед числом, если оно меньше 9
   
   while Seconds > 60:						#Если прошло больше 60 секунд:
      Seconds -= 60 						#Отнимаем 60 секунд от общего времени выполнения
      Minutes += 1						#и прибавляе одну минуту.
      if Minutes > 60:						#Если прошло больше 60 минут:
         Minutes = 0						#Обнуляем минуты
         Hours += 1						#и прибавляем один час.
      if Hours > 24:						#Если прошло больше 24 часов:
         Hours = 0						#Обнуляем часы
         Days += 1						#и прибывляе один день.
   if Seconds < 10:						#Если секунд меньше 9,
      SecondsLiter = '0'					#добавляем "0" спереди.
   if Minutes < 10:						#Если минут меньше 9, 
      MinutesLiter = '0'					#добавляем "0" спереди.
   if Hours < 10:						#Если часов меньше 9,
      HoursLiter = '0'						#добавляем "0" спереди.
   if Days < 10:						#Если дней меньше 9,
      DaysLiter = '0'						#добавляем "0" спереди.
   Result = (DaysLiter + str (Days) + ' Дней ' 
            + HoursLiter + str (Hours) + ':'
            + MinutesLiter + str (Minutes) + ':'
            + SecondsLiter + str (Seconds))
   return Result

#Приветствие
print ('\n')
print ('Скрипт CodeForC2000(C2000M) ver.',CodeForC2000Version, sep = '')
print ('Реализована на языке программирования Python v.3.5.1')
print ('Начало работы скрипта: ',strftime("%d %B %Y, %H:%M:%S", localtime()), sep = '')
print ('---------------------------------------------------')
print ('| Порядковый  |    Номер    |         Код         |')
print ('|    номер    |   перебора  |                     |')
print ('---------------------------------------------------')
#       | 10000000000 | 10000000000 | 0-1-2-3-4-5-6-7-8-9 | Пример вывода результата работы
#       | 10000000000 | 10000000000 | 0-1 2-3 4-5 6-7 8-9 | Пример вывода результата работы
#       --------------Выполнено на 000.001%---------------- Пример выводы хода работы
#	--------Время выполнения: 00 дней 01:10:45--------- Пример вывода хода работы

#Входные данные, которые можно менять
#------------------------------------
#Выводить на экран прогресс выполнения скрипта по 0.001%
PercentRate = 0.001
#Создадим список Number с цифрами
Numerals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Рассчётные переменные
#---------------------
#Порядковый номер
SerialNumber = 1 
#Номер по перебору
SortingNumber = 1
#Величина измерения процентов (в количестве переборов)
Percent = len (Numerals) ** len (Numerals) / int (100 / PercentRate)
#Процент выполнения скрипта
PercentComplete = 0
#Определяем, сколько цифр после запятой нужно выводить при печати
PercentDigit = '{0:.' + str (Digit (1 / PercentRate)) + 'f}'

#Начнём цикл перебора списка с цифрами PotCX
#где PotCX (сокращение от Part of the Code aka 'часть кода') и X = 1 ... 10
for PotC1 in Numerals:
   for PotC2 in Numerals:
      for PotC3 in Numerals:
         for PotC4 in Numerals:
            for PotC5 in Numerals:
               for PotC6 in Numerals:
                  for PotC7 in Numerals:
                     for PotC8 in Numerals:
                        for PotC9 in Numerals:
                           for PotC10 in Numerals:

                              FullCode = [PotC1, PotC2, PotC3, PotC4, PotC5, PotC6, PotC7, PotC8, PotC9, PotC10]	#Собираем код в множество
                              Counter = 10										#Индекс проверочной цифры 
                              Coincident = 0										#Индикатор совпадения
                              
                              while Counter != 0:									#Цикл перебора проверочной цифры
                                 MatchCounter = Counter - 1								#Индекс проверяемой цифры 
                                 while MatchCounter != 0:								#Цикл перебора проверяемых цифр
                                    if FullCode[Counter - 1] == FullCode[MatchCounter - 1]:                             #Если совпадение,
                                       Coincident = 1									#взводим флаг индикации 
                                       break										#и выходим из цикла (производительность up)
                                    MatchCounter -= 1
                                 if Coincident:										#Если совпадают две цифры, остальное
                                    break										#проверять не надо (производительность up)
                                 Counter -= 1
                              
                              if not Coincident:									#Если совпадений не найдено
                                 print ('|' + (11 - Digit (SerialNumber)) * ' ',SerialNumber,				#Выводим отформатированный результат
                                        ' |' + (11 - Digit (SortingNumber)) * ' ',SortingNumber,
                                        ' | ',FullCode[0],'-',FullCode[1],'-',FullCode[2],'-',
                                        FullCode[3],'-',FullCode[4],'-',FullCode[5],'-',FullCode[6],'-',
                                        FullCode[7],'-',FullCode[8],'-',FullCode[9],' |', sep = '')
                                 SerialNumber += 1									#Повышаем порядковый номер для следующего кода
                              
                              SortingNumber += 1									#Повышаем номер по перебору

                              if SortingNumber > (Percent * int (PercentComplete / PercentRate)):			#Если количество переборов превышает некий
                                 PercentComplete += PercentRate								#порог, то увеличиваем процент выполнения
                                 print (15 * '-','Выполнено на ' + PercentDigit.format (PercentComplete)		#Выводим результат с форматированием
                                       ,'%',Digit (PercentComplete) * '-',17 * '-', sep = '')
                                 print (9 * '-','Время выполнения: ',TimeScriptWork (),8 * '-', sep = '')	#Выводим время выполнения.
#Окончание работы
StopScript = time ()

#Выводим времени окончания
print ('---------------------------------------------------')
print ('Окончания работы скрипта: ',strftime("%d %B %Y, %H:%M:%S", localtime()))
