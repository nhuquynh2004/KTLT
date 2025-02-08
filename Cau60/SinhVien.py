from datetime import datetime
class SinhVien:
    def __init__(self,mssv:str,hoten:str,ngaysinh:datetime):
        self.mssv:str=mssv
        self.hoten:str=hoten
        self.ngaysinh:datetime=ngaysinh
    def ho_ten(self):
        name=self.hoten.split(' ')
        ho=name[0]
        ten=name[-1]
        return ho, ten
    def tuoi(self):
        hnay=datetime.today()
        tuoi=(hnay.year-self.ngaysinh.year)
        if (hnay.month,hnay.day) < (self.ngaysinh.month,self.ngaysinh.day):
            tuoi=tuoi-1
        return tuoi
