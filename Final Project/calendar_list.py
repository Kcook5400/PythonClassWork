import operator

from easygui import msgbox

from appt import appt

class calendar:
    def __init__(self):
        self.appointment_list = []
    def add_appt(self, appt):
        for x in self.appointment_list:
            if appt.month == x.month:
                if appt.day == x.day:
                    if appt.time == x.time:
                        if appt.am_or_pm == x.am_or_pm:
                            msgbox("Appointment already exists!")
                            return


        self.appointment_list.append(appt)
    def remove_appt(self, appt):
        if not self.appointment_list:
            msgbox("No appointments exist")
            return
        for x in self.appointment_list:
            if appt.month == x.month:
                if appt.day == x.day:
                    if appt.time == x.time:
                        if appt.am_or_pm == x.am_or_pm:
                            self.appointment_list.remove(x)
                            return
        msgbox("Appointment doesn't exist")
    def display_appt(self):
        self.appointment_list = sorted(self.appointment_list, key = operator.attrgetter('month', 'day', 'time'))
        s = []
        for x in self.appointment_list:
            s.append("Appointment: " + str(x.month) + " " +  str(x.day) + " at " + str(x.time) + x.am_or_pm + " Subject: " + x.subject)
        return s
