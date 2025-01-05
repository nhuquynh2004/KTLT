from PyQt6.QtWidgets import QApplication, QMainWindow

from Bai5Ext import Bai5Ext

app=QApplication([])
qMainWindow=QMainWindow()
myWindow=Bai5Ext()
myWindow.setupUi(qMainWindow)
myWindow.processSignalAndSlot()
qMainWindow.show()
app.exec()