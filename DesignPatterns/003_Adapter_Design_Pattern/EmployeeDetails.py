# It provides the details of the employees
class EmployeeDetails:
    def getEmployees(self):
        emps = []
        # This data assume we are getting from the data base
        # Here we are filling the list ourselves
        emps.append("1|ABC|SDE1|9873307173")
        emps.append("2|DEF|SDE2|9876543210")
        emps.append("3|GHI|QA|1234567890")
        emps.append("4|JKL|HR|1234556789")
        # ID | NAME | POSITION | Phone No.

        return emps