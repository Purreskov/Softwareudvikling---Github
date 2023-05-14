# Form implementation generated from reading ui file 'main_menu_widget.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from GUI.Pycharm.create_user_widget import Ui_create_user_menu
from GUI.Pycharm.patient_overview_widget import Ui_patient_overview


class Ui_main_menu(object):
    def setupUi(self, main_menu):
        main_menu.setObjectName("main_menu")
        main_menu.resize(443, 391)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=main_menu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 110, 371, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.create_user = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.create_user.setObjectName("create_user")
        self.verticalLayout.addWidget(self.create_user)
        self.edit_user = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.edit_user.setObjectName("edit_user")
        self.verticalLayout.addWidget(self.edit_user)
        self.lookup_user = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.lookup_user.setObjectName("lookup_user")
        self.verticalLayout.addWidget(self.lookup_user)
        self.label = QtWidgets.QLabel(parent=main_menu)
        self.label.setGeometry(QtCore.QRect(170, 30, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(main_menu)
        QtCore.QMetaObject.connectSlotsByName(main_menu)

    # INDSAT
        self.create_user.clicked.connect(self.create_user_clicked)
        self.edit_user.clicked.connect(self.edit_user_clicked)

    # INDSAT

    def create_user_clicked(self):
        self.create_user_widget= QtWidgets.QWidget()
        self.ui2 = Ui_create_user_menu()
        self.ui2.setupUi(self.create_user_widget)
        self.create_user_widget.show()

    def edit_user_clicked(self):
        self.patient_overview_widget = QtWidgets.QWidget()
        self.ui2 = Ui_patient_overview()
        self.ui2.setupUi(self.patient_overview_widget)
        self.patient_overview_widget.show()
    def retranslateUi(self, main_menu):
        _translate = QtCore.QCoreApplication.translate
        main_menu.setWindowTitle(_translate("main_menu", "Form"))
        self.create_user.setText(_translate("main_menu", "Create user"))
        self.edit_user.setText(_translate("main_menu", "Edit user"))
        self.lookup_user.setText(_translate("main_menu", "Lookup user"))
        self.label.setText(_translate("main_menu", "Main menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_menu = QtWidgets.QWidget()
    ui = Ui_main_menu()
    ui.setupUi(main_menu)
    main_menu.show()
    sys.exit(app.exec())
