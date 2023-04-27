import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='KOLNET',
                                         user='root',
                                         password='Pye23rxj+')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select * from Patients")
        record = cursor.fetchall()
        CPR_list = [i[1] for i in record]
        def select(col, tabl, cond, var):
            cursor.execute(f"SELECT {col} FROM {tabl} WHERE {cond} = '{var}'")
            return cursor.fetchall()




except Error as e:
    print("Error while connecting to MySQL", e)


