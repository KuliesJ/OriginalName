import mysql.connector
from mysql.connector import Error

class Rango:
    def __init__(self, idRango, nombre, descuento, beneficio):
        self.idRango = idRango
        self.nombre = nombre
        self.descuento = descuento
        self.beneficio = beneficio
        self.connection = mysql.connector.connect(
            user = "admin",
            password = "password",
            host = "68.64.164.98",
            database = "gatabase",
            port = "10108"
        )
        self.cursor = self.connection.cursor()

    def load_rank(self, idNumber):
        self.cursor.execute("""
            SELECT *
            FROM RANGO
            WHERE idRango = {}
        """.format(idNumber))

    def insert_rank(self):
        self.cursor.execute("""
            INSERT INTO RANGO VALUES
            ({}, '{}', {}, '{}')
        """.format(self.idRango, self.nombre, self.descuento, self.beneficio)
        )
        self.connection.commit()
        

def insert():
    r1 = Rango(10, "Sandia", 10, "Pepitas")
    r1.insert_rank()

try:

    connection = mysql.connector.connect(
        user = "admin",
        password = "password",
        host = "68.64.164.98",
        database = "gatabase",
        port = "10108"
    )
    if connection.is_connected():
        print("Connected")
        #info = connection.get_server_info()
        #print(info)
        cursor = connection.cursor()
        insert()

except Error as ex:
    print("Not connected: ", ex)

finally:
    if connection.is_connected():
        connection.close()  # Se cerró la conexión a la BD.
        print("Ended connection")
