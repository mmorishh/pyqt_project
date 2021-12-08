import sqlite3
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic.properties import QtCore, QtWidgets

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
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
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

            if self.le_search.text() == 'Diluc':
                pixmap = QPixmap('diluc.jpg')
            elif self.le_search.text() == 'Tartaglia':
                pixmap = QPixmap('tartaglia.jpg')
            elif self.le_search.text() == 'Keqing':
                pixmap = QPixmap('keqing.jpg.jpg')
            elif self.le_search.text() == 'Kazuha':
                pixmap = QPixmap('kazuha.jpg.jpg')
            elif self.le_search.text() == 'Kaeya':
                pixmap = QPixmap('kaeya.jpg.jpg')
            elif self.le_search.text() == 'Lisa':
                pixmap = QPixmap('lisa.jpg')
            elif self.le_search.text() == 'Barbara':
                pixmap = QPixmap('barbara.jpg.jpg')
            elif self.le_search.text() == 'Qiqi':
                pixmap = QPixmap('qiqi.jpg')
            elif self.le_search.text() == 'Zhongli':
                pixmap = QPixmap('zhongli.jpg.jpg')
            elif self.le_search.text() == 'Klee':
                pixmap = QPixmap('klee.jpg.jpg')
            elif self.le_search.text() == 'Xiao':
                pixmap = QPixmap('xiao.jpg')
            elif self.le_search.text() == 'Razor':
                pixmap = QPixmap('razor.jpg.jpg')
            elif self.le_search.text() == 'Albedo':
                pixmap = QPixmap('albedo.jpg.jpg')
            elif self.le_search.text() == 'Bennet':
                pixmap = QPixmap('bennet.jpg.jpg')
            elif self.le_search.text() == 'Xingqiu':
                pixmap = QPixmap('xingqiu.jpg.jpg')
            elif self.le_search.text() == 'Chongyun':
                pixmap = QPixmap('chongyun.jpg.jpg')
            elif self.le_search.text() == 'Venti':
                pixmap = QPixmap('venti.jpg.jpg')
            elif self.le_search.text() == 'Ningguang':
                pixmap = QPixmap('ningguang.jpg.jpg')

            self.label_8.setPixmap(pixmap)
            self.label_8.resize(200, 200)
            self.label_8.move(100, 100)




        else:
            item = self.Widget.item(0)
            item.setText(_translate("MainWindow", 'ERROR'))
            item = self.Widget.item(1)
            item.setText(_translate("MainWindow", 'Please check the character name'))

    def filter(self):
        cur = self.con.cursor()
        res_element = cur.execute(f"""
                      SELECT characters.id
                      FROM characters, elements JOIN characters_elements
                      ON characters.id = characters_elements.id_elements
                      WHERE id_elements = {self.cb_elements.currentIndex() + 1}
                      """).fetchall()
        for i in res_element:
            for j in self.list_btn:
                if 'self.btn' + str(i) == str(j):
                    j.show()
                else:
                    j.hide()

        res_weapon = cur.execute(f"""
                      SELECT characters.id
                      FROM characters, weap_role JOIN weap_role_characters
                      ON characters.id = weap_role_characters.id_weap_role
                      WHERE id_weap_role = {self.cb_weapons.currentIndex() + 1}
                      """).fetchall()
        for j in self.list_btn:
            for i in res_weapon:
                if 'self.btn' + str(i) == str(j):
                    j.show()
                else:
                    j.hide()
    def btn(self):
        button = QApplication.instance().sender()
        btn_name = button.text()
        _translate = QtCore.QCoreApplication.translate
        cur = self.con.cursor()
        __sortingEnabled = self.listWidjet.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        item = self.Widget.item(0)
        item.setText(_translate("MainWindow", 'Name:', btn_name))
        item = self.Widget.item(2)
        item.setText(_translate("MainWindow", 'Element:',
                                cur.execute("SELECT element FROM characters"
                                            "WHERE name=btn_name").fetchall()))
        item = self.Widget.item(4)
        item.setText(_translate("MainWindow", 'Weapon:',
                                cur.execute("SELECT weap_role FROM characters"
                                            "WHERE name=btn_name").fetchall()))
        item = self.Widget.item(6)
        item.setText(_translate("MainWindow", 'Artifacts:',
                                cur.execute("SELECT artifacts FROM characters"
                                            "WHERE name=btn_name").fetchall()))
        item = self.Widget.item(8)
        item.setText(_translate("MainWindow", 'Weapons:',
                                cur.execute("SELECT weapons FROM characters"
                                            "WHERE name=btn_nam)").fetchall()))
        if btn_name == 'Diluc':
            pixmap = QPixmap('diluc.jpg')
        elif btn_name == 'Tartaglia':
            pixmap = QPixmap('tartaglia.jpg')
        elif btn_name == 'Keqing':
            pixmap = QPixmap('keqing.jpg.jpg')
        elif btn_name == 'Kazuha':
            pixmap = QPixmap('kazuha.jpg.jpg')
        elif btn_name == 'Kaeya':
            pixmap = QPixmap('kaeya.jpg.jpg')
        elif btn_name == 'Lisa':
            pixmap = QPixmap('lisa.jpg')
        elif btn_name == 'Barbara':
            pixmap = QPixmap('barbara.jpg.jpg')
        elif btn_name == 'Qiqi':
            pixmap = QPixmap('qiqi.jpg')
        elif btn_name == 'Zhongli':
            pixmap = QPixmap('zhongli.jpg.jpg')
        elif btn_name == 'Klee':
            pixmap = QPixmap('klee.jpg.jpg')
        elif btn_name == 'Xiao':
            pixmap = QPixmap('xiao.jpg')
        elif btn_name == 'Razor':
            pixmap = QPixmap('razor.jpg.jpg')
        elif btn_name == 'Albedo':
            pixmap = QPixmap('albedo.jpg.jpg')
        elif btn_name == 'Bennet':
            pixmap = QPixmap('bennet.jpg.jpg')
        elif btn_name == 'Xingqiu':
            pixmap = QPixmap('xingqiu.jpg.jpg')
        elif btn_name == 'Chongyun':
            pixmap = QPixmap('chongyun.jpg.jpg')
        elif btn_name == 'Venti':
            pixmap = QPixmap('venti.jpg.jpg')
        elif btn_name == 'Ningguang':
            pixmap = QPixmap('ningguang.jpg.jpg')

        self.label_8.setPixmap(pixmap)
        self.label_8.resize(200, 200)
        self.label_8.move(100, 100)


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
