import psycopg2
import csv

#connecting to default db
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="admin"
)

cur = conn.cursor()

#creating users table
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        phone VARCHAR(255)
    )
""")
conn.commit()

#inserting users
# cur.execute("""
#     INSERT INTO users (name, phone)
#     VALUES
#     ('John', '87017773322'),
#     ('Alice', '87176664454'),
#     ('George', '87773452123'),
#     ('Anna', '87452342121'),
#     ('Conor', '87074561223');
# """)
# conn.commit()

#inserting users from csv file
# with open("Lab10//PhoneBook//users.csv", newline='', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         cur.execute(
#             "INSERT INTO users (name, phone) VALUES (%s, %s)",
#             (row['name'], row['phone'])
#         )

# conn.commit()

#updating user data
# cur.execute("""
#     UPDATE users
#     SET name = 'Pete'
#     WHERE name = 'CsvUser'
# """)
# conn.commit()

#querying data from users table
# cur.execute("""
#     SELECT * FROM users
#     WHERE name = 'Anna'
# """)
# conn.commit()

#deleting users 
cur.execute("""
    DELETE FROM users
    WHERE phone = '87074561223' 
""") 
conn.commit()

cur.close()
conn.close()