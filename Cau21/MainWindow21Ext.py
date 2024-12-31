from MainWindow21 import Ui_NguyenNhuQuynh_798_TohopChinhhop

class MainWindow21Ext(Ui_NguyenNhuQuynh_798_TohopChinhhop):
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.thuchien.clicked.connect(self.tinhtoan)
        
    def tinhtoan(self):
        def giaithua(n):
            if n==0: return 1
            else:
                return n*giaithua(n-1)
        def P(n,k):
            return giaithua(n)//giaithua(n-k)
        def C(n,k):
            return giaithua(n)//(giaithua(n-k)*giaithua(k))
        n=int(self.nhapN.text())
        k=int(self.nhapK.text())
        ansA=P(n,k)
        ansC=C(n,k)
        self.chinhhopP.setText(str(ansA))
        self.tohopC.setText(str(ansC))
    