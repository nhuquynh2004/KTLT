from CodingPickleFile.FileUtil import FileUtil
from CodingPickleFile.Product import Product

p1=Product(1,"Coca",150)
p2=Product(2,"Pepsi",200)
p3=Product(3,"Redbull",180)
list=[p1,p2,p3]
FileUtil.saveModel(list,"mydata.dat")
