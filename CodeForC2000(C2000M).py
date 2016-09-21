#!/usr/bin/env python

# --------------------------- 72 символа -------------------------------
# --------------------------- 79 символов -------------------------------------

"""Задание:

Скрипт расчёта идеальной комбинаций кода для С2000 (С2000М)
Коде должен состоять из 8 цифр, и при этом одна цифра должна
быть задействована лишь единожды.
Начало: 11 декабря 2015 г. 01:44.
Обновлена: 09 сентября 2016 г. 01:02.

"""

# Версия скрипта.  
CodeForC2000Version = '1.4.4'

"""Планирование разработки:

Исправлено в ver.1.4.4:
--------------------
1.Приведено к стандартам PEP8, PEP257.
2.Изменено количество цифр в пароле с 10 на 8 (Ошибка при
  составлении задания).

План работ на ver.1.X:
---------------------
1.Протестировать работу скипта.
2.Протестировать на разных ПК и сохранить время выполнения.

"""

# Подключаем модули (в данном случае - модуль времени).  
from time import strftime, localtime, time, gmtime

# Время начала работы скрипта.  
StartScript = time()

def Digit(Number):
    """Функция расчёта символов в числе (разрядность)."""
    int(Number)
    Counter = 0
    while Number >= 10:
        Counter += 1
        Number /= 10
        int(Number)
    return Counter

def TimeScriptWork():
    """Функция расчёта времени работы скрипта."""
    # Инициализируем переменные.  
    Minutes = Hours = Days = 0
    Seconds = int (time() - StartScript)
    SecondsLiter = MinutesLiter = HoursLiter = DaysLiter = ''
    
    # Механизм превращения "машинных" секунд в удобочитаемый формат  
    # времени.  
    while Seconds > 60:
        Seconds -= 60 
        Minutes += 1
        if Minutes > 60:
            Minutes = 0
            Hours += 1
        if Hours > 24:
            Hours = 0
            Days += 1
     
    # Добавление "0" перед цифрой, для форматированного  
    # вывода времени.  
    if Seconds < 10:
        SecondsLiter = '0'
    if Minutes < 10: 
        MinutesLiter = '0'
    if Hours < 10:
        HoursLiter = '0'
    if Days < 10:
        DaysLiter = '0'
     
    # Сбрка форматированного вывода в единую строку для вывода  
    # на экран.  
    Result = (DaysLiter+str(Days) + ' Дней ' +
              HoursLiter+str(Hours) + ':' +
              MinutesLiter+str(Minutes) + ':' +
              SecondsLiter+str(Seconds))
    return Result

def OutputMessage(Message):
    """Функция вывода сообщений в файл и на экран."""
    OutputFileName = ('LogFileCodeForC2000(' +
                      CodeForC2000Version + ').log')
    OutputFile = open(OutputFileName, 'a')
    OutputFile.write(Message + '\n')
    print(Message)
    OutputFile.close()

def OutputResult():
    """Функция вывода подходящего по заданию пароля."""
    OutputMessage('|  ' +
                  (8-Digit(SerialNumber))*' ' +
                  str(SerialNumber) +
                  '  |  ' +
                  (8-Digit(SortingNumber))*' ' +
                  str(SortingNumber) +
                  '  | ' +
                  str(FullCode[0]) + '-' +
                  str(FullCode[1]) + '-' +
                  str(FullCode[2]) + '-' +
                  str(FullCode[3]) + '-' +
                  str(FullCode[4]) + '-' +
                  str(FullCode[5]) + '-' +
                  str(FullCode[6]) + '-' +
                  str(FullCode[7]) + ' |')

def OutputPercent():
    """Функция вывода процента выполнения программы."""
    print(13*'-', 'Выполнено на ' + (2-Digit(PercentComplete))*'0' +
          PercentDigit.format(PercentComplete), '%', 13*'-', sep = '')
    print(6*'-', 'Время выполнения: ', TimeScriptWork(),
          7*'-', sep = '')
    
