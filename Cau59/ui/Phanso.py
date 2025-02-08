class Phanso:
    def __init__(self,tu=None,mau=None):
        self.__tu=tu
        self.__mau=mau
    def get_tu(self): return self.__tu
    def set_tu(self,tu): self.__tu=tu
    def get_mau(self): return self.__mau
    def set_mau(self,mau): self.__mau=mau
    tu=property(get_tu,set_tu,'tu')
    mau=property(get_mau,set_mau,'mau')
    def cong(self,ps2):
        tukq = self.__tu*ps2.mau + self.__mau*ps2.tu
        maukq = self.__mau*ps2.mau
        return Phanso(tukq,maukq)
    def tru(self,ps2):
        tukq = self.__tu * ps2.mau - self.__mau * ps2.tu
        maukq = self.__mau * ps2.mau
        return Phanso(tukq,maukq)
    def nhan(self,ps2):
        tukq = self.__tu * ps2.tu
        maukq = self.__mau * ps2.mau
        return Phanso(tukq,maukq)
    def chia(self,ps2):
        tukq = self.__tu * ps2.mau
        maukq = self.__mau * ps2.tu
        return Phanso(tukq,maukq)
    @staticmethod
    def ucln(a, b):  # Hàm tính ƯCLN của tử và mẫu số
        while a != b:
            if a > b: a -= b
            else: b -= a
        return a
    def rutgon(self,tukq,maukq):  # Hàm tính phân số rút gọn
        uc = Phanso.ucln(abs(tukq),abs(maukq))
        return tukq // uc, maukq // uc

