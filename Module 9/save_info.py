import calendar
import datetime


def save_info(Edate,Etime,Eam,Epm):
    date = Edate
    time = Etime
    time_sec= ""
    if Eam:
        time_sec = "AM"
    else:
        time_sec = "PM"
cal = calendar.Calendar()
i=1
year_list_team1 = []
booked_dict = []
booking = "Team 1"
c = datetime.datetime(2020, 12, 10)
c = c.strftime('%Y-%m-%d')
for i in range(1, 13):
    for d in [x for x in cal.itermonthdates(2020, i) if x.month == i]:
        year_list_team1.append(str(d))

if str(c) in year_list_team1:
    year_list_team1.remove(c)
    booked_dict.append("Date: " + c + " " + "Team: " + booking)



for b in range(1, len(year_list_team1)):
    print(year_list_team1[b])
print(booked_dict)

