from Danhmuc import Danhmuc
from Sanpham import Sanpham

class Khohang:
    def __init__(self):
        self.database=[]
    def add_danhmuc(self,dm):
        self.database.append(dm)
    def fake_data(self):
        dm1=Danhmuc('DM1','Laptop')
        dm2=Danhmuc('DM2','Điện thoại')
        dm3=Danhmuc('DM3','Tivi')

        self.add_danhmuc(dm1)
        self.add_danhmuc(dm2)
        self.add_danhmuc(dm3)

        dm1.add_product(Sanpham('SP1','DELL 113',1100,'TQ'))
        dm1.add_product(Sanpham('SP2','LG 114',800,'TQ'))
        dm1.add_product(Sanpham('SP3','Samsung 10',1100,'HQ'))
        dm2.add_product(Sanpham('SP4','Android 9',1000,'VN'))
        dm2.add_product(Sanpham('SP5','Apple 16',2000,'Mỹ'))
        dm3.add_product((Sanpham('SP6','TV Đại Việt',1500,'VN')))

    def xuat_ds_danhmuc(self):
        for dm in self.database:
            print('-'*40)
            print(dm)
            print('Gồm có: ')
            for sp in dm.list_product:
                print(sp)
    
    def loc_sp_xuatxu (self,xuatxu):
        list_sp=[]
        for dm in self.database:
            for sp in dm.list_product:
                if sp.xuatxu==xuatxu:
                    list_sp.append(sp)
        return list_sp