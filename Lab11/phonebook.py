import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="admin"
)
cur = conn.cursor()

#1
# cur.execute("""
#     CREATE OR REPLACE FUNCTION search_users(pattern TEXT)
#     RETURNS TABLE(id INT, name VARCHAR(255), phone VARCHAR(255))
#     AS $$
#     BEGIN
#         RETURN QUERY
#         SELECT * FROM users
#         WHERE users.phone ILIKE '%' || pattern || '%';   
#     END;
#     $$ LANGUAGE plpgsql;
# """)
# conn.commit()

# cur.execute("""
#     SELECT * FROM search_users('701');
# """)
# print(cur.fetchone())
# conn.commit()

#2
# cur.execute("""
#     CREATE OR REPLACE FUNCTION insert_user(p_name VARCHAR(255), p_phone VARCHAR(255))
#     RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR)
#     AS $$
#     BEGIN
#         IF EXISTS (SELECT 1 FROM users WHERE users.name = p_name) THEN
#             RETURN QUERY
#             UPDATE users
#             SET phone = p_phone
#             WHERE users.name = p_name
#             RETURNING users.id, users.name, users.phone;
#         ELSE
#             RETURN QUERY
#             INSERT INTO users(name, phone)
#             VALUES (p_name, p_phone)
#             RETURNING users.id, users.name, users.phone;
#         END IF;
#     END;
#     $$ LANGUAGE plpgsql;
# """)
# conn.commit()

# cur.execute("""
#     SELECT * FROM insert_user('Jack', '81111111111');
# """)
# print(cur.fetchone())
# conn.commit()

#3
# list_users = [['Robert', '81234567890'], ['Mark', '89876543210'], ['Ben', '12345678900']]
# cur.execute("""
#     CREATE OR REPLACE FUNCTION insert_list_users(user_list TEXT[][])
#     RETURNS TABLE(name TEXT, phone TEXT)
#     AS $$
#     DECLARE
#         i INT := 1;
#         u_name TEXT;
#         u_phone TEXT;
#     BEGIN
#         WHILE i <= array_length(user_list, 1) LOOP
#             u_name := user_list[i][1];
#             u_phone := user_list[i][2];

#             IF LEFT(u_phone, 1) = '8' THEN
#                 INSERT INTO users(name, phone)
#                 VALUES (u_name, u_phone);
#             ELSE
#                 name := u_name;
#                 phone := u_phone;
#                 RETURN NEXT;
#             END IF;

#             i := i + 1;
#         END LOOP;
#     END;
#     $$ LANGUAGE plpgsql;
# """)
# conn.commit()
# cur.execute("SELECT * FROM insert_list_users(%s)", (list_users,))
# conn.commit()
# print(cur.fetchone())

#4
# cur.execute("""
#     CREATE OR REPLACE FUNCTION get_users_page(p_limit INT, p_offset INT)
#     RETURNS TABLE(id INT, name VARCHAR(255), phone VARCHAR(255))
#     AS $$
#     BEGIN
#         RETURN QUERY
#         SELECT users.id, users.name, users.phone
#         FROM users
#         ORDER BY id
#         LIMIT p_limit
#         OFFSET p_offset;
#     END;
#     $$ LANGUAGE plpgsql;
# """)
# conn.commit()
# limit = 5
# offset = 5
# cur.execute("SELECT * FROM get_users_page(%s, %s)", (limit, offset))
# conn.commit()
# x = cur.fetchall()
# for row in x:
#     print(row)

#5
cur.execute("""
    CREATE OR REPLACE FUNCTION delete_user(p_name VARCHAR(255))
    RETURNS TABLE(id INT, name VARCHAR(255), phone VARCHAR(255))
    AS $$
    BEGIN
        RETURN QUERY
        DELETE FROM users
        WHERE users.name = p_name
        RETURNING users.id, users.name, users.phone;
    END;
    $$ LANGUAGE plpgsql;
""")
conn.commit()
cur.execute("SELECT * FROM delete_user('Mark');")
conn.commit()
print(cur.fetchone())