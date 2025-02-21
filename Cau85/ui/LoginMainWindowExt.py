from PyQt6.QtWidgets import QMessageBox, QMainWindow

from Cau85.libs.DataCollector import DataCollector
from Cau85.ui.LoginMainWindow import Ui_MainWindow
from Cau85.ui.MainWindow85Ext import MainWindow85Ext


class LoginMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSingnalsAndSlots()
    def showWindow(self):
        self.MainWindow.show()
    def setupSingnalsAndSlots(self):
        self.pushButtonLogin.clicked.connect(self.process_login)
    def process_login(self):
        dc = DataCollector()
        uid=self.lineEditUsername.text()
        pwd=self.lineEditPassword.text()
        emp=dc.login(uid,pwd)
        if emp!=None:
            self.MainWindow.close()
            self.mainwindow=QMainWindow()
            self.myui=MainWindow85Ext()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
        else:
            self.msg=QMessageBox(self.MainWindow)
            self.msg.setText("Đăng nhập thất bại")
            self.msg.exec()