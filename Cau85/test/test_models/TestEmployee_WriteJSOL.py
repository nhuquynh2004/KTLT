from Cau85.libs.JsonFileFactory import JsonFileFactory
from Cau85.models.Employee import Employee

employees=[]
employees.append(Employee("E1","Tèo","teo","123"))
employees.append(Employee("E2","Tí","ti","456"))
employees.append(Employee("E3","Bin","bin","789"))
employees.append(Employee("E4","Bo","bo","JQK"))
employees.append(Employee("E5","Bi","bi","ABC"))
print("DS Employee: ")
for e in employees:
    print(e)
jff=JsonFileFactory()
filename= "../../dataset/employees.json"
jff.write_data(employees,filename)