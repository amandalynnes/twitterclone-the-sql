-- Query to create a table for twitterusers

CREATE TABLE twitteruser(
    id SERIAL NOT NULL PRIMARY KEY,
    username VARCHAR(40) NOT NULL,
    password VARCHAR(40)NOT NULL,
    display_name VARCHAR(40) NOT NULL
);

-- Query to create a table for tweets

CREATE TABLE tweet(
    id SERIAL NOT NULL PRIMARY KEY,
    fk_twitteruser INT NOT NULL,
    body VARCHAR(140),
    created_at TIMESTAMP
);

-- Query to create a table for notifications

CREATE TABLE notification(
    id SERIAL NOT NULL PRIMARY KEY,
    fk_twitteruser INT NOT NULL,
    fk_tweet INT NOT NULL
);

-- Query to create a new user (username: steve, password: hunter2, display name: steve-o)

INSERT INTO twitteruser (username, password, display_name)
VALUES ('steve', 'hunter2', 'steve-o');

/* Query to create two new users at once: 
 -username: dave, password: asdf, display name: davey
 -username: bob, password: qwer, display name: bobbinator */


 
-- Query to get the username and password of twitteruser ID 1



-- Query to get the ID of a user by the username of dave



-- Query to create a new tweet written by the user with the username steve (yes, you have to get the ID of Steve first -- hint: subqueries are your friend)



-- Query to get the count of tweets by username steve (hint: subqueries are your friend)



-- Query to get the date and text of all tweets by username steve (hint: subqueries are your friend)



-- Query to get the username and password of the username bob



-- Query to create a notification for username bob using the tweet written by username steve (hint: subqueries are your friend)



-- Query to get all IDs of notifications for bob (hint: subqueries are your friend)


-- EC: 

-- Extra Credit, 1pt: Query to delete a tweet starting when you already know the ID (use 1)



-- Extra Credit: 2pts: Single query to delete all the tweets belonging to username bob



/* Extra Credit: 5pts: Single query to output:
    Username of the person the notification is meant for (steve-o)
    username of the person who wrote the tweet that triggered the notification
    text of the tweet
    ...where the only piece of information you start with is the display name of Steve; "steve-o" */
