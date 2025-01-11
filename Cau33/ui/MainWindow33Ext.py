from PyQt6.QtWidgets import QMessageBox
from MainWindow33 import Ui_MainWindow
import random

class MaiWindow33Ext(Ui_MainWindow):
    def __init__(self):
        self.arr_int=None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.SignalsAndSlots()
    def showWindow(self):
        self.MainWindow.show()
    def SignalsAndSlots(self):
        self.pushButtonThoat.clicked.connect(self.thoat)
        self.pushButtonXuatngaunhien.clicked.connect(self.ngaunhien)
        self.pushButtonTonggiatri.clicked.connect(self.tongmang)
        self.pushButtonSophantule.clicked.connect(self.demptle)
        self.pushButtonTonggiatriptule.clicked.connect(self.tongptle)
        self.pushButtonTimptunhonhat.clicked.connect(self.ptnhonhat)
        self.pushButtonTangmoiptulen2.clicked.connect(self.tangmoiptlen2)
        self.pushButtonSapmangtang.clicked.connect(self.sapmangtang)
        self.pushButtonSapmanggiam.clicked.connect(self.sapmanggiam)
    def thoat(self):
        dlg=QMessageBox(self.MainWindow)
        dlg.setWindowTitle('Xác nhận thoát')
        dlg.setText('Ê... muốn thoát hả?')
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons=QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        if dlg.exec()==QMessageBox.StandardButton.Yes: exit() #self.MainWindow.close()
        else: pass
    def ngaunhien(self):
        global n, Manggoc
        n=10
        Manggoc=[] 
        def phantungaunhien():
            Phantu = random.randint(0,100)
            x = Phantu in Manggoc
            if x == True: phantungaunhien()
            else: 
                Manggoc.append(Phantu)
        for i in range (n):
            phantungaunhien()
        printmang=str()
        for j in range (n):
            printmang=printmang+f'{Manggoc[j]}   '
        self.lineEditManggoc.setText(printmang)
    def tongmang(self):
        s=0
        for j in range(n):
            s+=Manggoc[j]
        self.lineEditKetqua.setText(f'Tổng mảng = {s}')
    def demptle(self):
        s=0
        for j in range(n):
            if Manggoc[j]%2!=0: s+=1
        self.lineEditKetqua.setText(f'Số phần tử lẻ = {s}')
    def tongptle(self):
        s=0
        for j in range(n):
            if Manggoc[j]%2!=0: s+=Manggoc[j]
        self.lineEditKetqua.setText(f'Số phần tử lẻ = {s}')
    def ptnhonhat(self):
        min=Manggoc[0]
        for j in range(1,n):
            if Manggoc[j]<min: min=Manggoc[j]
        self.lineEditKetqua.setText(f'Phần tử nhỏ nhất = {min}')
    def tangmoiptlen2(self):
        Manggoctemp=Manggoc.copy()
        for j in range(n):
            Manggoctemp[j]=Manggoctemp[j]+2
        printmang=str()
        for k in range(n):
            printmang=printmang+f'{Manggoctemp[k]}   '
        self.lineEditKetqua.setText(printmang)
    def sapmangtang(self):
        for j in range(n):
            for k in range(j+1,n):
                if Manggoc[k]<Manggoc[j]:
                    temp=Manggoc[j]
                    Manggoc[j]=Manggoc[k]
                    Manggoc[k]=temp
        printmang=str()
        for l in range (n):
            printmang=printmang+f'{Manggoc[l]}   '
        self.lineEditKetqua.setText(printmang)
    def sapmanggiam(self):
        for j in range(n):
            for k in range(j+1,n):
                if Manggoc[k]>Manggoc[j]:
                    temp=Manggoc[j]
                    Manggoc[j]=Manggoc[k]
                    Manggoc[k]=temp
        printmang=str()
        for l in range (n):
            printmang=printmang+f'{Manggoc[l]}   '
        self.lineEditKetqua.setText(printmang)

    
        
