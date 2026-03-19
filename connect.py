import psycopg2

def connect():
    # Твои данные, которые мы проверили
    params = {
        "host": "localhost",
        "database": "suppliers",
        "user": "postgres",
        "password": "human1or6"
    }

    try:
        print("Пробую подключиться...")
        # Устанавливаем соединение
        conn = psycopg2.connect(**params)
        
        # Создаем курсор
        cur = conn.cursor()
        
        # Выполняем тестовый запрос
        cur.execute("SELECT version();")
        record = cur.fetchone()
        
        print(f"Подключение успешно! Версия базы: {record}")
        
        # Закрываем всё
        cur.close()
        conn.close()
        print("Соединение закрыто.")

    except Exception as e:
        print(f"Не удалось подключиться: {e}")

if __name__ == "__main__":
    connect()