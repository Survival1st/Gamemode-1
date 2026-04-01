import psycopg2
from Practices.Practice_8.lake.config import load_config


def call_procedure(proc_name, params):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if proc_name == "insert_many_contacts":
                    
                    cur.execute(f"CALL {proc_name}(%s, %s, NULL)", params)
                    invalid_data = cur.fetchone()[0]
                    conn.commit()
                    return invalid_data
                else:
                    
                    cur.execute(f"CALL {proc_name}(%s, %s)", params) if len(params) > 1 else cur.execute(f"CALL {proc_name}(%s)", params)
                    conn.commit()
    except Exception as e:
        print(f"Процедура қатесі: {e}")


def call_function(func_name, params):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if len(params) > 1:
                    cur.execute(f"SELECT * FROM {func_name}(%s, %s)", params)
                else:
                    cur.execute(f"SELECT * FROM {func_name}(%s)", params)
                return cur.fetchall()
    except Exception as e:
        print(f"Функция қатесі: {e}")
        return []


if __name__ == "__main__":
    
    print("--- 1. Қосу/Жаңарту орындалуда... ---")
    call_procedure("upsert_contact", ("Meirzhan", "87071112233"))

    
    print("\n--- 3. Топтық енгізу (Валидациямен) ---")
    names = ['Alikhan', 'Nurbek', 'Sanzhar']
    phones = ['87075556677', '777', '87001112233'] 
    invalid = call_procedure("insert_many_contacts", (names, phones))
    if invalid:
        print("Қате болғандықтан енгізілмегендер:", invalid)

    
    print("\n--- 4. Іздеу нәтижесі ('Ali' бойынша) ---")
    search_results = call_function("get_contacts_by_pattern", ("Ali",))
    for row in search_results:
        print(row)

    
    print("\n--- 5. Пагинация (Limit: 5, Offset: 0) ---")
    page = call_function("get_contacts_paged", (5, 0))
    for row in page:
        print(row)