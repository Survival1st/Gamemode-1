import psycopg2

# 1. Настройки подключения
DB_CONFIG = {
    "host": "localhost",
    "database": "suppliers",
    "user": "postgres",
    "password": "your_password"
}

def init_db():
    """Создает таблицу, если она еще не существует"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50),
            phone_number VARCHAR(20) NOT NULL
        )
        """,
    )
    conn = None
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                conn.commit()
                print("База данных готова к работе.")
    except Exception as e:
        print(f"Ошибка при инициализации: {e}")

def add_contact(f_name, l_name, phone):
    """Добавляет новый контакт в таблицу"""
    sql = "INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s);"
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (f_name, l_name, phone))
                conn.commit()
                print(f"Контакт {f_name} успешно добавлен!")
    except Exception as e:
        print(f"Ошибка при добавлении: {e}")

def get_all_contacts():
    """Выводит все контакты на экран"""
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT first_name, last_name, phone_number FROM phonebook;")
                rows = cur.fetchall()
                print("\n--- Список контактов ---")
                for row in rows:
                    print(f"{row[0]} {row[1]}: {row[2]}")
    except Exception as e:
        print(f"Ошибка при чтении: {e}")

# --- ЗАПУСК ---
if __name__ == "__main__":
    init_db()  # Создаем таблицу
    
    # Пример использования
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите номер: ")
    
    add_contact(name, surname, phone)
    get_all_contacts()