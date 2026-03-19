import csv

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()