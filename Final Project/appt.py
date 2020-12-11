from Scheduler_Exceptions import day_range, time_range

class appt:
    def __init__(self, month, day, time, duration, am_or_pm, subject):
        try:
            val = int(month)
            val = int(day)
            val = int(time)
            val = int(duration)
        except ValueError:
            raise ValueError
        if str(am_or_pm).isalpha() == False:
            raise ValueError
        if not 1 <= month <= 12:
            raise ValueError
        months = [9,4,6,11]
        if month in months and day > 30:
            raise day_range
        if not 1 <= day <= 31:
            raise ValueError
        times = [1,2,3,4,5,8,9,10,11,12]
        if not time in times:
            raise time_range



        self.month = month
        self.day = int(day)
        self.time = int(time)
        self.duration = duration
        self.am_or_pm = am_or_pm
        self.subject = subject

    def __repr__(self):
        return 'Month'+ self.month + 'Day'+  str(self.day) + 'Time' + str(self.time) + self.am_or_pm + 'Duration' + self.duration

    def __str__(self):
        return 'Month' + self.month + 'Day' + str(self.day) + 'Time'+ str(self.time) + self.am_or_pm + 'Duration'+ self.duration
