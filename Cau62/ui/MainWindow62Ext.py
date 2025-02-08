from PyQt6.QtWidgets import QPushButton

from Cau62.models.Danhmuc import Danhmuc
from Cau62.models.Sanpham import Sanpham
from MainWindow62 import Ui_MainWindow

class MainWindow62Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def __init__(self):
        super().__init__()
        self.listCatalogue={}
        self.selectedCatalogue = None
        self.selectedProduct = None
        self.existing_product_widgets = []
    def setupSignalsAndSlots(self):
        self.pushButtonCatalogueSave.clicked.connect(self.SaveCatalogue)
        self.pushButtonCatalogueRemove.clicked.connect(self.RemoveCatalogue)
        self.pushButtonProductSave.clicked.connect(self.SaveProduct)
        self.pushButtonProductRemove.clicked.connect(self.RemoveProduct)
        self.pushButtonTotalValue.clicked.connect(self.totalValue)
        self.pushButtonListByOrigin.clicked.connect(self.filter_products_by_origin)

#Thao tác với Catalogue
    def select_buttonCtl(self,id):
        if self.selectedCatalogue:
            self.selectedCatalogue.setChecked(False)
        self.selectedCatalogue = self.listCatalogue[id]["btn"]
        self.selectedCatalogue.setChecked(True)
        Catalog_info = self.listCatalogue[id]["ctl"]
        self.LineEditCatalogueID.setText(Catalog_info.id)
        self.LineEditCatalogueName.setText(Catalog_info.name)
        while self.verticalLayoutProduct.count():
            item = self.verticalLayoutProduct.takeAt(0)
            if (widget := item.widget()):
                widget.deleteLater()
        self.updateProductLayout(Catalog_info)
    def updateProductLayout(self, Catalog_info):
        products_to_display = list(Catalog_info.list_product.items())
        currentWidgets = len(self.existing_product_widgets)
        requiredWitgets = len(products_to_display)
        for i in range(min(currentWidgets, requiredWitgets)):
            pdt_id, data = products_to_display[i]
            widget = self.existing_product_widgets[i]
            widget.setText(
                f"Product ID: {pdt_id}\nName: {data['pdt'].name}\nPrice: {data['pdt'].price}\nOrigin: {data['pdt'].origin}")
            widget.setVisible(True)  # Hiển thị widget
        if requiredWitgets > currentWidgets:
            for i in range(currentWidgets, requiredWitgets):
                pdt_id, data = products_to_display[i]
                btn = QPushButton(
                    f"Product ID: {pdt_id}\nName: {data['pdt'].name}\nPrice: {data['pdt'].price}\nOrigin: {data['pdt'].origin}")
                btn.setCheckable(True)
                btn.setStyleSheet("background-color: rgb(240,237,237);text-align: left; padding-left: 10px;")
                btn.clicked.connect(lambda _, id=pdt_id: self.select_buttonPdt(id))
                self.verticalLayoutProduct.addWidget(btn)
                self.existing_product_widgets.append(btn)
        for i in range(requiredWitgets, currentWidgets):
            self.existing_product_widgets[i].setVisible(False)
    def clearContentsCtl(self):
        self.LineEditCatalogueID.clear()
        self.LineEditCatalogueName.clear()
    def SaveCatalogue(self):
        id=self.LineEditCatalogueID.text().strip()
        name=self.LineEditCatalogueName.text().strip()
        ctl=Danhmuc(id,name)
        if id in self.listCatalogue:
            self.listCatalogue[id]["ctl"]=ctl
            self.listCatalogue[id]["btn"].setText(f"Catalogue ID: {id}\nCatalogue Name: {name}")
        else:
            btn=QPushButton(f"Catalogue ID: {id}\nCatalogue Name: {name}")
            btn.setCheckable(True)
            btn.setStyleSheet("background-color: rgb(240,237,237);text-align: left; padding-left: 10px;")
            self.verticalLayoutCatalogue.addWidget(btn)
            self.listCatalogue[id]={"ctl":ctl,"btn":btn}
            btn.clicked.connect(lambda: self.select_buttonCtl(id))
        self.clearContentsCtl()
    def RemoveCatalogue(self):
        if self.selectedCatalogue:
            self.verticalLayoutCatalogue.removeWidget(self.selectedCatalogue)
            self.selectedCatalogue.deleteLater()
            self.verticalLayoutProduct.clear()
            ctl_id=self.LineEditCatalogueID.text().strip()
            if ctl_id in self.listCatalogue:
                del self.listCatalogue[ctl_id] #del: xóa hoàn toàn một biến/ phần tử trong một cấu trúc dữ liệu
                for pdt_id, data in self.listCatalogue[ctl_id]["ctl"].list_product.items():
                    self.verticalLayoutProduct.removeWidget(data["btn"])
                    data["btn"].deleteLater()
            self.clearContentsCtl()
            self.selectedCatalogue=None

