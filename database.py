def select(cursor, title):

    cursor.execute("SELECT * FROM " + title)
    results = cursor.fetchall()

    return [title, list(cursor.column_names), list(results)]

def getAllTables(cursor):
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'gatabase'")
    results = cursor.fetchall()

    y = [x[0] for x in results]

    return y

def insert(connector, l):
    title = l[0]
    columns = l[1]
    data = l[2]

    txt1 = ""
    for i in range(len(columns) - 1):
        txt1 += columns[i] + ', '
    txt1 += columns[-1]

    txt2 = ""
    for i in range(len(data) - 1):
        txt2 += data[i] + ', '
    txt2 += data[-1]

    cursor = connector.cursor()
    cursor.execute("INSERT INTO " + title + "(" + txt1 + ") VALUES (" + txt2 + ")")

    connector.commit()

def getTableInfo(cursor, title):

    cursor.execute("SELECT COLUMN_NAME, DATA_TYPE from INFORMATION_SCHEMA.COLUMNS where table_schema = 'gatabase' and table_name = '" + title + "'")
    r = cursor.fetchall()

    return [list(cursor.column_names), list(r)]
