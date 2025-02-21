from Chuong4_File.JSOL_File_OOP.JsonFileFactory import JsonFileFactory
from Exercise.Cau85.models.Employee_Asset import Employee_Asset

eas=[]
eas.append(Employee_Asset("E1","TS1","MAIN"))
eas.append(Employee_Asset("E2","TS3","MAIN"))
eas.append(Employee_Asset("E5","TS5","MAIN"))
eas.append(Employee_Asset("E4","TS4","MAIN"))
eas.append(Employee_Asset("E5","TS4","MAIN"))
eas.append(Employee_Asset("E1","TS6","MAIN"))
eas.append(Employee_Asset("E4","TS7","MAIN"))

print("DS Phân công Qly Tài sản: ")
for a in eas:
    print(a)

jff=JsonFileFactory()
filename= "../../dataset/employee_asset.json"
jff.write_data(eas,filename)
