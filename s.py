import sqlite3

# File names
sql_file = "restaurants.sql"
db_file = "restaurants.db"

# Connect to SQLite database (creates .db if not exists)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Read SQL file
with open(sql_file, "r") as file:
    sql_script = file.read()

# Execute SQL script
cursor.executescript(sql_script)

# Commit changes and close connection
conn.commit()
conn.close()

print("restaurants.sql successfully converted to restaurants.db")