#Thao tác với Product
    def select_buttonPdt(self,id):
        ctl_id = self.LineEditCatalogueID.text().strip()
        Product=self.listCatalogue[ctl_id]["ctl"].list_product
        if self.selectedProduct: self.selectedProduct.setChecked(False)
        self.selectedProduct=Product[id]["btn"]
        self.selectedProduct.setChecked(True)
        Product_info=Product[id]["pdt"]
        self.LineEditProductID.setText(Product_info.id)
        self.LineEditProductName.setText(Product_info.name)
        self.LineEditProductPrice.setText(Product_info.price)
        self.LineEditProductOrigin.setText(Product_info.origin)
        self.LineEditInStock.setText(Product_info.in_stock)
    def clearContentsPdt(self):
        self.LineEditProductID.clear()
        self.LineEditProductName.clear()
        self.LineEditProductPrice.clear()
        self.LineEditProductOrigin.clear()
        self.LineEditInStock.clear()
    def SaveProduct(self):
        id=self.LineEditProductID.text().strip()
        name=self.LineEditProductName.text().strip()
        price=self.LineEditProductPrice.text().strip()
        origin=self.LineEditProductOrigin.text().strip()
        in_stock=self.LineEditInStock.text().strip()
        pdt=Sanpham(id,name,price,origin,in_stock)
        if self.selectedCatalogue:
            ctl_id=self.LineEditCatalogueID.text().strip()
            if ctl_id in self.listCatalogue:
                Product=self.listCatalogue[ctl_id]["ctl"].list_product
                if id in Product:
                    Product[id]["pdt"]=pdt
                    Product[id]["btn"].setText(f"Product ID: {id}\nProduct Name: {name}\nProduct Price: {price}\nProduct Origin: {origin}\nProduct In-stock: {in_stock}")
                else:
                    btn=QPushButton(f"Product ID: {id}\nProduct Name: {name}\nProduct Price: {price}\nProduct Origin: {origin}\nProduct In-stock: {in_stock}")
                    btn.setCheckable(True)
                    btn.setStyleSheet("background-color: rgb(240,237,237);text-align: left; padding-left: 10px;")
                    self.verticalLayoutProduct.addWidget(btn)
                    Product[id]={"pdt":pdt,"btn":btn}
                    btn.clicked.connect(lambda: self.select_buttonPdt(id))
                self.clearContentsPdt()
    def RemoveProduct(self):
        if self.selectedProduct:
            self.verticalLayoutProduct.removeWidget(self.selectedProduct)
            self.selectedProduct.deleteLater()
            ctl_id=self.LineEditCatalogueID.text().strip()
            pdt_id=self.LineEditProductID.text().strip()
            Product=self.listCatalogue[ctl_id]["ctl"].list_product
            if pdt_id in Product:
                del Product[pdt_id]
            if self.listCatalogue.get(ctl_id) and pdt_id in self.listCatalogue[ctl_id]["ctl"].list_product:
                del self.listCatalogue[ctl_id]["ctl"].list_product[pdt_id]
            self.clearContentsPdt()
            self.selectedProduct = None

#Tính tổng giá trị và chức năng lọc
    def totalValue(self):
        total_value = 0
        for catalog in self.listCatalogue.values():
            for product_data in catalog["ctl"].list_product.values():
                product = product_data["pdt"]
                try:
                    price = float(product.price)
                    in_stock = int(product.in_stock)
                    total_value += price * in_stock
                except (ValueError, AttributeError): continue
        self.LineEditTotalValue.setText(str(total_value))

    def filter_products_by_origin(self):
        origin = self.LineEditListByOrigin.text()
        while self.verticalLayoutProduct.count():
            item = self.verticalLayoutProduct.takeAt(0)
            if (widget := item.widget()):
                widget.deleteLater()

        for catalog in self.listCatalogue.values():
            for pdt_id, product_data in catalog["ctl"].list_product.items():
                product = product_data["pdt"]
                if product.origin.lower() == origin.lower():
                    btn = QPushButton(
                        f"Product ID: {pdt_id}\nName: {product.name}\nPrice: {product.price}\nOrigin: {product.origin}")
                    btn.setCheckable(True)
                    btn.setStyleSheet("background-color: rgb(240,237,237);text-align: left; padding-left: 10px;")
                    btn.clicked.connect(lambda _, id=pdt_id: self.select_buttonPdt(id))
                    self.verticalLayoutProduct.addWidget(btn)


