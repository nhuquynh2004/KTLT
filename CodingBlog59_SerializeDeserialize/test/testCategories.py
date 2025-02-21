from CodingBlog59_SerializeDeserialize.models.Categories import Categories
from CodingBlog59_SerializeDeserialize.models.Category import Category
from CodingBlog59_SerializeDeserialize.models.Product import Product
from CodingBlog59_SerializeDeserialize.utils.JsonFactory import JsonFactory

database=Categories()

cate1=Category("C1","Phone")
cate1.add_product(Product("P1","Samsung",500))
cate1.add_product(Product("P2","Iphone",1000))
cate1.add_product(Product("P3","Xiaomi",300))

cate2=Category("C2","Laptop")
cate2.add_product(Product("P4","HP",1200))
cate2.add_product(Product("P5","DELL",900))
cate2.add_product(Product("P6","MacBook",2000))

cate3=Category("C1","TV")
cate3.add_product(Product("P7","Sony",2000))
cate3.add_product(Product("P8","Panasonic",1000))
cate3.add_product(Product("P9","TVC",500))

database.add_cate(cate1)
database.add_cate(cate2)
database.add_cate(cate3)

database.print_all_categories()

print("Obj to json str")
json_data=JsonFactory.parse_json(database)
print(json_data)
print("Recover json str to Obj")
restoreObject=JsonFactory.restore_object(json_data)
restoreObject.print_all_categories()

print("Objs to dataset.json")
JsonFactory.serialize(database,"../assets/database.json")
myobj=JsonFactory.deserialize("../assets/database.json")
print("Deserialize from .json")
myobj.print_all_categories()
