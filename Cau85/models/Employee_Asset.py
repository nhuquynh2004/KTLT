class Employee_Asset:
    def __init__(self,EmployeeID,AssetID,Role):
        self.EmployeeID=EmployeeID
        self.AssetID=AssetID
        self.Role=Role
    def __str__(self):
        return f"{self.EmployeeID}\t{self.AssetID}\t{self.Role}"