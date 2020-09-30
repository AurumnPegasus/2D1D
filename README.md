## Installation Instructions

I trust that the students reading this are all at a respectable age to be able to handle installation bugs themselves and won't be needing the TAs to help them. 

### MySQL

Although you haven't strictly been told to explicitly use MySQL it is highly recommended. To install MySQL server on Ubuntu, run the following commands

```
sudo apt-get update
sudo apt-get install mysql-server
```

When installing the MySQL server for the first time, it will prompt for a root password that you can later login with. 

The start command is
```
mysql -u <user_name> -p <password>
```

If for some reason, you aren't asked for the password during installation, try prepending the start command with sudo and provide your root password. You can now set a root password or create a new user. 

Here, I would also like to point out that if your application involves a login or some form of authentication, you may do so using the USER table of the MYSQL database that exists by default. 

To create a new user, you may use the following command
```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```
At this stage the created user doesn't have access to the data. To allow access, you'll have to run a grant access query as below
```
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
```

It is also possible to grant a new user access to only one database or some tables of a database. If your application involves different user types with different access clearences, you may use this feature.

With this you must be in a place to be able to play around with MySQL. Since this template has been made to work on top of the POKEBASE dataset, proceed to load the dataset using the following command within the mysql environment
```
source path_to_POKEBASE.sql;
```

### To Run
To run the code, you will need to login with a username and password(your MYSQL username and password) which has access to the COMPANY database.

```
python3 boilerPlate.py
```

This will prompt for you to enter your username and password.

