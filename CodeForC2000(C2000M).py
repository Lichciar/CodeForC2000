#!/usr/bin/env python
CodeForC2000Version = '1.4.1'
from time import strftime, localtime, time, gmtime
StartScript = time ()
def Digit (Number):
   int (Number)
   Counter = 0
   while Number > 9:
      Counter += 1
      Number /= 10
      int (Number)
   return Counter
def TimeScriptWork ():
   Minutes = Hours = Days = 0
   Seconds = int (time () - StartScript)
   SecondsLiter = MinutesLiter = HoursLiter = DaysLiter = ''
   while Seconds > 60:
      Seconds -= 60 
      Minutes += 1
      if Minutes > 60:
         Minutes = 0
         Hours += 1
      if Hours > 24:
         Hours = 0
         Days += 1
   if Seconds < 10:
      SecondsLiter = '0'
   if Minutes < 10: 
      MinutesLiter = '0'
   if Hours < 10:
      HoursLiter = '0'
   if Days < 10:
      DaysLiter = '0'
   Result = (DaysLiter + str (Days) + ' Дней '
            + HoursLiter + str (Hours) + ':'
            + MinutesLiter + str (Minutes) + ':'
            + SecondsLiter + str (Seconds))
   return Result
print ('\n')
print ('Скрипт CodeForC2000(C2000M) ver.',CodeForC2000Version, sep = '')
print ('Реализована на языке программирования Python v.3.5.1')
print ('Начало работы скрипта: ',strftime("%d %B %Y, %H:%M:%S", localtime()), sep = '')
print ('---------------------------------------------------')
print ('| Порядковый  |    Номер    |         Код         |')
print ('|    номер    |   перебора  |                     |')
print ('---------------------------------------------------')
PercentRate = 0.001
Numerals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SerialNumber = 1 
SortingNumber = 1
Percent = len (Numerals) ** len (Numerals) / int (100 / PercentRate)
PercentComplete = 0
PercentDigit = '{0:.' + str (Digit (1 / PercentRate)) + 'f}'
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
                              FullCode = [PotC1, PotC2, PotC3, PotC4, PotC5, PotC6, PotC7, PotC8, PotC9, PotC10]
                              Counter = 10								 
                              Coincident = 0								
                              while Counter != 0:						
                                 MatchCounter = Counter - 1				 
                                 while MatchCounter != 0:				
                                    if FullCode[Counter - 1] == FullCode[MatchCounter - 1]:
                                       Coincident = 1					 
                                       break						
                                    MatchCounter -= 1
                                 if Coincident:					
                                    break				
                                 Counter -= 1
                              if not Coincident:								
                                 print ('|' + (11 - Digit (SerialNumber)) * ' ',SerialNumber,		
                                        ' |' + (11 - Digit (SortingNumber)) * ' ',SortingNumber,
                                        ' | ',FullCode[0],'-',FullCode[1],'-',FullCode[2],'-',
                                        FullCode[3],'-',FullCode[4],'-',FullCode[5],'-',FullCode[6],'-',
                                        FullCode[7],'-',FullCode[8],'-',FullCode[9],' |', sep = '')
                                 SerialNumber += 1						
                              SortingNumber += 1						
                              if SortingNumber > (Percent * int (PercentComplete / PercentRate)):
                                 PercentComplete += PercentRate					
                                 print (15 * '-','Выполнено на ' + (2 - Digit (PercentComplete)) * '0' +
                                        PercentDigit.format (PercentComplete)		
                                       ,'%',15 * '-', sep = '')
                                 print (9 * '-','Время выполнения: ',TimeScriptWork (),8 * '-', sep = '')
StopScript = time ()
print ('---------------------------------------------------')
print ('Окончания работы скрипта: ',strftime("%d %B %Y, %H:%M:%S", localtime()))