# Основная программа начинается с приветствия  
OutputMessage('\n')
OutputMessage('Скрипт CodeForC2000(C2000M) ver.' + CodeForC2000Version)
OutputMessage('Реализована на языке программирования Python v.3.5.1')
OutputMessage('Начало работы скрипта: ' +
               strftime("%d %B %Y, %H:%M:%S", localtime()))
OutputMessage('-----------------------------------------------')
OutputMessage('| Порядковый  |    Номер    |       Код       |')
OutputMessage('|    номер    |   перебора  |                 |')
OutputMessage('-----------------------------------------------')
"""Пример вывода работы
               |  100000000  |  100000000  | 0-1-2-3-4-5-6-7 |
               |  100000000  |  100000000  | 0-1 2-3 4-5 6-7 |
               -------------Выполнено на 000.001%-------------
               ------Время выполнения: 00 дней 01:10:45-------

"""

# Входные данные, которые можно менять.  
# -------------------------------------   
# Выводить на экран прогресс выполнения скрипта по 0.001%.  
PercentRate = 0.001
# Создадим список Number с цифрами.  
Numerals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Количество цифр в пароле.  
PasswordLen = 8

# Рассчётные переменные.  
# ----------------------  
# Порядковый номер.  
SerialNumber = 1 
# Номер по перебору.  
SortingNumber = 1
# Величина измерения процентов (в количестве переборов).  
Percent = len(Numerals)**PasswordLen / int(100/PercentRate)
# Процент выполнения скрипта.  
PercentComplete = 0
# Определяем, сколько цифр после запятой нужно выводить при печати.  
PercentDigit = '{0:.' + str(Digit(1/PercentRate)) + 'f}'

# Начнём цикл перебора списка с цифрами PotCX,  
# где PotCX (сокращение от Part of the Code aka 'часть кода')  
# и X = 1 ... 8.  
for PotC1 in Numerals:
    for PotC2 in Numerals:
        for PotC3 in Numerals:
            for PotC4 in Numerals:
                for PotC5 in Numerals:
                    for PotC6 in Numerals:
                        for PotC7 in Numerals:
                            for PotC8 in Numerals:
                                # Инициализируем данные для начала  
                                # расчёта.   
                                FullCode = [PotC1, PotC2, PotC3, PotC4,
                                            PotC5, PotC6, PotC7, PotC8]
                                Counter = 8
                                Coincident = 0

                                # Начинаем перебор цифр.  
                                while Counter != 0:
                                    MatchCounter = Counter - 1
                                     
                                    # Сравниваем перебираемую цифру с  
                                    # другими цифрами в пароле.   
                                    while MatchCounter != 0:
                                        if (FullCode[Counter - 1] ==
                                            FullCode[MatchCounter - 1]):
                                            Coincident = 1
                                            break
                                        MatchCounter -= 1
                                     
                                    # Если совпадают хотя бы 2  
                                    # цифры, остальное можно  
                                    # не проверять.   
                                    if Coincident:
                                        break
                                     
                                    Counter -= 1
                                     
                                # Если совпадений не найдено, то  
                                # выводим результат.   
                                if not Coincident:
                                    OutputResult()
                                    SerialNumber += 1
                                     
                                SortingNumber += 1
                                     
                                # Если количество перебранных  
                                # комбинаций паролей превышает  
                                # порог PercentRate, выводим  
                                # отчёт.  
                                if (SortingNumber >
                                    (Percent *
                                     int(PercentComplete/
                                         PercentRate))):
                                    PercentComplete += PercentRate
                                    OutputPercent()

#Окончание работы
StopScript = time()

#Выводим времени окончания
OutputMessage ('-----------------------------------------------')
OutputMessage ('Окончания работы скрипта: ' +
               strftime("%d %B %Y, %H:%M:%S", localtime()))
