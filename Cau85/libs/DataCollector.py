from Cau85.libs.JsonFileFactory import JsonFileFactory
from Cau85.models.Employee import Employee
from Cau85.models.Asset import Asset
from Cau85.models.Employee_Asset import Employee_Asset

class DataCollector:
    def get_all_employees(self):
        jff = JsonFileFactory()
        filename = "../dataset/employees.json"
        employees = jff.read_data(filename, Employee)
        return employees
    def get_all_assets(self):
        jff = JsonFileFactory()
        filename = "../dataset/assets.json"
        assets = jff.read_data(filename, Asset)
        return assets
    def get_all_employee_asset(self):
        jff = JsonFileFactory()
        filename = "../dataset/employee_asset.json"
        eas = jff.read_data(filename, Employee_Asset)
        return eas
    def login(self,username,password):
        employees=self.get_all_employees()
        for e in employees:
            if e.Username==username and e.Password==password:
                return e
        return None