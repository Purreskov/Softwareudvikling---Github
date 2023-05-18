import mysql.connector
from mysql.connector import Error
from User import *

try:
    connection = mysql.connector.connect(host='mysql-db.caprover.diplomportal.dk',
                                         database='s230899',
                                         user='s230899',
                                         password='5yyApJaeFajPBo9ARO8Hl')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select * from Patients")
        record = cursor.fetchall()
        print("You're connected to database: ", record)
        CPR_list = [i[0] for i in record]
        def select(col, tabl, cond, var):
            cursor.execute(f"SELECT {col} FROM {tabl} WHERE {cond} = '{var}'")
            return cursor.fetchall()




except Error as e:
    print("Error while connecting to MySQL", e)



def createUser(cpr, name, telephone, age, weight, fev1, GOLD, MRC):
    user_Patients = User_Patients(cpr, weight, fev1, GOLD, MRC)
    user_Person = User_Person(name, age, telephone, cpr)
    cursor = connection.cursor()
    query_Person = "INSERT INTO Person (name, age, telephone, cpr) VALUES (%s, %s, %s, %s)"
    values_Person = (user_Person.name, user_Person.age, user_Person.telephone, user_Person.cpr)
    query_Patients = "INSERT INTO Patients (cpr, weight, FEV1, GOLD, MRC) VALUES (%s, %s, %s, %s, %s)"
    values_Patients = (user_Patients.cpr, user_Patients.weight, user_Patients.fev1, user_Patients.GOLD, user_Patients.MRC)
    cursor.execute(query_Person, values_Person)
    cursor.execute(query_Patients, values_Patients)
    connection.commit()
    cursor.close()