from BTRL_XuLyFile_SanPham.XuLyFile import *

msp=input("Nhập mã SP: ")
tensp=input("Nhập tên SP: ")
dongia=float(input("Nhập giá: "))
line=msp+';'+tensp+";"+str(dongia)

LuuFile("database.txt",line)