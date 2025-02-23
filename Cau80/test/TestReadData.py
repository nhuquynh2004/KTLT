from Cau80.libs.TXTFileFactory import TXTFileFactory

products=TXTFileFactory.readData("../dataset/products.txt")
def printProducts(products):
    for product in products:
        print(product)
    print()
printProducts(products)
def sortProducts(products):
    for i in range (len(products)):
        for j in range (len(products)):
            pi=products[i]
            pj=products[j]
            if pi.price < pj.price:
                products[i]=pj
                products[j]=pi
sortProducts(products)
print("Products after price sorting: ")
printProducts(products)