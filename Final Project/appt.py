

class appt:
    def __init__(self, month, day, time, duration, am_or_pm):
        self.month = month
        self.day = day
        self.time = time
        self.duration = duration
        self.am_or_pm = am_or_pm

    def __repr__(self):
        return 'Month'+ self.month + 'Day'+  self.day + 'Time' + self.time + self.am_or_pm + 'Duration' + self.duration

    def __str__(self):
        return 'Month' + self.month + 'Day' + self.day + 'Time'+ self.time + self.am_or_pm + 'Duration'+ self.duration
