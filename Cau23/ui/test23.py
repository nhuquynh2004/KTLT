from PyQt6.QtWidgets import QApplication, QMainWindow
from MainWindow23Ext import MainWindow23Ext

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow23Ext()
myui.setupUi(mainwindow)
myui.signalsandslots()
mainwindow.show()
myui.showWindow()
app.exec()