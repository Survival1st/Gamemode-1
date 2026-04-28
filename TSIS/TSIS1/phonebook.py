import psycopg2
import json
import csv
from config import load_config

# ------------------ DB CORE ------------------

def execute(sql, params=None, fetch=False):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                if fetch:
                    return cur.fetchall()
                conn.commit()
    except Exception as e:
        print("DB error:", e)

# ------------------ SCHEMA ------------------

def create_tables():
    execute("""
    CREATE TABLE IF NOT EXISTS groups(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    execute("""
    CREATE TABLE IF NOT EXISTS contacts(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) UNIQUE NOT NULL,
        email VARCHAR(100),
        birthday DATE,
        group_id INTEGER REFERENCES groups(id)
    );
    """)

    execute("""
    CREATE TABLE IF NOT EXISTS phones(
        id SERIAL PRIMARY KEY,
        contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
        phone VARCHAR(20) NOT NULL,
        type VARCHAR(10) CHECK (type IN ('home','work','mobile'))
    );
    """)

    print("Tables created")

# ------------------ INSERT ------------------

def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    group = input("Group: ")

    execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT DO NOTHING", (group,))
    group_id = execute("SELECT id FROM groups WHERE name=%s", (group,), True)[0][0]

    execute("""
    INSERT INTO contacts(name,email,birthday,group_id)
    VALUES(%s,%s,%s,%s)
    ON CONFLICT (name) DO NOTHING
    """, (name, email, birthday, group_id))

    print("Contact added")

def add_phone():
    name = input("Contact name: ")
    phone = input("Phone: ")
    ptype = input("Type (home/work/mobile): ")

    execute("CALL add_phone(%s,%s,%s)", (name, phone, ptype))

# ------------------ SEARCH ------------------

def search():
    query = input("Search: ")
    rows = execute("SELECT * FROM search_contacts(%s)", (query,), True)

    for r in rows:
        print(r)

# ------------------ FILTER + SORT + PAGINATION ------------------

def list_contacts():
    group = input("Filter group (or empty): ")
    sort = input("Sort by (name/birthday): ")

    sql = """
    SELECT c.name, c.email, c.birthday, g.name
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    """

    params = []

    if group:
        sql += " WHERE g.name=%s"
        params.append(group)

    if sort in ["name", "birthday"]:
        sql += f" ORDER BY c.{sort}"

    rows = execute(sql, tuple(params), True)

    page_size = 3
    page = 0

    while True:
        start = page * page_size
        chunk = rows[start:start+page_size]

        if not chunk:
            print("No more data")
            break

        print("\n--- PAGE", page+1, "---")
        for r in chunk:
            print(r)

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            page += 1
        elif cmd == "prev" and page > 0:
            page -= 1
        else:
            break

# ------------------ JSON EXPORT ------------------

def export_json():
    data = execute("""
    SELECT c.name, c.email, c.birthday, g.name,
           p.phone, p.type
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON p.contact_id = c.id
    """, fetch=True)

    result = []
    for row in data:
        result.append({
            "name": row[0],
            "email": row[1],
            "birthday": str(row[2]),
            "group": row[3],
            "phone": row[4],
            "type": row[5]
        })

    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    print("Exported to JSON")

# ------------------ JSON IMPORT ------------------

def import_json():
    with open("contacts.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for c in data:
        exists = execute("SELECT id FROM contacts WHERE name=%s",
                         (c["name"],), True)

        if exists:
            choice = input(f"{c['name']} exists. skip/overwrite? ")

            if choice == "skip":
                continue
            else:
                execute("DELETE FROM contacts WHERE name=%s", (c["name"],))

        execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT DO NOTHING",
                (c["group"],))

        gid = execute("SELECT id FROM groups WHERE name=%s",
                      (c["group"],), True)[0][0]

        execute("""
        INSERT INTO contacts(name,email,birthday,group_id)
        VALUES(%s,%s,%s,%s)
        """, (c["name"], c["email"], c["birthday"], gid))

        execute("CALL add_phone(%s,%s,%s)",
                (c["name"], c["phone"], c["type"]))

    print("Imported JSON")

# ------------------ CSV IMPORT ------------------

def import_csv(file):
    with open(file, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT DO NOTHING",
                    (row["group"],))

            gid = execute("SELECT id FROM groups WHERE name=%s",
                          (row["group"],), True)[0][0]

            execute("""
            INSERT INTO contacts(name,email,birthday,group_id)
            VALUES(%s,%s,%s,%s)
            ON CONFLICT DO NOTHING
            """, (row["name"], row["email"], row["birthday"], gid))

            execute("CALL add_phone(%s,%s,%s)",
                    (row["name"], row["phone"], row["type"]))

    print("CSV imported")

# ------------------ MENU ------------------

def menu():
    while True:
        print("""
1. Add contact
2. Add phone
3. Search
4. List (filter/sort/pagination)
5. Export JSON
6. Import JSON
7. Import CSV
0. Exit
""")

        c = input("> ")

        if c == "1":
            add_contact()
        elif c == "2":
            add_phone()
        elif c == "3":
            search()
        elif c == "4":
            list_contacts()
        elif c == "5":
            export_json()
        elif c == "6":
            import_json()
        elif c == "7":
            import_csv("contacts.csv")
        elif c == "0":
            break

# ------------------ RUN ------------------

if __name__ == "__main__":
    create_tables()
    menu()