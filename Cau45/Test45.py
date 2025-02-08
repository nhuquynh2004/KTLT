from PyQt6.QtWidgets import QApplication, QMainWindow
from MainWindow45Ext import MainWindow45Ext

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow45Ext()
myui.setupUi(mainwindow)
myui.signalsAndslots()
mainwindow.show()
app.exec()