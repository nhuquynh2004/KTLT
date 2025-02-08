from PyQt6.QtWidgets import QApplication, QMainWindow
from MainWindow59Ext import MainWindow59Ext

app = QApplication([])
mainwindow = QMainWindow()
ui = MainWindow59Ext()
ui.setupUi(mainwindow)
mainwindow.show()
ui.signalsAndslots()
app.exec()
