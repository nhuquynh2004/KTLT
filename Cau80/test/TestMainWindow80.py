from PyQt6.QtWidgets import QApplication, QMainWindow

from Cau80.ui.MainWindow80Ext import MainWindow80Ext

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow80Ext()
myui.setupUi(mainwindow)
mainwindow.show()
app.exec()