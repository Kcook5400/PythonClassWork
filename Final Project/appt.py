

class appt:
    def __init__(self, month, day, time, duration, am_or_pm, subject):
        try:
            val = int(month)
            val = int(day)
            val = int(time)
            val = int(duration)
            val = str(am_or_pm)
            val = str(subject)
        except ValueError:
            raise ValueError
        if not 1 <= month <= 12:
            raise ValueError


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
