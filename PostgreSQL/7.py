def find_by_phone(phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE phone = %s",
        (phone,)
    )

    print(cur.fetchall())
    conn.close()