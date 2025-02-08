from PyQt6.QtWidgets import QApplication,QMainWindow
from MainWindow39Ext import MainWindow39Ext

app = QApplication([])
MainWindow = QMainWindow()
ui = MainWindow39Ext()
ui.setupUi(MainWindow)
ui.showWindow()
app.exec()