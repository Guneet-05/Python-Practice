from PhoneListSource import *
from EmployeeListToPLAdapter import *
from EmployeeDetails import *
from intranet import *

def main():
    employeeDS = EmployeeDetails()
    adapter = EmployeeListToPLAdapter()
    adapter.setEmployeeDS(employeeDS)
    intra = Intranet(adapter)
    intra.printPhoneNumbers()

if __name__=='__main__':
    main()

# SOLID 
# O means Open-Close Principle
# Once a class has been written and tested, it is open for extension and closed for modification 