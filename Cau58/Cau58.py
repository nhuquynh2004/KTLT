class NhanVien:
    def __init__(self,ho,ten,sp):
        self.__ho=ho
        self.__ten=ten
        if sp>=0: self.__sp=sp
        else: self.__sp=0
    def get_ho(self):
        return self.__ho
    def get_ten(self):
        return self.__ten
    def get_sp(self):
        return self.__sp
    def set_ho(self,ho):
        self.__ho=ho
        return
    def set_ten(self,ten):
        self.__ten=ten
        return
    def set_sp(self,sp):
        self.__sp=sp
        return
    ho = property(get_ho, set_ho, 'ho')
    ten = property(get_ten, set_ten, 'ten')
    sp = property(get_sp, set_sp, 'sp')

    def getLuong(self):
        heso=[0.5,0.55,0.6,0.65]
        sosp=[1,200,400,600]
        if self.__sp == 0: dongia = 0
        elif self.__sp >= sosp[-1]: dongia = heso[-1]
        else:
            for i in range (len(sosp)-1):
                if sosp[i] <= self.__sp < sosp[i+1]:
                    dongia=heso[i]
                    break
        luong=self.__sp*dongia
        return luong
    def isHigher(self,nv2):
        return self.__sp > nv2.__sp
