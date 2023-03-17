# init is just like a constructor
class Student:
    def __init__(self,name,rollNo):
        print("inside the init method")
        self.name = name
        self.rollNo = rollNo
    
    def printData(self):
        print("Name=",self.name,"Roll No=",self.rollNo)

st1 = Student("Guneet",14)
st2 = Student("Yash",15)
st1.printData()
st2.printData()