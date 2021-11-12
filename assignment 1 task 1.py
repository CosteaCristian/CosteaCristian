###GROUP 13 984165 AND 965396
#we are converting the input directly as a string so then we can substring it
date=str(input('Please enter the date in DD:MM:YYYY format:'))
#converting the day, month and year to integers so we won`t get the operand
#error between two different types of inputs
day=int(date[0:2])
month=int(date[3:5])
year=int(date[6:10])
prev_day=day-1
#For the special cases such as the day entered is the first day of that month
#after the calculation the result would be 0 and there is no such day so the
#previous day becomes the last day of the previous month
#also if the month is also the first it has to become the last month which is 12
#and the year to decrease by 1
#if the date entered is the first day of the 3rd month the prev day becomes 28
#because February has only 28 days
#also if the year is a leap year the last day of February is 29 otherwise is 28
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           bolean=True
       else:
           bolean=False
   else:
       bolean=True
else:
   bolean=False
if prev_day==0:
    month=month-1
    if month==0:
        month=12
        year=year-1
        prev_day=31
    if month==1:
        prev_day=31
    if month==2:
        if bolean==True:
            prev_day=29
        else:
            prev_day=28
    if month==3:
        prev_day=31
    if month==4:
        prev_day=30
    if month==5:
        prev_day=31
    if month==6:
        prev_day=30
    if month==7:
        prev_day=31
    if month==8:
        prev_day=31
    if month==9:
        prev_day=30
    if month==10:
        prev_day=31
    if month==11:
        prev_day=30
    if month==12:
        prev_day=31
print('Yesterday date was:',prev_day,month,year)






