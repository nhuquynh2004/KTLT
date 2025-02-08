from PyQt6.QtWidgets import QApplication, QMainWindow

from Cau62.ui.MainWindow62Ext import MainWindow62Ext

app=QApplication([])
mainwindow=QMainWindow()
ui=MainWindow62Ext()
ui.setupUi(mainwindow)
mainwindow.show()
ui.setupSignalsAndSlots()
app.exec()