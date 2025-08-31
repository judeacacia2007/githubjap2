 import sqlite3

 conn = sqlite3.connect("library.db")
 cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS books")
cursor.execute("DROP TABLE IF EXISTS members")
cursor.execute("DROP TABLE IF EXISTS borrowed")

cursor.execute("""
CREATE TABLE books(
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT
)
""")

cursor.execute("""
CREATE TABLE members(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("""
CREATE TABLE borrowed(
    member_id INTEGER,
    book_id INTEGER,
    FOREIGN KEY(member_id)REFERENCES members(id)
    FOREIGN KEY(book_id)REFERENCES books(id)
)
""")

books = [
    (1, "python basics", "guido"),
    (2, "SQL made easy", "E.F.codd")
    (3, "date science 101", "andrew ng")
]

members = [
    (1, "alice", 21,)
    (2, "bob", 23),
    (3, "charlie", 25)
]

borrowed = [
    (1,1),(2,2)
]

cursor.executemany("INSERT INTO books VALUES (?,?,?)",books)
cursor.executemany("INSERT INTO books VALUES (?,?,?)",members)
cursor.executemany("INSERT INTO books VALUES (?,?,?)",borrowed)

print("\nborrowed books:")
cursor.execute("""
SELECT members.name,books.title
FROM borrowed
JOIN members ON borrowed.member_id = members.id
JOIN books ON borrowed.book_id = books.id
""")

for row in cursor.fetchall():
    print(f"{row[0]} borrowed '{row[1]}'")

conn.commit()
conn.close()