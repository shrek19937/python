class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def __str__(self):
        return "__str__ " + self.name + " " + self.major

    def __repr__(self):
        return "__repr__ " + self.name + " " + self.major

mike = Student("mike", "numeric analysis")

print(mike)