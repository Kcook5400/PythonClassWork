"""
PEP: 8
Title: appt
Author: Kevin Cook
Status: Active
Type: Process
Created: 12-12-2020
Post:12-12-2020
History:
"""


from Scheduler_Exceptions import day_range, time_range

class appt:
    def __init__(self, month, day, time, duration, am_or_pm, subject):
        """Creates instance of appt class"""
        months_list = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September",
                       "October", "November", "December"]

        for x in range(1, 12):
            if month in months_list:
                month = x

        """validating month, day, time, and duration variables are ints"""
        try:
            val = int(month)
            val = str(day)
            val = str(time)
            val = str(duration)
        except ValueError:
            raise ValueError
        """validating am_or_pm variable is a str"""
        if str(am_or_pm).isalpha() == False:
            raise ValueError
        """validating month variable is a month"""
        print(month)
        if not 1 <= month <= 31:
            raise ValueError
        """creating months list for validating months with <31 days"""
        months = [9, 4, 6, 11]
        """validating days variable is not >30 in months with only 30 days"""
        if month in months and int(day) > 30:
            raise day_range
        """validating days variable is between 1-31"""
        if not 1 <= int(day) <= 31:
            raise ValueError
        """ creating times list for validating times variable is between 8 and 5"""
        times = [1,2,3,4,5,8,9,10,11,12]
        """validating times variable is on times list"""
        if not int(time) in times:
            raise time_range

        """setting variables"""
        self.month = month
        self.day = int(day)
        self.time = int(time)
        self.duration = duration
        self.am_or_pm = am_or_pm
        self.subject = subject


    def __repr__(self):
        """repr function"""
        return 'Month'+ str(self.month) + 'Day'+ str(self.day) + 'Time' + str(self.time) + str(self.am_or_pm) + 'Duration' + str(self.duration)
    def __str__(self):
        """ str function"""
        return 'Month '+ str(self.month) + ' Day '+ str(self.day) + ' Time ' + str(self.time) + str(self.am_or_pm) + ' Duration ' + str(self.duration)
