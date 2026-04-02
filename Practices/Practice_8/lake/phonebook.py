import psycopg2
from psycopg2 import extras
from config import load_config

def call_procedure(proc_name, params=None):
    config = load_config()
    if params is None:
        params = ()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                placeholders = ", ".join(["%s"] * len(params))
                
                if proc_name == "insert_many_contacts":
                    query = f"CALL {proc_name}(%s, %s, NULL)"
                    cur.execute(query, params)
                    result = cur.fetchone()
                    conn.commit()
                    return result[0] if result else None
                else:
                    query = f"CALL {proc_name}({placeholders})"
                    cur.execute(query, params)
                    conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        return None

def call_function(func_name, params=None):
    config = load_config()
    if params is None:
        params = ()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor(cursor_factory=extras.DictCursor) as cur:
                placeholders = ", ".join(["%s"] * len(params))
                query = f"SELECT * FROM {func_name}({placeholders})"
                cur.execute(query, params)
                return [dict(row) for row in cur.fetchall()]
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    call_procedure("upsert_contact", ("Ansar", "87751437232"))

    print("-----------------------------------")

    names = ['Sofia', 'Nurazamat', 'Sanzhar']
    phones = ['87075598777', '347', '87001163543']
    invalid_data = call_procedure("insert_many_contacts", (names, phones))
    if invalid_data:
        print(f"Invalid: {invalid_data}")

    print("-----------------------------------")

    search_results = call_function("get_contacts_by_pattern", ("Sa",))
    for row in search_results:
        print(row)

    print("-----------------------------------")

    page_data = call_function("get_contacts_paged", (5, 0))
    for row in page_data:
        print(row)
    
    print("-----------------------------------")

    
    # all_contacts = call_function("get_all_contacts")
    # for row in all_contacts:
    #     print(row)
