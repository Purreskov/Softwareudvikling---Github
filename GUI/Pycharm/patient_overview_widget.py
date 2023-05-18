from PyQt6 import QtCore, QtGui, QtWidgets
from SQL_connector import connection
from PyQt6.QtWidgets import QMessageBox

class Ui_patient_overview(object):
    def setupUi(self, patient_overview):
        patient_overview.setObjectName("patient_overview")
        patient_overview.resize(584, 423)
        self.tableWidget = QtWidgets.QTableWidget(parent=patient_overview)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 561, 191))
        self.tableWidget.setObjectName("tableView")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(50)
        self.label = QtWidgets.QLabel(parent=patient_overview)
        self.label.setGeometry(QtCore.QRect(200, 50, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.update_user_button = QtWidgets.QPushButton(parent=patient_overview)
        self.update_user_button.setGeometry(QtCore.QRect(60, 311, 151, 51))
        self.update_user_button.setObjectName("update_user_button")
        self.delete_button = QtWidgets.QPushButton(parent=patient_overview)
        self.delete_button.setGeometry(QtCore.QRect(372, 311, 151, 51))
        self.delete_button.setObjectName("delete_button")
        self.retranslateUi(patient_overview)
        QtCore.QMetaObject.connectSlotsByName(patient_overview)

        #load the function loaddata upon opening the widget
        self.loaddata()

        # Connect the deletePatient function to the delete_button's clicked signal
        self.delete_button.clicked.connect(self.deletePatient)

        # Connect the updatePatient function to the update_user_button's clicked signal
        self.update_user_button.clicked.connect(self.updatePatient)

    def retranslateUi(self, patient_overview):
        _translate = QtCore.QCoreApplication.translate
        patient_overview.setWindowTitle(_translate("patient_overview", "Form"))
        self.label.setText(_translate("patient_overview", "Patient overview"))
        self.update_user_button.setText(_translate("patient_overview", "Update user"))
        self.delete_button.setText(_translate("patient_overview", "Delete user"))

    def loaddata(self):
        cur = connection.cursor()
        sql_query = "SELECT pa.cpr, pa.patient_id, pe.age, pe.name, pe.telephone, pa.Weight, pa.FEV1, pa.GOLD, pa.MRC FROM Patients AS pa JOIN Person AS pe ON pa.cpr = pe.cpr"
        cur.execute(sql_query)
        rows = cur.fetchall()
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(9)
        column_names = ["Cpr", "Patient_ID", "Age", "Name", "Telephone", "Weight", "FEV1", "GOLD", "MRC"]
        self.tableWidget.setHorizontalHeaderLabels(column_names)

        table_row = 0
        for row in rows:
            for column, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(table_row, column, item)
            table_row += 1

    def deletePatient(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            patient_id = self.tableWidget.item(selected_row,
                                               1).text()  # Assuming the patient ID is in the second column
            cur = connection.cursor()
            sql_query = "DELETE FROM Patients WHERE Patient_ID = %s"
            cur.execute(sql_query, (patient_id,))
            connection.commit()
            self.loaddata()
            QtWidgets.QMessageBox.information(None, "Success", "Patient deleted successfully.")
        else:
            QtWidgets.QMessageBox.warning(None, "Warning", "Please select a patient to delete.")

    def updatePatient(self):
        selected_row = self.tableWidget.currentRow()
        selected_column = self.tableWidget.currentColumn()

        if selected_row >= 0 and selected_column >= 0:
            item = self.tableWidget.item(selected_row, selected_column)
            current_value = item.text()
            new_value, ok = QtWidgets.QInputDialog.getText(
                self.tableWidget,
                "Update Value",
                f"Enter new value for cell ({selected_row}, {selected_column}):",
                text=current_value
            )

            if ok and new_value:
                item.setText(new_value)

                patient_id = self.tableWidget.item(selected_row, 1).text()
                column_name = self.tableWidget.horizontalHeaderItem(selected_column).text()

                cur = connection.cursor()
                sql_query = f"UPDATE Patients SET {column_name} = %s WHERE Patient_ID = %s"

                try:
                    cur.execute(sql_query, (new_value, patient_id))
                    connection.commit()
                    QMessageBox.information(
                        self.tableWidget,
                        "Success",
                        "Patient data successfully updated!"
                    )
                except Exception as e:
                    connection.rollback()
                    QMessageBox.warning(
                        self.tableWidget,
                        "Error",
                        f"Failed to update patient data:\n{str(e)}"
                    )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    patient_overview = QtWidgets.QWidget()
    ui = Ui_patient_overview()
    ui.setupUi(patient_overview)
    patient_overview.show()
    sys.exit(app.exec())