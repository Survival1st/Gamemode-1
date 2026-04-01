import psycopg2
from Practices.Practice_8.lake.config import load_config

def connect():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    connect()