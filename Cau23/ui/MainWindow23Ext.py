from PyQt6.QtWidgets import QMessageBox
from MainWindow23 import Ui_MainWindow

class MainWindow23Ext(Ui_MainWindow):
    def __init__(self):
        self.sokhachhang = 0
        self.soluongmua = 0
        self.sosv = 0
        self.soluongmuasv = 0
    def checkname(self):
        dlg=QMessageBox(self.MainWindow)
        dlg.setWindowTitle('Tên đâu?')
        dlg.setText('Thiếu tên KH kìa!!!')
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons=QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        dlg.button(QMessageBox.StandardButton.Yes).setText("Sorry, để tui nhập liền")
        dlg.button(QMessageBox.StandardButton.No).setText("Hong nhập đấy thì sao")
        if dlg.exec()==QMessageBox.StandardButton.No: exit() #Hong nhập thì exit cho mất hết dữ liệu lun!
        else: pass #Cho cơ hội nhập lại
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()
    def signalsandslots(self):
        self.pushButtonBanmoi.clicked.connect(self.banmoi)
        self.pushButtonThongke.clicked.connect(self.thongke)
        self.pushButtonTinh.clicked.connect(self.tinhtien)
    def banmoi(self):
        self.lineEditSoluong.setText('')
        self.lineEditTenKH.setText('')
        self.lineEditThanhtien.setText('')
        self.checkBoxKHlaSV.setChecked(False)
        self.lineEditTenKH.setFocus()
    def tinhtien(self):
        name_check=str.strip(self.lineEditTenKH.text())
        if name_check == '': self.checkname()
        else: 
            soluong=int(self.lineEditSoluong.text())
            thanhtien=soluong*20000
            if self.checkBoxKHlaSV.isChecked()==True:
                thanhtien=thanhtien*0.95
                self.sosv=self.sosv + 1
                self.soluongmuasv=self.soluongmuasv+soluong
            else:
                self.sokhachhang=self.sokhachhang + 1
                self.soluongmua=self.soluongmua+soluong
            self.lineEditThanhtien.setText(str(int(thanhtien)))
    def thongke(self):
        self.lineEditTongsoKH.setText(str(self.sokhachhang))
        self.lineEditTongsoKHlaSV.setText(str(self.sosv))
        self.lineEditTongdoanhthu.setText(str(int(self.sokhachhang*self.soluongmua*20000+self.sosv*self.soluongmuasv*20000*0.95)))