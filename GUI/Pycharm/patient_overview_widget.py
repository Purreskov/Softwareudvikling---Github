# Form implementation generated from reading ui file 'patient_overview_widget.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_patient_overview(object):
    def setupUi(self, patient_overview):
        patient_overview.setObjectName("patient_overview")
        patient_overview.resize(584, 423)
        self.tableView = QtWidgets.QTableView(parent=patient_overview)
        self.tableView.setGeometry(QtCore.QRect(10, 90, 561, 191))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(parent=patient_overview)
        self.label.setGeometry(QtCore.QRect(200, 50, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.update_user_button = QtWidgets.QPushButton(parent=patient_overview)
        self.update_user_button.setGeometry(QtCore.QRect(60, 311, 151, 51))
        self.update_user_button.setObjectName("update_user_button")
        self.pushButton_2 = QtWidgets.QPushButton(parent=patient_overview)
        self.pushButton_2.setGeometry(QtCore.QRect(372, 311, 151, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(patient_overview)
        QtCore.QMetaObject.connectSlotsByName(patient_overview)

    def retranslateUi(self, patient_overview):
        _translate = QtCore.QCoreApplication.translate
        patient_overview.setWindowTitle(_translate("patient_overview", "Form"))
        self.label.setText(_translate("patient_overview", "Patient overview"))
        self.update_user_button.setText(_translate("patient_overview", "Update user"))
        self.pushButton_2.setText(_translate("patient_overview", "Delete user"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    patient_overview = QtWidgets.QWidget()
    ui = Ui_patient_overview()
    ui.setupUi(patient_overview)
    patient_overview.show()
    sys.exit(app.exec())