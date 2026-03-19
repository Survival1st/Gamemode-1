import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="your_password"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(20) UNIQUE
);
""")

conn.commit()
cur.close()
conn.close()