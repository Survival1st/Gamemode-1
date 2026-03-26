import psycopg2
import csv
from config import load_config

def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS phonebook
    (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL
    )
    """
    execute_query(sql)
    print("Таблица успешно создана")

def insert_data_by_consol():
    name = input()
    num = input()
    sql = "INSERT INTO phonebook(name,phone_number) VALUES(%s,%s)"
    execute_query(sql,(name,num))

def insert_data_from_csv(file_path):
    sql = "INSERT INTO phonebook(name,phone_name) VALUES(%s,%s)"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(file_path,'r',encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        cur.execute(sql,row)
                    conn.commit()
        print(f"Cose succesfully work by path{file_path}")        
    except Exception as e:
        print(f"Error {e}")

def update_data():
    old_name = input()
    new_num = input()
    sql = "UPDATE TABLE Phonebook SET phone_number = %s WHERE name = %s"
    execute_query(sql,(new_num,old_name))
    print("Succesfully work")

def search_to_insert():
    sql = "SELECT * FROM Phonebook WHERE name LIKE %s"
    search = input()
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql,(f'%{search}%'))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except Exception as e:
        print(f"Error {e}")

def delete():
    name = input()
    sql = "DELETE FROM phonebook WHERE name=%s"
    execute_query(sql,(name))
    print("Succesfully work")

def execute_query(sql,params=None):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql,params)
                conn.commit()
    except Exception as e:
        print(f'BD error{e}')

if __name__ == "__main__":
    create_table()
    insert_data_by_consol()
    insert_data_from_csv()
    execute_query()
    delete()
    search_to_insert()
    update_data()