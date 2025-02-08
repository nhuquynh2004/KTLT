from Danhmuc import Danhmuc
from Sanpham import Sanpham

kho_hang=[]
dm1=Danhmuc('DM1','Laptop')
dm2=Danhmuc('DM2','Điện thoại')
dm3=Danhmuc('DM3','Tivi')
kho_hang.extend([dm1,dm2,dm3])
print('Ds danh mục sp trong kho hàng: ')
for dm in kho_hang:
    print(dm)
dm1.add_product(Sanpham('SP1','DELL 113',1100,'TQ'))
dm1.add_product(Sanpham('SP2','LG 114',800,'TQ'))
dm1.add_product(Sanpham('SP3','Samsung 10',1100,'HQ'))

dm2.add_product(Sanpham('SP4','Android 9',1000,'VN'))
dm2.add_product(Sanpham('SP5','Apple 16',2000,'Mỹ'))

dm3.add_product((Sanpham('SP6','TV Đại Việt',1500,'VN')))

print('*'*40)
print('Sp phân loại theo danh mục')
for dm in kho_hang:
    print('-'*40)
    print(dm)
    print('Gồm có: ')
    for sp in dm.list_product:
        print(sp)