from Cau85.libs.JsonFileFactory import JsonFileFactory
from Cau85.models.Employee import Employee

jff=JsonFileFactory()
filename= "../../dataset/employees.json"
employees=jff.read_data(filename,Employee)
print("DS Employee sau khi đọc file: ")
for e in employees:
    print(e)