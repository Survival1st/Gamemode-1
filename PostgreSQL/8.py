def delete_by_name(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE first_name = %s",
        (name,)
    )

    conn.commit()
    conn.close()