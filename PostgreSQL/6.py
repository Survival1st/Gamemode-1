def find_by_name(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE first_name = %s",
        (name,)
    )

    print(cur.fetchall())
    conn.close()