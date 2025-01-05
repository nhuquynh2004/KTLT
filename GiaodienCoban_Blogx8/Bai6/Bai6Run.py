from PyQt6.QtWidgets import QApplication, QMainWindow

from Bai6Ext import Bai6Ext

app=QApplication([])
qMainWindow=QMainWindow()
myWindow=Bai6Ext()
myWindow.setupUi(qMainWindow)
myWindow.processSignalAndSlot()
qMainWindow.show()
app.exec()