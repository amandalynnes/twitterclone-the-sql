import sqlite3
conn = sqlite3.connect('trial.db')
c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#             first text,
#             last text,
#             pay integer
#             )""")

# c.execute("INSERT INTO employees VALUES ('willie', 's', 10000000)")

c.execute("SELECT * FROM employees WHERE last = 's'")

print(c.fetchall())

conn.commit()

conn.close()
