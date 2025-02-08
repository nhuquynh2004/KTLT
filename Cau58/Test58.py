from Cau58 import NhanVien
#Nhập thông tin NV
ho1=input('Họ NV1: ')
ten1=input('Tên NV1: ')
sp1=int(input('Số SP NV1 bán được: '))
ho2=input('Họ NV2: ')
ten2=input('Tên NV2: ')
sp2=int(input('Số SP NV2 bán được: '))

#Tính lương
NhanVien1=NhanVien(ho1,ten1,sp1)
NhanVien2=NhanVien(ho2,ten2,sp2)
luongNV1=NhanVien1.getLuong()
luongNV2=NhanVien2.getLuong()
print(f"Lương NV1: {luongNV1}")
print(f"Lương NV2: {luongNV2}")

#So sánh lương với hàm isHigher()
print(f"Lương NV1 lớn hơn NV2? {NhanVien1.isHigher(NhanVien2)}")

#So sánh lương không dùng hàm isHigher()
if luongNV1 == luongNV2:
    print("Hai NV có lương bằng nhau")
else:
    if luongNV1 > luongNV2:
        higher="Nhân viên 1"
        lower="Nhân viên 2"
    else:
        higher="Nhân viên 2"
        lower="Nhân viên 1"
    print(f"Lương {higher} cao hơn {lower}: {abs(luongNV1-luongNV2)}")


