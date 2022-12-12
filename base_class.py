import mysql.connector

class base:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user = "admin",
            password = "password",
            host = "68.64.164.98",
            database = "gatabase",
            port = "10108"
        )
        self.cursor = self.connection.cursor()

