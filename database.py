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
    
def getTablePK(cursor, title):

    cursor.execute("""SELECT k.column_name
FROM information_schema.table_constraints t
JOIN information_schema.key_column_usage k
USING(constraint_name,table_schema,table_name)
WHERE t.constraint_type='PRIMARY KEY'
  AND t.table_schema='gatabase'
  AND t.table_name='USUARIO' AND k.column_name <> ALL(SELECT
    q.column_name
FROM
    information_schema.table_constraints u
JOIN information_schema.key_column_usage q USING(
        CONSTRAINT_NAME,
        table_schema,
        TABLE_NAME
    )
WHERE
    u.constraint_type = 'FOREIGN KEY' AND u.table_schema = 'gatabase' AND u.table_name = 'USUARIO');""")
    r = cursor.fetchall()

    return r[0][0]

def delete(connector, l):
    title = l[0]
    pk = l[1]
    cond = l[2]

    cursor = connector.cursor()
    cursor.execute("DELETE FROM " + title + " WHERE " + pk + "=" + cond)

    connector.commit()

def execute(cursor, cond):
    cursor.execute(cond)
    results = cursor.fetchall()

    return [list(cursor.column_names), list(results)]
