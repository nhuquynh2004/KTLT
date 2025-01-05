from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QMainWindow


from Bai6_MainWindow import Ui_MainWindow
from Bai6_SecondWindow import SecondWindow

class Bai6Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.secondWindow=None
    def processSignalAndSlot(self):
        self.pushButtonExit.clicked.connect(self.processExit)
        self.pushButtonVisitBlog.clicked.connect(self.openMyBlog)
        self.pushButtonSendName.clicked.connect(self.openSecondWindow)
    def processExit(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Exit Confirmation")
        dlg.setText("Are you sure you want to Exit?")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
        else:
            pass
    def openMyBlog(self):
        import webbrowser
        webbrowser.open('https://tranduythanh.com/')
    def openSecondWindow(self):
        if self.secondWindow==None or self.qmainWindow.isVisible()==False:
            self.qmainWindow = QMainWindow()
            self.secondWindow=SecondWindow(self)
            self.secondWindow.setupUi(self.qmainWindow)
            self.qmainWindow.show()
    
