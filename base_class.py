import mysql.connector

class base:
    def __init__(self, table_name):
        self.table_name = table_name
        self.connection = mysql.connector.connect(
            user = "admin",
            password = "password",
            host = "68.64.164.98",
            database = "gatabase",
            port = "10108"
        )

    def id_search(self, id):
        self.cursor.execute("""
            SELECT *
            FROM {0}
            WHERE idRango = {1}
        """.format(self.table_name, id))

