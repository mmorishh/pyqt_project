import sqlite3
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic.properties import QtCore

from genshin_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("genshin_db.sqlite")
        cur = self.con.cursor()
        self.cb_elements.addItems(
            [item[0] for item in cur.execute("SELECT name FROM elements").fetchall()])
        self.cb_weapons.addItems(
            [item[0] for item in cur.execute("SELECT name FROM weap_role").fetchall()])
        self.btn_show.clicked.connect(self.filter)

        self.btn1.clicked.connect(self.btn)
        self.btn2.clicked.connect(self.btn)
        self.btn3.clicked.connect(self.btn)
        self.btn4.clicked.connect(self.btn)
        self.btn5.clicked.connect(self.btn)
        self.btn6.clicked.connect(self.btn)
        self.btn7.clicked.connect(self.btn)
        self.btn8.clicked.connect(self.btn)
        self.btn9.clicked.connect(self.btn)
        self.btn10.clicked.connect(self.btn)
        self.btn11.clicked.connect(self.btn)
        self.btn12.clicked.connect(self.btn)
        self.btn13.clicked.connect(self.btn)
        self.btn14.clicked.connect(self.btn)
        self.btn15.clicked.connect(self.btn)
        self.btn16.clicked.connect(self.btn)
        self.btn17.clicked.connect(self.btn)
        self.btn18.clicked.connect(self.btn)
        self.list_btn = [self.btn1, self.btn2, self.btn3, self.btn4,
                         self.btn5, self.btn6, self.btn7, self.btn8,
                         self.btn9, self.btn10, self.btn11, self.btn12,
                         self.btn13, self.btn14, self.btn15, self.btn16,
                         self.btn17, self.btn18]
        self.btn_search.clicked.connect(self.search)

    def search(self):  #  работает с поиском
        _translate = QtCore.QCoreApplication.translate
        if self.le_search.text() == '':
            pass
        elif self.le_search.text() == 'Diluc' or\
          self.le_search.text() == 'Tartaglia' or\
          self.le_search.text() == 'Keqing' or\
          self.le_search.text() == 'Kazuha' or\
          self.le_search.text() == 'Kaeya' or\
          self.le_search.text() == 'Lisa' or\
          self.le_search.text() == 'Barbara' or\
          self.le_search.text() == 'Qiqi' or\
          self.le_search.text() == 'Zhongli' or\
          self.le_search.text() == 'Klee' or\
          self.le_search.text() == 'Xiao' or\
          self.le_search.text() == 'Razor' or\
          self.le_search.text() == 'Albedo' or\
          self.le_search.text() == 'Bennet' or\
          self.le_search.text() == 'Xingqiu' or\
          self.le_search.text() == 'Chongyun' or\
          self.le_search.text() == 'Venti' or\
          self.le_search.text() == 'Ningguang':

            cur = self.con.cursor()
            __sortingEnabled = self.listWidjet.isSortingEnabled()
            self.listWidget.setSortingEnabled(False)
            self.listWidget.setSortingEnabled(__sortingEnabled)
            item = self.Widget.item(0)
            item.setText(_translate("MainWindow", 'Name:', self.le_search.text()))
            item = self.Widget.item(2)
            item.setText(_translate("MainWindow", 'Element:',
                                    cur.execute("SELECT element FROM characters"
                                                "WHERE name=self.le_search.text()").fetchall()))
            item = self.Widget.item(4)
            item.setText(_translate("MainWindow", 'Weapon:',
                                    cur.execute("SELECT weap_role FROM characters"
                                                "WHERE name=self.le_search.text()").fetchall()))
            item = self.Widget.item(6)
            item.setText(_translate("MainWindow", 'Artifacts:',
                                    cur.execute("SELECT artifacts FROM characters"
                                                "WHERE name=self.le_search.text()").fetchall()))
            item = self.Widget.item(8)
            item.setText(_translate("MainWindow", 'Weapons:',
                                    cur.execute("SELECT weapons FROM characters"
                                                "WHERE name=self.le_search.text()").fetchall()))



        else:
            item = self.Widget.item(0)
            item.setText(_translate("MainWindow", 'ERROR'))
            item = self.Widget.item(1)
            item.setText(_translate("MainWindow", 'Please check the character name'))

    def filter(self):
        cur = self.con.cursor()
        res_element = cur.execute(f"""
                      SELECT DISTINCT characters.id
                      FROM characters, elements JOIN characters_elements
                      ON characters.id = characters_elements.id_elements
                      WHERE id_elements = {self.cb_elements.currentIndex() + 1}
                      """).fetchall()
        for j in self.list_btn:
            for i in res_element:
                if 'btn' + str(i) == str(j):
                    j.show()
                else:
                    j.hide()
        res_weapon = cur.execute(f"""
                      SELECT DISTINCT characters.id
                      FROM characters, weap_role JOIN weap_role_characters
                      ON characters.id = weap_role_characters.id_weap_role
                      WHERE id_weap_role = {self.cb_weapons.currentIndex() + 1}
                      """).fetchall()
        for j in self.list_btn:
            for i in res_weapon:
                if 'btn' + str(i) == str(j):
                    j.show()
                else:
                    j.hide()
    def btn(self):
        pass


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
