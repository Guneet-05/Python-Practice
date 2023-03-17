class Student:
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
        self.laptop = self.Laptop()
    
    def show(self):
        print("Name =",self.name,"Roll No =",self.rollNo)
        print("Student's Laptop details are",end=" ")
        self.Laptop.show(self.laptop) 

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.processor = 'i5'
            self.ram = 8

        def show(self):
            print("Brand =",self.brand,"CPU =",self.processor,"RAM =",self.ram)     

s1 = Student("Guneet",14)
s2 = Student("Yash",15)

lap1 = s1.laptop
lap2 = s2.laptop
s1.show()
s2.show()

lap = Student.Laptop()
