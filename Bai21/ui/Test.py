from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindow21Ext import MainWindow21Ext

app=QApplication([])
Mainwindow=QMainWindow()
myui=MainWindow21Ext()
myui.setupUi(Mainwindow)
myui.tinhtoan()
Mainwindow.showMainWindow()
app.exec()