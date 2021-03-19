# Write a python script to connect to a sqlite database using the following things using the linked documentation:
# https://docs.python.org/3/library/sqlite3.html (Links to an external site.)

import sqlite3
con = sqlite3.connect('example.db')

# Use IF NOT EXISTS to see if your three twitterclone tables are there
# if not, create them
# There is a slight difference in table creation when using sqlite versus postgresql
# https://sqlite.org/autoinc.html (Links to an external site.)


CREATE TABLE [IF NOT EXISTS] twitteruser(
        id SERIAL NOT NULL PRIMARY KEY,
        username VARCHAR(40) NOT NULL,
        password VARCHAR(40)NOT NULL,
        display_name VARCHAR(40) NOT NULL
) [WITHOUT ROWID];

CREATE TABLE [IF NOT EXISTS] tweet(
        id SERIAL NOT NULL PRIMARY KEY,
        fk_twitteruser INT NOT NULL,
        body VARCHAR(140),
        created_at TIMESTAMP
) [WITHOUT ROWID];

CREATE TABLE [IF NOT EXISTS] notification(
        id SERIAL NOT NULL PRIMARY KEY,
        fk_twitteruser INT NOT NULL,
        fk_tweet INT NOT NULL
) [WITHOUT ROWID];

# Use the Mimesis (Links to an external site.) package for Python to generate 500 new user accounts and insert them into your database (hint: mimesis supports passwords, usernames, and full names)



# Randomly select users and use the mimesis.Text.text() to create 1000 tweets and insert them into your database



# randomly select two users that are not the same, grab a tweet by one of them from the database, and generate 200 notifications and insert them into your database