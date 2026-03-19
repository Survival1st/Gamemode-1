import psycopg2
from config import load_config

def create_tables():
    commands = (
        """
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
    )
    try:
        params = load_config()
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                print("Таблица 'vendors' успешно создана!")
    except Exception as error:
        print(f"Ошибка: {error}")

if __name__ == '__main__':
    create_tables()