import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Cau61.StudentBody import StudentBody

app = QApplication(sys.argv)  # Dùng sys.argv thay vì []
mainwindow = QMainWindow()
ui = StudentBody()
ui.setupUi(mainwindow)
ui.setupSignalsAndSlots()
mainwindow.show()
sys.exit(app.exec())  # Đảm bảo ứng dụng thoát đúng cách
