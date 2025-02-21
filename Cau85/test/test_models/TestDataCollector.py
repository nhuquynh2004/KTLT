from Exercise.Cau85.libs.DataCollector import DataCollector

dc=DataCollector()

#Lấy toàn bộ NV
employees=dc.get_all_employees()
print("DS Employee: ")
for e in employees:
    print(e)

#Lấy toàn bộ TS
assets=dc.get_all_assets()
print("DS Assets: ")
for a in assets:
    print(a)

#Lấy toàn bộ
eas=dc.get_all_employee_asset()
print("DS Phân công Qly Tài sản: ")
for e in eas:
    print(e)

#Test chức năng đăng nhập
uid="teo"
pwd=123
emp=dc.login(uid,pwd)
if emp!=None:
    print("Đăng nhập thành công")
else:
    print("Đăng nhập thất bại")