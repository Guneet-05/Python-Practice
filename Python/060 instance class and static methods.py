# In case of variables, class and static meant the same
# However, this is not the case in methods
# So, class and static methods are different

class Student:
    school = "GUNEET"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # an instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    # use cls for class methods
    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is a Student Class. This is a static method")

s1 = Student(34,47,32)
s2 = Student(89,32,12)
print(s1.avg())
print(s2.avg())

# instance methods are of 2 types -> accessors and mutators
# Accessors -> If we only want to fetch the values of the variables (getters)
# Mutators -> If we want to modify the values (setters)

print(Student.getSchool())
Student.info()