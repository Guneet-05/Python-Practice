from PhoneListSource import *
from EmployeeDetails import *

# data consumer
# wants phone list details but we have employeedetails that sends the details of the employee
class Intranet:
    def __init__(self,phoneListSource) -> None:
        self.__phoneListSource = phoneListSource
    
    def printPhoneNumbers(self):
        phones = self.__phoneListSource.getPhoneNumbers()
        print(phones)