from Cau80.libs.TXTFileFactory import TXTFileFactory
from Cau80.models.Product import Product

print("Input Products")
while True:
    id=input("Input Product ID: ")
    name=input("Input Product Name: ")
    price=input("Input Unit Price: ")
    product=Product(id,name,price)

    TXTFileFactory.writeData("../dataset/products.txt", product)
    ans=input("Continue?(Y/N) ")
    if ans!='Y' or ans!='y':
        break