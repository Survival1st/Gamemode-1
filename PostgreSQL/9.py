def delete_by_phone(phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE phone = %s",
        (phone,)
    )

    conn.commit()
    conn.close()