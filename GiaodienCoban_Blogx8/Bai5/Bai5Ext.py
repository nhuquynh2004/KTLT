from PyQt6.QtWidgets import QMessageBox

from Bai5 import Ui_MainWindow

class Bai5Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def processSignalAndSlot(self):
        self.pushButtonExit.clicked.connect(self.processExit)
        self.pushButtonVisitBlog.clicked.connect(self.openMyBlog)
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