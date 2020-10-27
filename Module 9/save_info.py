import calendar
import datetime

def save_info(Edate,Etime,Eam,Epm):
    date=Edate
    time=Etime
    time_sec= ""
    if Eam:
        time_sec = "AM"
    else:
        time_sec = "PM"
cal = calendar.Calendar()
i=1
year_list = []
booked_dict = []
booking = "Rocky"
c = datetime.datetime(2020, 12, 10)
c = c.strftime('%Y-%m-%d')
for i in range(1, 13):
    for d in [x for x in cal.itermonthdates(2020, i) if x.month == i]:
        year_list.append(str(d))

if str(c) in year_list:
    year_list.remove(c)
    booked_dict.append(c + " " + booking)



for b in range(1, len(year_list)):
    print(year_list[b])
print(booked_dict)

