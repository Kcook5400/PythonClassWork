class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        if lname is None:
            raise ValueError
        self.last_name = lname
        if fname is None:
            raise ValueError
        self.first_name = fname

        self.major = major

        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)