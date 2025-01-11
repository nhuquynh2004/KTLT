import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ui')))
from PyQt6.QtWidgets import QApplication,QMainWindow
from ui.MainWindow33Ext import MaiWindow33Ext

app=QApplication([])
mainWindow=QMainWindow()
myui=MaiWindow33Ext()
myui.setupUi(mainWindow)
myui.showWindow()
app.exec()