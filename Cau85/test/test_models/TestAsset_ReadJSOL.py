from Cau85.libs.JsonFileFactory import JsonFileFactory
from Cau85.models.Asset import Asset

jff=JsonFileFactory()
filename= "../../dataset/assets.json"
assets=jff.read_data(filename,Asset)
print("DS Tài sản sau khi đọc file: ")
for a in assets:
    print(a)