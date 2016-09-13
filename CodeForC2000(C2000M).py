#!/usr/bin/python

#Програма расчёта идеальной комбинаций кода для С2000 (С2000М)
#В коде должно быть задействовано 10 цифр, и при этом одна цифра должна
#быть задействована лишь единожды.
#Начало: 11 декабря 2015 г. 01:44

#Версия программы
CodeForC2000Version = '1.0'

#Приветствие
print ('\n')
print ('Программа CodeForC2000(C200M) ver.',CodeForC2000Version)
print ('--------------------------------------------------------')
print ('|Порядковый номер|Номер перебора\t\t|Код         |')
print ('--------------------------------------------------------')

#Создадим список Number с цифрами
Numerals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#Порядковый номер
SerialNumber = 1
#Номер по перебору
SortingNumber = 1

#Начнём цикл перебора списка с цифрами PotCX
#где PotCX (сокращение от Part of thr Code aka 'часть кода') и X = 1 ... 10
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

#Проверяем отсутствие одинаковых цифр в коде
#Для этого создаем цикл с перебором всех значений
                              FullCode = [PotC1, PotC2, PotC3, PotC4, PotC5, PotC6, PotC7, PotC8, PotC9, PotC10]
                              Counter = 9
                              Coincident = 0
                              while Counter >= 1:
                                 MatchCounter = 8
                                 if FullCode[Counter] == FullCode[MatchCounter]:
                                    Coincident = 1 
                                 Counter -= 1
                                 MatchCounter -= 1
                              if not Coincident:
                                 SerialNumber += 1 
                                 print ('| ',SerialNumber,'\t| ',SortingNumber,'\t| ',FullCode,' |')
                              SortingNumber += 1
