import calendar 
from datetime import datetime
now = datetime.now()
age = int(input("Enter your age: "))
yr = int(input('Enter year:'))
mt = int(input("Enter the month: "))
dy = int(input("Enter the day of the month: "))
cal = calendar.weekday(yr,mt,dy)
day = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
print('You were born on',day[cal])
