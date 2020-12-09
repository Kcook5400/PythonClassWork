import operator

from appt import appt

class calendar:
    def __init__(self):
        self.appointment_list = []
    def add_appt(self, appt):
        print("Hiya")
        self.appointment_list.append(appt)
    def remove_appt(self, appt):
        self.remove_appt(appt)
    def display_appt(self):
        self.appointment_list = sorted(self.appointment_list, key = operator.attrgetter('month', 'day', 'time'))
        print(self.appointment_list)