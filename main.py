import sqlite3
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

from GenshMain_ui import Ui_Dialog

class MyWidjet(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    ex = MyWidjet()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '  main  ':
    main()