def DispPokemon():
	tmp = sp.call('clear', shell=True)
	print("Select display condition: ")
	print("1. Type")
	print("2. Tier")
	print("3. Generation")
	print("4. Total Base Stats")
	print("5. Single stat and type")
	ch = int(input("Enter your choice : "))
	if ch == 1:
		#
	elif ch == 2:
		#
	elif ch == 3:
		#
	elif ch == 4:
		#
	elif ch == 5:
	else:
		print("Invalid option")

	getch = input("Press ENTER to return")

def SearchPokemon():
	tmp = sp.call('clear', shell=True)
	print("Select search condition : ")
	print("1. Name")
	print("2. PokedexID")
	ch = int(input("Enter your choice : "))
	if ch == 1:
	elif ch == 2:
	else:
		print("Invalid option")

	getch = input("Press ENTER to return")


def SearchMoves():
	tmp = sp.call('clear', shell=True)
	print("Select search condition :")
	print("1. Pokemon")
	print("2. Type")
	ch = int(input("Enter your choice :"))
	if ch == 1:
	elif ch == 2:
	else:
		print("Invalid option")

	getch = input("Press ENTER to return")

# Returns the weaknesses, resistances and immunities of the type/pokemon
def CheckEffect():
	tmp = sp.call('clear', shell=True)
	print("Select search condition : ")
	print("1. Type")
	print("2. Pokemon name")
	ch = int(input("Enter your choice :"))
	if ch == 1:
	elif ch == 2:
	else:
		print("Invalid option")

	getch = input("Press ENTER to return")

def DispChampion():
	
	getch = input("Press ENTER to return")

def AddChampion():
	getch = input("Press ENTER to return")

def EditChampion():
	getch = input("Press ENTER to return")

def RemoveChampion():
	getch = input("Press ENTER to return")

def DispLegendary():
	getch = input("Press ENTER to return")


# Main loop
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hard core username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='POKEBASE',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Press ENTER to continue")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
               	
                print("Welcome to the PokeBase!")
                print("Please enter your choice :")
                print("1. Display pokemon")
                print("2. Search pokemon")
                print("3. Search moves")
                print("4. Check effectiveness")
                print("5. Display champion builds")
                print("6. Add champion build")
                print("7. Edit champion build")
                print("8. Delete a champion build")
                print("9. Display legendary pokemon")
                print("10. Exit")
                ch = int(input("Enter your choice : "))
                tmp = sp.call('clear', shell=True)
                if ch == 1:
                	DispPokemon()
                elif ch == 2:
                	SearchPokemon()
                elif ch == 3:
                	SearchMoves()
                elif ch == 4:
                	CheckEffect()
                elif ch == 5:
                    DispChampion()
                elif ch == 6:
                	AddChampion()
                elif ch == 7:
                	EditChampion()
                elif ch == 8:
                	RemoveChampion()
                elif ch == 9:
                	DispLegendary()
               	elif ch == 10:
               		break
                else:
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")