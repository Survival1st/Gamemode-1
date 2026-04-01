CREATE OR REPLACE FUNCTION get_contacts_by_pattern(search_pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$ 
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.phone 
    FROM phonebook p
    WHERE p.name ILIKE '%' || search_pattern || '%' 
       OR p.phone ILIKE '%' || search_pattern || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_paged(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$ 
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.phone 
    FROM phonebook p
    ORDER BY p.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;