from MainWindow21 import Ui_Dialog

class MainWindow21Ext(Ui_Dialog):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.thuchien.clicked.connect(self.tinhtoan)
        
    def tinhtoan(self):
        def giaithua(n):
            gt = 1
            for i in range (1,n+1):
                gt=gt*i
            return gt
        def P(n,k):
            return giaithua(n)//giaithua(n-k)
        def C(n,k):
            return giaithua(n)//(giaithua(n-k)*giaithua(k))
        n=int(self.nhapn.text())
        k=int(self.nhapk.text())
        self.ansA.setText(int(P(n,k)))
        self.ansC.setText(int(C(n,k)))
    