# Write a python script to connect to a sqlite database using the following things using the linked documentation:
# https://docs.python.org/3/library/sqlite3.html (Links to an external site.)

import sqlite3
import datetime

# import mimesis
from mimesis import Person, Text, Datetime
import random

conn = sqlite3.connect("example.db")
from random import randint

person = Person()
text = Text()
date = Datetime()

# Use IF NOT EXISTS to see if your three twitterclone tables are there
# if not, create them
# There is a slight difference in table creation when using sqlite versus postgresql
# https://sqlite.org/autoinc.html (Links to an external site.)

c = conn.cursor()

c.execute(
    """CREATE TABLE IF NOT EXISTS twitteruser(
        username TEXT NOT NULL, password TEXT NOT NULL, display_name TEXT NOT NULL)"""
)

c.execute(
    """CREATE TABLE IF NOT EXISTS tweet(
        fk_twitteruser INTEGER NOT NULL,
        body TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (fk_twitteruser) REFERENCES twitteruser(rowid) ON DELETE CASCADE) """
)

c.execute(
    """CREATE TABLE IF NOT EXISTS notification(
        fk_twitteruser INTEGER, fk_tweet INTEGER)"""
)

for i in range(500):
    c.execute(
        f"""INSERT INTO twitteruser VALUES ("{person.username()}", "{person.password(hashed=True)}", "{person.first_name()}")"""
    )

c.execute(f"""SELECT rowid FROM twitteruser""")
users = c.fetchall()
for i in range(1000):
    user = random.choice(users)
    c.execute(
        f"""INSERT INTO tweet VALUES(?, ?, ?)""",
        (user[0], text.text(), date.datetime()),
    )

for i in range(200):
    person_1 = random.randint(1, 500)
    person_2 = random.randint(1, 500)

    if person_1 == person_2:
        person_2 = random.randint(1, 500)

    c.execute(f"""SELECT rowid FROM twitteruser WHERE rowid="{person_1}" """)
    user_1 = c.fetchone()
    c.execute(f"""SELECT rowid FROM tweet WHERE fk_twitteruser="{person_2}" """)
    tweet = c.fetchone()

    if tweet:
        c.execute(f"""INSERT INTO notification VALUES("{user_1[0]}", "{tweet[0]}")""")
    else:
        person_1 = random.randint(1, 500)
        person_2 = random.randint(1, 500)

        if person_1 == person_2:
            person_2 = random.randint(1, 500)

        c.execute(f"""SELECT rowid FROM twitteruser WHERE rowid="{person_1}" """)
        user_1 = c.fetchone()
        c.execute(f"""SELECT rowid FROM tweet WHERE fk_twitteruser="{person_2}" """)
        tweet = c.fetchone()

        if tweet:
            c.execute(
                f"""INSERT INTO notification VALUES("{user_1[0]}", "{tweet[0]}")"""
            )


conn.commit()
conn.close()

