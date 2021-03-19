# Write a python script to connect to a sqlite database using the following things using the linked documentation:
# https://docs.python.org/3/library/sqlite3.html (Links to an external site.)

import sqlite3
import datetime
import mimesis
import random
conn = sqlite3.connect('example.db')

# Use IF NOT EXISTS to see if your three twitterclone tables are there
# if not, create them
# There is a slight difference in table creation when using sqlite versus postgresql
# https://sqlite.org/autoinc.html (Links to an external site.)

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS twitteruser(
        username VARCHAR(40) NOT NULL, password VARCHAR(40) NOT NULL, display_name VARCHAR(40) NOT NULL)''')

for i in range(500):
        c.execute(f"INSERT INTO twitteruser VALUES ('{mimesis.Person.username}', '{mimesis.Person.password}', '{mimesis.Person.first_name}')")


c.execute('''CREATE TABLE IF NOT EXISTS tweet(
        fk_twitteruser INT NOT NULL, body VARCHAR(140), created_at TIMESTAMP) ''')

for i in range(1000):
    c.execute(f"INSERT INTO tweet VALUES('{random.randint(0, 1000)}', '{mimesis.Text.text}', '{mimesis.Datetime.datetime}')")


c.execute('''CREATE TABLE IF NOT EXISTS notification(
        fk_twitteruser INT, fk_tweet INT)''')
# c.execute('''INSERT INTO notification VALUES (
#         (SELECT rowid FROM twitteruser WHERE username='bob'),
#         (SELECT rowid FROM tweet WHERE fk_twitteruser= (
#             SELECT rowid FROM twitteruser WHERE username='steve'))''')


for i in range(200):
    person_1 = {random.randint(0,1000)}
    person_2 = {random.randint(0,1000)}

    user_1 = c.execute(f'SELECT rowid FROM twitteruser WHERE rowid="{person_1}"')
    tweet = c.execute(f'SELECT rowid FROM tweet WHERE fk_twitteruser="{person_2}"')
    c.execute(f"INSERT INTO notification VALUES('{user_1}', '{tweet}')")
    

conn.commit()
conn.close()



# randomly select two users that are not the same, grab a tweet by one of them from the database, and generate 200 notifications and insert them into your database
