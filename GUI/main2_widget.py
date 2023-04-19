# Form implementation generated from reading ui file 'main_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 479)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(280, 110, 181, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.consultationbutton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.consultationbutton.setFont(font)
        self.consultationbutton.setObjectName("consultationbutton")
        self.gridLayout.addWidget(self.consultationbutton, 4, 0, 1, 1)
        self.reportbutton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.reportbutton.setFont(font)
        self.reportbutton.setObjectName("reportbutton")
        self.gridLayout.addWidget(self.reportbutton, 2, 0, 1, 1)
        self.prescriptionbutton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.prescriptionbutton.setFont(font)
        self.prescriptionbutton.setObjectName("prescriptionbutton")
        self.gridLayout.addWidget(self.prescriptionbutton, 3, 0, 1, 1)
        self.prombutton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.prombutton.setFont(font)
        self.prombutton.setObjectName("prombutton")
        self.gridLayout.addWidget(self.prombutton, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 91, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../blank-profile-picture-973460_960_720 kopi.png"))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 160, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.age = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.age.setObjectName("age")
        self.verticalLayout.addWidget(self.age)
        self.telephone = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.telephone.setObjectName("telephone")
        self.verticalLayout.addWidget(self.telephone)
        self.weight = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.weight.setObjectName("weight")
        self.verticalLayout.addWidget(self.weight)
        self.comorbidities = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.comorbidities.setObjectName("comorbidities")
        self.verticalLayout.addWidget(self.comorbidities)
        self.medicine = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.medicine.setObjectName("medicine")
        self.verticalLayout.addWidget(self.medicine)
        self.fev1 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.fev1.setObjectName("fev1")
        self.verticalLayout.addWidget(self.fev1)
        self.gold = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.gold.setObjectName("gold")
        self.verticalLayout.addWidget(self.gold)
        self.mrc = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.mrc.setObjectName("mrc")
        self.verticalLayout.addWidget(self.mrc)
        self.pef = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.pef.setObjectName("pef")
        self.verticalLayout.addWidget(self.pef)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.consultationbutton.setText(_translate("MainWindow", "Create consultation"))
        self.reportbutton.setText(_translate("MainWindow", "Write Report"))
        self.prescriptionbutton.setText(_translate("MainWindow", "Create prescription"))
        self.prombutton.setText(_translate("MainWindow", "PROM"))
        self.name.setText(_translate("MainWindow", "Name:"))
        self.age.setText(_translate("MainWindow", "Age: "))
        self.telephone.setText(_translate("MainWindow", "Telephone: "))
        self.weight.setText(_translate("MainWindow", "Weight: "))
        self.comorbidities.setText(_translate("MainWindow", "Comorbidities:"))
        self.medicine.setText(_translate("MainWindow", "Medicine:"))
        self.fev1.setText(_translate("MainWindow", "FEV1:"))
        self.gold.setText(_translate("MainWindow", "GOLD:"))
        self.mrc.setText(_translate("MainWindow", "MRC:"))
        self.pef.setText(_translate("MainWindow", "PEF:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
