import mysql.connector

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
        #info = connection.get_server_info()
        #print(info)
        cursor = connection.cursor()
        cursor.execute("SELECT database();")
        database = cursor.fetchone()
        cursor.execute("SELECT * FROM RANGO")
        results = cursor.fetchall()
        print(cursor.column_names)

        #SELECT SAMPLE
        for res in results:
            print (res)
        print("Rows: ", cursor.rowcount)
        #INSERT
        '''i1 = input("Ingrese nombre de nuevo rango: ")
        i2 = input("Ingrese descuento unico: ")
        i3 = input("Ingrese descripcion: ")
        cursor.execute("INSERT INTO RANGO (nombre, descuento_unico, beneficios) VALUES ('Brillantina', 10, 'Brillitos para tus compras')")
        connection.commit()
        print("Brillante sonrisa colgate")'''
        #DELETE

        #UPDATE

        
        print(database)
except Error as ex:
    print("Not connected: ", ex)

finally:
    if connection.is_connected():
        connection.close()
        print("Ended connection")
