from datetime import datetime
import calendar

today_to = datetime.today().day
today = calendar.day_name[datetime.today().weekday()]
month = calendar.month_name[datetime.today().month]

print(today, today_to, month, datetime.today().year)
if today == 'Sunday':
    print('Fuck YEAH')
else:
    print('sasi')