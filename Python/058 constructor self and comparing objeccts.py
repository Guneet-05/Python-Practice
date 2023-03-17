class Student:    
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
    
    def printData(self):
        print("Name =",self.name,"Roll No =",self.rollNo)
    
    def compare(self,other):
        if self.name==other.name and self.rollNo==other.rollNo:
            return True
        else:
            return False

s1 = Student("Guneet",14)
s2 = Student("Guneet",14)
print(id(s1))
print(id(s2))

print(s1.compare(s2))