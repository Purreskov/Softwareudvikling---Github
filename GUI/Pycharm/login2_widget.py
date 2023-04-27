# Form implementation generated from reading ui file 'login_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets

from main3_widget_final import MainWindow
from login_error_widget import ErrorWidget
from SQL_connector import CPR_list

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.cpr_input = QtWidgets.QLineEdit(parent=Form)
        self.cpr_input.setGeometry(QtCore.QRect(100, 80, 181, 21))
        self.cpr_input.setText("")
        self.cpr_input.setObjectName("cpr_input")
        self.searchbutton = QtWidgets.QPushButton(parent=Form)
        self.searchbutton.setGeometry(QtCore.QRect(130, 120, 113, 32))
        self.searchbutton.setObjectName("searchbutton")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(120, 50, 141, 21))
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #INDSAT
        self.searchbutton.clicked.connect(self.on_search_button_clicked)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Lookup patient"))
        self.searchbutton.setText(_translate("Form", "Search"))
        self.label.setText(_translate("Form", "Social security number"))

    #INDSAT
    def on_search_button_clicked(self):
        if self.cpr_input.text() in CPR_list:
            # Create an instance of the main2_widget
            self.main3_widget_final = QtWidgets.QWidget()
            self.ui2 = MainWindow()
            self.ui2.setupUi(self.main3_widget_final, self.cpr_input.text())
            self.main3_widget_final.show()
        else:
            self.login_error_widget = QtWidgets.QWidget()
            self.ui2 = ErrorWidget()
            self.ui2.setupUi(self.login_error_widget)
            self.login_error_widget.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())


