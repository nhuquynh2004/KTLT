from PyQt6.QtWidgets import QPushButton
from MainWindow45 import Ui_MainWindow


class MainWindow45Ext(Ui_MainWindow):
    def __init__(self):
        self.selectedBook = None
        self.books = {}

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.signalsAndslots()

    def signalsAndslots(self):
        self.pushButtonSave.clicked.connect(self.saveBook)
        self.pushButtonRemove.clicked.connect(self.removeBook)

    def saveBook(self):
        isbn = self.lineEditISBN.text().strip()
        book_title = self.lineEditTitle.text().strip()
        author = self.lineEditAuthor.text().strip()
        year = self.lineEditYear.text().strip()
        publisher = self.lineEditPublisher.text().strip()

        if not isbn or not book_title:
            return

        bookInfo = (isbn, book_title, author, year, publisher)

        if isbn in self.books:
            btn = self.books[isbn]
            btn.setText(f'ISBN: {bookInfo[0]}, {bookInfo[1]}, {bookInfo[2]}, {bookInfo[3]}, {bookInfo[4]}')
        else:
            btn = QPushButton(f'ISBN: {bookInfo[0]}, {bookInfo[1]}, {bookInfo[2]}, {bookInfo[3]}, {bookInfo[4]}')
            btn.setCheckable(True)
            btn.setStyleSheet("background-color: rgb(240,237,237);")

            btn.clicked.connect(lambda: self.select_button(btn))

            self.books[isbn] = btn
            self.verticalLayout.addWidget(btn)

        self.clearContents()

    def clearContents(self):
        self.lineEditISBN.clear()
        self.lineEditTitle.clear()
        self.lineEditYear.clear()
        self.lineEditAuthor.clear()
        self.lineEditPublisher.clear()

    def select_button(self, btn):
        if self.selectedBook:
            self.selectedBook.setChecked(False)
        self.selectedBook = btn
        btn.setChecked(True)

        book_text = btn.text().replace("ISBN: ", "").split(", ")
        self.lineEditISBN.setText(book_text[0])
        self.lineEditTitle.setText(book_text[1])
        self.lineEditAuthor.setText(book_text[2])
        self.lineEditYear.setText(book_text[3])
        self.lineEditPublisher.setText(book_text[4])

    def removeBook(self):
        if self.selectedBook:
            book_text = self.selectedBook.text().replace("ISBN: ", "").split(", ")
            isbn = book_text[0]
            self.verticalLayout.removeWidget(self.selectedBook)
            self.selectedBook.deleteLater()
            if isbn in self.books:
                del self.books[isbn]
            self.clearContents()
            self.selectedBook = None
