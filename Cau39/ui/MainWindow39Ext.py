from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget
import random, functools
from MainWindow39 import Ui_MainWindow

class MainWindow39Ext(Ui_MainWindow):
    def __init__(self):
        self.list = []
        self.previous_button = None
        self.selected_button = None
        self.selected_index = -1
        self.buttons = []

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalsandSlots()

    def showWindow(self):
        self.MainWindow.show()

    def select_button(self, btn, index):
        if self.selected_button:
            self.selected_button.setChecked(False)
        self.selected_button = btn
        self.selected_index = index
        btn.setChecked(True)
        self.lineEditN.setText(btn.text())

    def setupSignalsandSlots(self):
        self.pushButtonCreate.clicked.connect(self.solveCreateRandom)
        self.pushButtonDelete.clicked.connect(self.deleteNegative)
        self.pushButtonAdd.clicked.connect(self.add)
        self.pushButtonUpdate.clicked.connect(self.updateSelected)
        self.pushButtonAscSort.clicked.connect(self.sort_buttons_ascending)
        self.pushButtonDescSort.clicked.connect(self.sort_buttons_descending)
        self.pushButtonRemoveAll.clicked.connect(self.remove_all_buttons)

    def solveCreateRandom(self):
        n = int(self.lineEditN.text())
        self.list = [random.randint(-100, 100) for _ in range(n)]
        self.createRandom()

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def createRandom(self):
        self.clearLayout(self.verticalLayout)
        self.buttons = []
        for i, value in enumerate(self.list):
            btn = QPushButton(text=str(value))
            btn.setCheckable(True)
            btn.setStyleSheet("background-color:rgb(240,237,237);")
            btn.clicked.connect(functools.partial(self.select_button, btn, i))
            self.verticalLayout.addWidget(btn)
            self.buttons.append(btn)

    def deleteNegative(self):
        for i in reversed(range(self.verticalLayout.count())):
            btn = self.verticalLayout.itemAt(i).widget()
            if btn and int(btn.text()) < 0:
                btn.setParent(None)

    def add(self):
        value = random.randint(0, 10)
        btn = QPushButton(text=str(value))
        btn.setCheckable(True)
        btn.setStyleSheet("background-color:rgb(240,237,237);")
        btn.clicked.connect(functools.partial(self.select_button, btn, len(self.buttons)))
        self.buttons.append(btn)
        self.verticalLayout.addWidget(btn)

    def updateSelected(self):
        if self.selected_button:
            value = int(self.selected_button.text())
            self.selected_button.setText(str(value // 10))

    def sort_buttons_ascending(self):
        buttons = sorted([self.verticalLayout.itemAt(i).widget() for i in range(self.verticalLayout.count())],
                         key=lambda btn: int(btn.text()))
        for i in reversed(range(self.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().setParent(None)
        for btn in buttons:
            self.verticalLayout.addWidget(btn)

    def sort_buttons_descending(self):
        buttons = sorted([self.verticalLayout.itemAt(i).widget() for i in range(self.verticalLayout.count())],
                         key=lambda btn: int(btn.text()), reverse=True)
        for i in reversed(range(self.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().setParent(None)
        for btn in buttons:
            self.verticalLayout.addWidget(btn)

    def remove_all_buttons(self):
        self.buttons.clear()
        self.refreshLayout()

    def refreshLayout(self):
        self.clearLayout(self.verticalLayout)
        for btn in self.buttons:
            self.verticalLayout.addWidget(btn)
