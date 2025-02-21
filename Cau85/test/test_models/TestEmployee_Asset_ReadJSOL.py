from Exercise.Cau85.libs.JsonFileFactory import JsonFileFactory
from Exercise.Cau85.models.Employee_Asset import Employee_Asset

jff=JsonFileFactory()
filename= "../../dataset/employee_asset.json"
eas=jff.read_data(filename,Employee_Asset)
print("DS Employee sau khi đọc file: ")
for e in eas:
    print(e)