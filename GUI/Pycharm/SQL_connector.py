import mysql.connector
from mysql.connector import Error
from User import User

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
    user = User(cpr, name, telephone, age, weight, fev1, GOLD, MRC)
    cursor = connection.cursor()
    query = "INSERT INTO Patients (cpr, name, telephone, age, weight, FEV1, GOLD, MRC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (user.cpr, user.name, user.telephone, user.age, user.weight, user.fev1, user.GOLD, user.MRC)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()