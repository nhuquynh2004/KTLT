from PyQt6.QtWidgets import QPushButton
from MainWindow60 import Ui_MainWindow
from SinhVien import SinhVien
from datetime import datetime

class MainWindow60Ext(Ui_MainWindow):
    def __init__(self):
        self.selectedSV=None
        self.listSV={}
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def signalsAndslots(self):
        self.pushButtonSave.clicked.connect(self.save_update)
        self.pushButtonRemove.clicked.connect(self.remove)
        self.pushButtonTongSV.clicked.connect(self.countSV)

    def save_update(self):
        #Lấy thông tin input
        mssv=self.lineEditMssv.text().strip()
        hoten=self.lineEditHoten.text().strip()
        ngaysinh_str=self.lineEditNgaysinh.text().strip()

        #Nếu thiếu 1 trong 3 thông tin thì không lưu được
        if not mssv or not hoten or not ngaysinh_str: return

        #Chuyển ngaysinh từ dạng str về datetime
        ngaysinh_int = list(map(int, ngaysinh_str.split('/')))  # or ngaysinh_int=(int(x) for x in ngaysinh_str.split('/'))
        ngaysinh_datetime=datetime(ngaysinh_int[2],ngaysinh_int[1],ngaysinh_int[0])

        #Gom thông tin input vào list sv
        sv = SinhVien(mssv, hoten, ngaysinh_datetime)

        #Lấy thông tin họ, tên, tuổi qua method ho_ten() và tuoi() trong class SinhVien
        ho,ten=sv.ho_ten()
        tuoi=sv.tuoi()

        if mssv in self.listSV: #Sinh viên đã lưu
            #Lấy button với mssv tương ứng đã lưu trong dic listSV
            sv_btn = self.listSV[mssv]['btn']

            #Lấy thông tin input với mssv tương ứng đã lưu trong dic listSV
            sv_info = self.listSV[mssv]['sv']

            #Cập nhật thông tin input vào dic listSV
            sv_info.hoten = hoten
            sv_info.ngaysinh = ngaysinh_datetime

            #Cập nhật button text vào dic listSV
            sv_btn.setText(f"MSSV: {mssv}\nHọ: {ho}  Tên: {ten}\nHọ và tên: {hoten}\nNgày sinh: {ngaysinh_str}\tTuổi: {tuoi}")

        else: #Sinh viên chưa lưu
            #Tạo button cho SV mới
            btn = QPushButton(f"MSSV: {mssv}\nHọ: {ho}  Tên: {ten}\nHọ và tên: {hoten}\nNgày sinh: {ngaysinh_str}\tTuổi: {tuoi}")
            btn.setCheckable(True)
            btn.setStyleSheet("background-color: rgb(240,237,237);")

            #Lưu listSV (chứa thông tin input) và button (mới tạo) vào dic listSV
            self.listSV[mssv] = {'sv': sv, 'btn': btn}

            #Thêm button vào verticalLayout --> show button
            self.verticalLayout.addWidget(btn)

            #Click vào button, gọi show_inputInfo
            btn.clicked.connect(lambda: self.show_SVInfo(mssv))

            self.clearContents()

    def clearContents(self):
        self.lineEditMssv.clear()
        self.lineEditHoten.clear()
        self.lineEditNgaysinh.clear()

    def show_SVInfo(self,mssv):
        # Bỏ chọn nút cũ (self.selectedSV.setChecked(False)).
        if self.selectedSV: self.selectedSV.setChecked(False)

        # Cập nhật selectedSV thành nút vừa chọn và chọn nó.
        self.selectedSV = self.listSV[mssv]['btn']
        self.selectedSV.setChecked(True)

        #Lấy thông tin input với mssv tương ứng đã lưu trong dic listSV
        sv_info = self.listSV[mssv]['sv']

        #Hiện thông tin trong sv_info lên khu vực nhập thông tin
        self.lineEditMssv.setText(sv_info.mssv)
        self.lineEditHoten.setText(sv_info.hoten)
        self.lineEditNgaysinh.setText(sv_info.ngaysinh.strftime("%d/%m/%Y"))

    def remove(self):
        if self.selectedSV:
            #Xoá button SV đang chọn
            self.verticalLayout.removeWidget(self.selectedSV)
            self.selectedSV.deleteLater()

            #Xóa thông tin SV đang chọn trong listSV
            mssv = self.lineEditMssv.text().strip()
            if mssv in self.listSV: del self.listSV[mssv]

            self.clearContents()
            self.selectedSV=None

    def countSV(self): self.lineEditTongSV.setText(str(len(self.listSV)))

