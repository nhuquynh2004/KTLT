from PyQt6.QtWidgets import QApplication, QMainWindow

from Cau85.ui.MainWindow85Ext import MainWindow85Ext

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow85Ext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()