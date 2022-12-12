def select(cursor, title):

    cursor.execute("SELECT * FROM " + title)
    results = cursor.fetchall()

    return [title, list(cursor.column_names), list(results)]

def getAllTables(cursor):
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'gatabase'")
    results = cursor.fetchall()

    y = [x[0] for x in results]

    return y
