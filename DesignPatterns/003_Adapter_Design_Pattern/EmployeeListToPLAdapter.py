from PhoneListSource import *
from EmployeeDetails import *

class EmployeeListToPLAdapter(PhoneListSource):
    
    def __init__(self) -> None:
        self.__employeeDS = None # employeeDS = employee data source
        super().__init__()

    def setEmployeeDS(self,employeeDS):
        self.__employeeDS = employeeDS

    def getPhoneNumbers(self):
        emps = self.__employeeDS.getEmployees()
        phones = []

        for employee in emps:
            parts = employee.split('|')
            phone  = parts[3]
            phones.append(phone)
        
        return phones