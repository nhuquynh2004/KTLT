# Form implementation generated from reading ui file 'MainWindow33.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(374, 380)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Ky_thuat_lap_trinh/Exercise/Cau33/images/K24.JPG"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 321, 61))
        self.groupBox.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.groupBox.setObjectName("groupBox")
        self.lineEditManggoc = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditManggoc.setGeometry(QtCore.QRect(10, 20, 301, 31))
        self.lineEditManggoc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditManggoc.setObjectName("lineEditManggoc")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 80, 321, 61))
        self.groupBox_2.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEditKetqua = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditKetqua.setGeometry(QtCore.QRect(10, 20, 301, 31))
        self.lineEditKetqua.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditKetqua.setObjectName("lineEditKetqua")
        self.pushButtonXuatngaunhien = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonXuatngaunhien.setGeometry(QtCore.QRect(20, 150, 141, 21))
        self.pushButtonXuatngaunhien.setObjectName("pushButtonXuatngaunhien")
        self.pushButtonTonggiatri = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonTonggiatri.setGeometry(QtCore.QRect(20, 180, 141, 21))
        self.pushButtonTonggiatri.setObjectName("pushButtonTonggiatri")
        self.pushButtonSophantule = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSophantule.setGeometry(QtCore.QRect(20, 210, 141, 21))
        self.pushButtonSophantule.setObjectName("pushButtonSophantule")
        self.pushButtonTonggiatriptule = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonTonggiatriptule.setGeometry(QtCore.QRect(20, 240, 141, 21))
        self.pushButtonTonggiatriptule.setObjectName("pushButtonTonggiatriptule")
        self.pushButtonSapmangtang = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSapmangtang.setGeometry(QtCore.QRect(200, 210, 141, 21))
        self.pushButtonSapmangtang.setObjectName("pushButtonSapmangtang")
        self.pushButtonSapmanggiam = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSapmanggiam.setGeometry(QtCore.QRect(200, 240, 141, 21))
        self.pushButtonSapmanggiam.setObjectName("pushButtonSapmanggiam")
        self.pushButtonTangmoiptulen2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonTangmoiptulen2.setGeometry(QtCore.QRect(200, 180, 141, 21))
        self.pushButtonTangmoiptulen2.setObjectName("pushButtonTangmoiptulen2")
        self.pushButtonTimptunhonhat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonTimptunhonhat.setGeometry(QtCore.QRect(200, 150, 141, 21))
        self.pushButtonTimptunhonhat.setObjectName("pushButtonTimptunhonhat")
        self.pushButtonThoat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonThoat.setGeometry(QtCore.QRect(130, 270, 101, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:/Ky_thuat_lap_trinh/Exercise/Cau33/images/close.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.pushButtonThoat.setIcon(icon1)
        self.pushButtonThoat.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonThoat.setObjectName("pushButtonThoat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 374, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "N.N.Quỳnh K244060798 - MainWindow 33"))
        self.groupBox.setTitle(_translate("MainWindow", "Mảng gốc:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Kết quả:"))
        self.pushButtonXuatngaunhien.setText(_translate("MainWindow", "Xuất mảng ngẫu nhiên"))
        self.pushButtonTonggiatri.setText(_translate("MainWindow", "Tính tổng giá trị mảng"))
        self.pushButtonSophantule.setText(_translate("MainWindow", "Đếm số phần tử lẻ"))
        self.pushButtonTonggiatriptule.setText(_translate("MainWindow", "Tổng giá trị phần tử lẻ"))
        self.pushButtonSapmangtang.setText(_translate("MainWindow", "Sắp mảng tăng"))
        self.pushButtonSapmanggiam.setText(_translate("MainWindow", "Sắp mảng giảm"))
        self.pushButtonTangmoiptulen2.setText(_translate("MainWindow", "Tăng mỗi phần tử lên 2"))
        self.pushButtonTimptunhonhat.setText(_translate("MainWindow", "Tìm phần tử nhỏ nhất"))
        self.pushButtonThoat.setText(_translate("MainWindow", "Thoát"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())