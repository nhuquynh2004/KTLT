def LuuFile(path):
    file=open(path,'w',encoding='utf-8')
    file.writelines("SV001;Trần;1/1/1998\n")
    file.writelines("SV002;Nguyễn;2/1/1998\n")
    file.writelines("SV003;Lê;3/1/1998\n")
    file.close()
LuuFile("csdlsinhvien.txt")