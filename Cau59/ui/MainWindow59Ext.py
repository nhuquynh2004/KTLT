from MainWindow59 import Ui_MainWindow
from Phanso import Phanso

class MainWindow59Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def signalsAndslots(self):
        self.pushButtonCong.clicked.connect(self.showAnswerCong)
        self.pushButtonTru.clicked.connect(self.showAnswerTru)
        self.pushButtonNhan.clicked.connect(self.showAnswerNhan)
        self.pushButtonChia.clicked.connect(self.showAnswerChia)
    def getPS(self):
        tu1=int(self.lineEditTu1.text())
        tu2=int(self.lineEditTu2.text())
        mau1=int(self.lineEditMau1.text())
        mau2=int(self.lineEditMau2.text())
        ps1 = Phanso(tu1, mau1)
        ps2 = Phanso(tu2, mau2)
        return ps1,ps2
    def showAnswerCong(self):
        ps1,ps2=self.getPS()
        kq = ps1.cong(ps2)
        tukq,maukq=kq.rutgon(kq.tu,kq.mau)
        self.lineEditTuKq.setText(str(tukq))
        self.lineEditMauKq.setText(str(maukq))
        self.label_4.setText("+")
    def showAnswerTru(self):
        ps1, ps2 = self.getPS()
        kq = ps1.tru(ps2)
        tukq,maukq=kq.rutgon(kq.tu,kq.mau)
        self.lineEditTuKq.setText(str(tukq))
        self.lineEditMauKq.setText(str(maukq))
        self.label_4.setText("-")
    def showAnswerNhan(self):
        ps1, ps2 = self.getPS()
        kq = ps1.nhan(ps2)
        tukq,maukq=kq.rutgon(kq.tu,kq.mau)
        self.lineEditTuKq.setText(str(tukq))
        self.lineEditMauKq.setText(str(maukq))
        self.label_4.setText("x")
    def showAnswerChia(self):
        ps1, ps2 = self.getPS()
        kq = ps1.chia(ps2)
        tukq,maukq=kq.rutgon(kq.tu,kq.mau)
        self.lineEditTuKq.setText(str(tukq))
        self.lineEditMauKq.setText(str(maukq))
        self.label_4.setText(":")


