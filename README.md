# Welcome to PokeBase!
PokeBase is a tool designed to help pokemon fans of any level take their game to the next level. Our goal is to provide competitive pokemon information in a simple and intuitive format to everyone interested. Whether you simply want to check the weaknesses and resistances of Charizard, or want to build a killer set of moves for a pokemon we got you covered.

## Installation Instructions
PokeBase is written in python and uses mysql to store the data. We assume here that python-3 is already installed on your system.
### MySQL
To install MySQL server on Ubuntu, run the following commands
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

#### (Optional)
To create a new user, you may use the following command
```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```
At this stage the created user doesn't have access to the data. To allow access, you'll have to run a grant access query as below
```
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
```

With this you must be in a place to be able to use MySQL. Since this program has been made to work on top of the POKEBASE dataset, proceed to load the dataset using the following command within the mysql environment
```
source PokeBase.sql;
```
(Do ensure that you are running this command from the directory that contains the PokeBase.sql file)  

### Python
This program uses pymysql and PrettyTable. Both of these can be installed using any python library manager. We assume here that pip3 is already installed on your system.  
To install the necessary libraries run : 
```
pip3 install pymysql
pip3 install prettytable
```
At this point, we should be ready to start up PokeBase!!

## Running PokeBase
In your terminal use ``` python3 PokeBase.py ``` to run the program.
This should prompt you to enter your username and password (the mysql credentials you created earlier). If the credentials are valid you will enter PokeBase.  
### How do I use PokeBase?
PokeBase is designed to be a very intuitive CLI for pokemon players. Once you enter PokeBase you simply enter your choices and view the results on the terminal.
### What all can PokeBase do?
PokeBase was designed to appeal to all levels of pokemon players. Therefore it has functionality that ranges from very basic (read: listing legendary pokemon) to only applicable to professional players (sort pokemon based on type and SpA).
#### Display pokemon
You can choose to display pokemon based on type, tier, generation, total base stats and even choose to sort pokemon based on their type and a stat.
#### Search for Pokemon
You can search PokeBase for pokemon by their name or pokedex ID.
#### Search for moves
You can search for moves based on the name of the pokemon that can use them, or the type of the move.
####  Check effectiveness 
Given a pokemon or type, the program will return all the types that the given pokemon/types resistances, weaknesses and immunities.
#### Display champion builds
Champion builds are user defined collections of pokemon and moves. Here we can display all the champion builds that the user has created.
#### Add a champion build
If you come up with a brilliant combination of moves for a pokemon and wish to store it for later use, this is your chance!
#### Edit a champion build
If you feel like the champion build for a particular pokemon is in need of an update, you can always change its moves.
#### Delete a champion build
Although it is not advisable to delete a champion build (we love all pokemon equally!), we still provide you the functionality.
#### Display legendary pokemon
Read the lore of these magnificent beings and make your fellow pokemon trainers jealous for sure!
