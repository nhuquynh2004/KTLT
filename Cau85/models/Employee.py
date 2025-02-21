class Employee:
    def __init__(self,EmployeeID,EmployeeName,Username,Password):
        self.EmployeeID=EmployeeID
        self.EmployeeName=EmployeeName
        self.Username=Username
        self.Password=Password
    def __str__(self):
        return f"{self.EmployeeID}\t{self.EmployeeName}"
