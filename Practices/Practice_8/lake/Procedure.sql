CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
AS $$
BEGIN
    INSERT INTO lake (name, phone)
    VALUES (p_name, p_phone)
    ON CONFLICT (name) 
    DO UPDATE SET phone = EXCLUDED.phone;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names VARCHAR[], 
    p_phones VARCHAR[],
    OUT p_invalid_data TEXT[]
)
AS $$
DECLARE
    i INTEGER;
    invalid_list TEXT[] := '{}';
BEGIN
    FOR i IN 1 .. array_upper(p_names, 1) LOOP
        IF p_phones[i] ~ '^[0-9]{11}$' THEN
            INSERT INTO lake (name, phone)
            VALUES (p_names[i], p_phones[i])
            ON CONFLICT (name) DO UPDATE SET phone = EXCLUDED.phone;
        ELSE
            invalid_list := array_append(invalid_list, p_names[i] || ':' || p_phones[i]);
        END IF;
    END LOOP;
    p_invalid_data := invalid_list;
END;
$$ LANGUAGE plpgsql;