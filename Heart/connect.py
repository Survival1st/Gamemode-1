import psycopg2
from config import load_config

def connect(config):
    """ Подключение к серверу базы данных PostgreSQL """
    conn = None
    try:
        # Считываем параметры
        print('Connecting to the PostgreSQL database...')
        
        # Подключаемся к серверу
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
            
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    config = load_config()
    connect(config)