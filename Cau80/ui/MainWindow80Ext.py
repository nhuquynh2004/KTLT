import functools

from PyQt6.QtWidgets import QPushButton, QMessageBox

from Cau80.libs.TXTFileFactory import TXTFileFactory
from Cau80.models.Product import Product
from Cau80.ui.MainWindow80 import Ui_MainWindow


class MainWindow80Ext(Ui_MainWindow):
    def __init__(self):
        self.products=self.get_all_product()
        self.selected_product=None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalsAndSlots()
        self.showProducttoUI()
    def setupSignalsAndSlots(self):
        self.pushButtonSave.clicked.connect(self.save)
        self.pushButtonRemove.clicked.connect(self.remove)
    def get_all_product(self):
        txt = TXTFileFactory()
        filename = "../dataset/products.txt"
        products = txt.readData(filename)
        return products
    def clearLayout(self,layout):
        if layout is not None:
            while layout.count():
                item=layout.takeAt(0)
                widget=item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())
    def showProducttoUI(self):
        self.clearLayout(self.verticalLayout)
        for i in range(len(self.products)):
            pro=self.products[i]
            btn=QPushButton(text=str(pro))
            self.verticalLayout.addWidget(btn)
            btn.clicked.connect(functools.partial(self.detailData,pro))
    def detailData(self,pro):
        self.lineEditID.setText(pro.id)
        self.lineEditName.setText(pro.name)
        self.lineEditPrice.setText(str(pro.price))
        self.selected_product=pro
    def save(self):
        id=self.lineEditID.text()
        name=self.lineEditName.text()
        price=float(self.lineEditPrice.text())
        new_product=Product(id,name,price)
        self.products.append(new_product)
        txt=TXTFileFactory()
        filename="../dataset/products.txt"
        txt.writeData(filename,new_product)
        self.showProducttoUI()
    def remove(self):
        id=self.lineEditID.text()
        name=self.lineEditName.text()
        dlg=QMessageBox(self.MainWindow)
        dlg.setText(f"Ê muốn xóa sản phầm {id}-{name} hả?")
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons=QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        button=dlg.exec()
        if button==QMessageBox.StandardButton.No:
            return
        if self.selected_product:
            self.products = [p for p in self.products if p.id != self.selected_product.id]
            filename = "../dataset/products.txt"
            with open(filename, 'w', encoding='utf-8') as file:
                for product in self.products:
                    file.writelines(f"{product.id};{product.name};{product.price}\n")
            self.selected_product = None
            self.lineEditID.clear()
            self.lineEditName.clear()
            self.lineEditPrice.clear()
            self.showProducttoUI()
