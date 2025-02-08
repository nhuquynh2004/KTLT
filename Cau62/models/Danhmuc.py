class Danhmuc:
    def __init__(self,id=None,name=None):
        self.id=id
        self.name=name
        self.list_product={}#lưu ds sp
    def __str__(self):
        return f'{self.ma}\t{self.ten}'
    def add_product(self,p):
        self.list_product.append(p)
    def print_product(self):
        for p in self.list_product:
            print(p)
    