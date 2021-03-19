# Write a python script to connect to a sqlite database using the following things using the linked documentation:
# https://docs.python.org/3/library/sqlite3.html (Links to an external site.)

import sqlite3
con = sqlite3.connect('example.db')

# Use IF NOT EXISTS to see if your three twitterclone tables are there
# if not, create them
# There is a slight difference in table creation when using sqlite versus postgresql
# https://sqlite.org/autoinc.html (Links to an external site.)

cur = con.cursor()

cur.execute('''CREATE TABLE[IF NOT EXISTS] twitteruser(
        id real, username text, password text, display_name text)''')
cur.execute('''INSERT INTO twitteruser VALUES (
        ('steve', 'hunter2', 'steve-o'),
        ('dave', 'asdf', 'davey'),
        ('bob', 'qwer', 'bobbinator'))''')
con.commit()
con.close()


cur.execute('''CREATE TABLE[IF NOT EXISTS] tweet(
        id real, fk_twitteruser real, body text, created_at real''')
cur.execute('''INSERT INTO tweet VALUES (
        (SELECT id FROM twitteruser WHERE username='steve'),
        'Hey, @bob', NOW())''')
con.commit()
con.close()


cur.execute('''CREATE TABLE[IF NOT EXISTS] notification(
        id real, fk_twitteruser real, fk_tweet real''')
cur.execute('''INSERT INTO notification VALUES (
        (SELECT id FROM twitteruser WHERE username='bob'),
        (SELECT id FROM tweet WHERE fk_twitteruser= (
            SELECT id FROM twitteruser WHERE username='steve'))''')
con.commit()
con.close()


# Use the Mimesis (Links to an external site.) package for Python to generate 500 new user accounts and insert them into your database (hint: mimesis supports passwords, usernames, and full names)



# Randomly select users and use the mimesis.Text.text() to create 1000 tweets and insert them into your database



# randomly select two users that are not the same, grab a tweet by one of them from the database, and generate 200 notifications and insert them into your database
