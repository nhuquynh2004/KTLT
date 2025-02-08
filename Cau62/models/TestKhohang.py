from Khohang import Khohang

kho_binhduong = Khohang()
kho_binhduong.fake_data()
print('DS sp trong kho Bình Dương')
kho_binhduong.xuat_ds_danhmuc()

lsp=kho_binhduong.loc_sp_xuatxu('TQ')
print('Các sp xuất xứ từ TQ')
for sp in lsp: print(sp)