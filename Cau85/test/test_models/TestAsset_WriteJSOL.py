from Cau85.libs.JsonFileFactory import JsonFileFactory
from Cau85.models.Asset import Asset

assets=[]
assets.append(Asset("TS1","Máy chiếu 1",2017,10))
assets.append(Asset("TS2","Máy chiếu 2",2018,10))
assets.append(Asset("TS3","Máy tính A",2016,10))
assets.append(Asset("TS4","Máy tính B",2020,10))
assets.append(Asset("TS5","Máy lọc nước",2018,10))
assets.append(Asset("TS6","Máy ảnh",2017,10))
print("DS Tài sản: ")
for a in assets:
    print(a)
jff=JsonFileFactory()
filename= "../../dataset/assets.json"
jff.write_data(assets,filename)