class Sanpham:
    def __init__(self,id,name,price,origin,in_stock):
        self.id=id
        self.name=name
        self.price=price
        self.origin=origin
        self.in_stock=in_stock
    def __str__(self):
        return f'{self.ma}\t{self.ten}\t{self.gia}\t{self.xuatxu}'