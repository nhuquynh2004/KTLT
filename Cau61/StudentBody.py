from PyQt6.QtWidgets import QPushButton

from MainWindow61 import Ui_MainWindow
from Student_Adress import Student,Address

class StudentBody(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def setupSignalsAndSlots(self):
        self.pushButtonView.clicked.connect(self.view)
        self.pushButtonSave.clicked.connect(self.save)
        self.pushButtonUpdate.clicked.connect(self.update)
        self.pushButtonRemove.clicked.connect(self.remove)
    def __init__(self):
        super().__init__()
        self.selectedSV=None
        self.listStudent={}

    def getInfo(self):
        id=self.lineEditStudentID.text()
        first=self.lineEditFirstName.text()
        last=self.lineEditLastName.text()
        home_address=[self.lineEditHomeStreet.text(),
                      self.lineEditHomeDistrict.text(),
                      self.lineEditHomeCity.text(),
                      self.lineEditHomeZipCode.text()]
        school_address=[self.lineEditSchoolStreet.text(),
                      self.lineEditSchoolDistrict.text(),
                      self.lineEditSchoolCity.text(),
                      self.lineEditSchoolZipCode.text()]
        home=Address(*home_address)
        school=Address(*school_address)
        stu=Student(id,first,last,home,school)
        return stu

    def show_button(self,stu):
        home=stu.home_address.string_address()
        school=stu.school_address.string_address()
        return f"ID: {stu.id}\nName: {stu.first_name} {stu.last_name}\nHome address: {home}\nSchool address: {school}"

    def select_button(self,id):
        if self.selectedSV: self.selectedSV.setChecked(False)
        self.selectedSV=self.listStudent[id]["btn"]
        self.selectedSV.setChecked(True)

    def clearContents(self):
        self.lineEditStudentID.setText('')
        self.lineEditFirstName.setText('')
        self.lineEditLastName.setText('')
        self.lineEditHomeStreet.setText('')
        self.lineEditHomeDistrict.setText('')
        self.lineEditHomeCity.setText('')
        self.lineEditHomeZipCode.setText('')
        self.lineEditSchoolStreet.setText('')
        self.lineEditSchoolDistrict.setText('')
        self.lineEditSchoolCity.setText('')
        self.lineEditSchoolZipCode.setText('')

    def save(self):
        stu = self.getInfo()
        if not stu.id or not stu.first_name or not stu.last_name: return
        if stu.id in self.listStudent: pass
        else:
            btn = QPushButton(self.show_button(stu))
            btn.setCheckable(True)
            btn.setStyleSheet("background-color: rgb(240,237,237);text-align: left; padding-left: 10px;")
            self.verticalLayout.addWidget(btn)
            self.listStudent[stu.id] = {"stu": stu, "btn": btn}
            btn.clicked.connect(lambda: self.select_button(stu.id))
        self.clearContents()

    def view(self):
        if self.selectedSV:
            for id, data in self.listStudent.items(): #id là key, data là value, listStudent.items(): trả về ds các cặp key,value
                if data["btn"] == self.selectedSV: #data["btn"]: lấy data button đang duyệt trong listStudent
                    stu = data["stu"]
                    self.lineEditStudentID.setText(stu.id)
                    self.lineEditFirstName.setText(stu.first_name)
                    self.lineEditLastName.setText(stu.last_name)
                    self.lineEditHomeStreet.setText(stu.home_address.street)
                    self.lineEditHomeDistrict.setText(stu.home_address.district)
                    self.lineEditHomeCity.setText(stu.home_address.city)
                    self.lineEditHomeZipCode.setText(stu.home_address.zipcode)
                    self.lineEditSchoolStreet.setText(stu.school_address.street)
                    self.lineEditSchoolDistrict.setText(stu.school_address.district)
                    self.lineEditSchoolCity.setText(stu.school_address.city)
                    self.lineEditSchoolZipCode.setText(stu.school_address.zipcode)
                    break

    def update(self):
        stu=self.getInfo()
        if stu.id in self.listStudent:
            self.listStudent[stu.id]["stu"]=stu
            btn=(self.listStudent[stu.id]["btn"])
            btn.setText(self.show_button(stu))
            self.clearContents()
        else: pass

    def remove(self):
        if self.selectedSV:
            for id,data in self.listStudent.items():
                if data["btn"]==self.selectedSV:
                    remove_id=id
            if remove_id:
                self.verticalLayout.removeWidget(self.selectedSV)
                self.selectedSV.deleteLater()
                del self.listStudent[remove_id]
                self.selectedSV=None
        self.clearContents()