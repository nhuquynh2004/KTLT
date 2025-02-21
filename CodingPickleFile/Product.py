class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
    def __str__(self):
        return (str(self.id)+"\t"
                +self.name+"\t"
                +str(self.price))