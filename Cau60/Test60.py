from PyQt6.QtWidgets import QApplication, QMainWindow
from MainWindow60Ext import MainWindow60Ext

app=QApplication([])
mainwindow=QMainWindow()
ui=MainWindow60Ext()
ui.setupUi(mainwindow)
ui.signalsAndslots()
mainwindow.show()
app.exec()
