#     ## Review Exercises

1. Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.

import sqlite3

# Yangi SQLite bazasini yaratamiz (fayl nomi: roster.db)
connection = sqlite3.connect("roster.db")

# Kursor obyektini yaratamiz
cursor = connection.cursor()

# Jadval yaratish so'rovi
create_table_query = """
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
"""

# So'rovni bajarish
cursor.execute(create_table_query)

# O'zgarishlarni saqlash
connection.commit()

# Ulashni yopish
connection.close()

print("Database va Roster jadvali yaratildi.")



2.  Populate your new table with the following values:    
| Name            | Species      | Age |
|-----------------|--------------|-----|
| Benjamin Sisko  | Human        |  40 |
| Jadzia Dax      | Trill        | 300 |
| Kira Nerys      | Bajoran      |  29 |

import sqlite3

data = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]

with sqlite3.connect('roster.db') as conn:
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)
    conn.commit()


3. Update the Name of Jadzia Dax to be Ezri Dax

cursor.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ('Ezri Dax', 'Jadzia Dax'))


4.  Display the Name and Age of everyone in the table classified as Bajoran.

select Name, Age
from roster
where Species = 'Bajoran';






