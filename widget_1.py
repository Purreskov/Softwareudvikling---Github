# Form implementation generated from reading ui file 'widget_1.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3

import mysql.connector
from PyQt6 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 80, 181, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 120, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setText(_translate("Form", "Enter social security number"))
        self.pushButton.setText(_translate("Form", "Søg"))

### Virker ikke:
    # https://www.youtube.com/watch?v=YySB6tkjZ7Y&t=161s
    # https://www.youtube.com/watch?v=g60QghtJmjY&t=2s
    def loaddata(self):
        connection = sqlite3.connect("patient_liste")
        mycursor = connection.cursor()
        sqlquery = "Select * FROM patient"
        for row in mycursor.execute(sqlquery):
            print(row)
#Opretter fobindelse til DB
mydb = mysql.connector.connect(host="localhost", user="root", password="Gulerodskage64", database="patient_liste")

#Vælger patient table
mycursor = mydb.cursor()
mycursor.execute("Select * from patient")
myresult = mycursor.fetchall()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
