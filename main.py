import mysql.connector
from ui import app

try:
    from mysql.connector import Error
    connection = mysql.connector.connect(
        user = "admin",
        password = "password",
        host = "68.64.164.98",
        database = "gatabase",
        port = "10108"
    )
    if connection.is_connected():
        print("Connected")
        
        app(connection)
        

except Error as ex:
    print("Not connected: ", ex)

finally:
    if connection.is_connected():
        connection.close()
        print("Ended connection")
