import calendar
import datetime

def save_info(Edate,Etime,Eam,Epm):
    date=Edate
    time=Etime
    time_sec= ""
    if Eam:
        time_sec = "AM"
    else:
        time_sec="PM"
cal = calendar.Calendar()
i=1
year_list = []
booking = "Rocky"
c = datetime.datetime(2020, 12, 31)
c= c.strftime('%Y-%m-%d')
for i in range(1, 13):
    for d in [x for x in cal.itermonthdates(2020, i) if x.month == i]:
        year_list.append(d)


for b in range(1, len(year_list)):
    if c == str(year_list[b]):
        year_list.remove(year_list[b])
for b in range(1, len(year_list)):
    print(year_list[b])
