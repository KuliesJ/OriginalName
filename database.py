def selectExample(cursor, title):

    cursor.execute("SELECT * FROM " + title)
    results = cursor.fetchall()

    return [title, list(cursor.column_names), list(results)]