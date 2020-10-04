import subprocess as sp
import pymysql
import pymysql.cursors
from prettytable import PrettyTable

def DispPokemon():
	try:
		tmp = sp.call('clear', shell=True)
		print("Select display condition: ")
		print("1. Type")
		print("2. Tier")
		print("3. Generation")
		print("4. Total Base Stats")
		print("5. Single stat and type")
		ch = int(input("Enter your choice : "))
		if ch == 1:
			print("Valid types are :\nNormal\t\tFighting\tBug\nDark\t\tDragon\t\tElectric\nFairy\t\tFire\t\tFlying\nGhost\t\tGrass\t\tGround\nIce\t\tPoison\t\tPsychic\nRock\t\tSteel\t\tWater\n")
			type = input("Enter type (First letter capitalized ex: Fire): ")
			query = "SELECT P.PokedexID, N.Name, P.Generation, P.Tier, P.EvolvesFrom, T.Type1, T.Type2 FROM POKEMON AS P, POKENAME AS N, POKETYPE AS T WHERE P.PokedexID = N.PokedexID AND P.PokedexID = T.PokedexID AND (T.Type1 = '%s' OR T.Type2 = '%s')" % (type, type)
			cur.execute(query)
			rows = cur.fetchall()
			printlist(rows)
   			
			
		elif ch == 2:
			print("Valid Tiers are are : OU\tRU\tNU\tUBER")
			tier = input("Enter Tier: ")
			query = "SELECT P.PokedexID, N.Name, P.Generation, P.Tier, P.EvolvesFrom, T.Type1, T.Type2 FROM POKEMON AS P, POKENAME AS N, POKETYPE AS T WHERE P.PokedexID = N.PokedexID AND P.PokedexID = T.PokedexID AND P.Tier = '%s'" % (tier)
			cur.execute(query)
			rows = cur.fetchall()
			printlist(rows)
   
		elif ch == 3:
			print("Valid Generations are are : (1, 2, 3, 4, 5, 6, 7, 8)")
			generation = int(input("Enter Generation: "))
			query = "SELECT P.PokedexID, N.Name, P.Generation, P.Tier, P.EvolvesFrom, T.Type1, T.Type2 FROM POKEMON AS P, POKENAME AS N, POKETYPE AS T WHERE P.PokedexID = N.PokedexID AND P.PokedexID = T.PokedexID AND P.Generation = %d" % (generation)
			cur.execute(query)
			rows = cur.fetchall()
			printlist(rows)

		elif ch == 4:
			TBS = int(input("Enter minimum total base stats: "))
			query = query = "SELECT P.PokedexID, N.Name, P.Generation, P.Tier, P.EvolvesFrom, T.Type1, T.Type2, S.HP+S.Atk+S.Def+S.SpA+S.SpD+S.Spe AS TBS FROM POKEMON AS P, POKENAME AS N, POKETYPE AS T, STATS AS S WHERE P.PokedexID = N.PokedexID AND P.PokedexID = T.PokedexID AND P.PokedexID = S.PokedexID AND S.HP+S.Atk+S.Def+S.SpA+S.SpD+S.Spe >= %d" % (TBS)
			cur.execute(query)
			rows = cur.fetchall()
			printlist(rows)

		elif ch == 5:
			print("Valid types are :\nNormal\t\tFighting\tBug\nDark\t\tDragon\t\tElectric\nFairy\t\tFiret\t\tFlying\nGhost\t\tGrass\t\tGround\nIce\t\tPoison\t\tPsychic\nRock\t\tSteel\t\tWater\n")
			type = input("Enter type (First letter capitalized ex: Fire): ")
			print("Valid stats are :\nHP\tAtk\tDef\nSpA\tSpD\tSpe")
			stat = input("Enter stat (First letter capitalized ex: Atk): ")
			query = "SELECT P.PokedexID, N.Name, P.Generation, P.Tier, P.EvolvesFrom, T.Type1, T.Type2, S.%s FROM POKEMON AS P, POKENAME AS N, POKETYPE AS T, STATS AS S WHERE P.PokedexID = N.PokedexID AND P.PokedexID = T.PokedexID AND P.PokedexID = S.PokedexID AND (T.Type1 = '%s' OR T.Type2 = '%s') ORDER BY S.%s DESC" % (stat, type, type, stat)
			cur.execute(query)
			rows = cur.fetchall()
			printlist(rows)
   
		else:
			print("Invalid option")
	except:
		print("Error in displaying pokemon")
	getch = input("Press ENTER to return")



def SearchPokemon():
	try:
		tmp = sp.call('clear', shell=True)
		print("Select search condition : ")
		print("1. Name")
		print("2. PokedexID")
		ch = int(input("Enter your choice : "))
		if ch == 1:
			name = input("Enter name of pokemon : ")
			query = "SELECT P.PokedexID, N.Name, P.Generation, P.Tier, P.EvolvesFrom, T.Type1, T.Type2 FROM POKEMON AS P, POKENAME AS N, POKETYPE AS T WHERE P.PokedexID = N.PokedexID AND P.PokedexID = T.PokedexID AND N.Name = '%s'" % (name)
			cur.execute(query)
			rows = cur.fetchall()
			printlist(rows)


		elif ch == 2:
			PokedexID = int(input("Enter PokedexID of pokemon : "))
			query = "SELECT P.PokedexID, N.Name, P.Generation, P.Tier, P.EvolvesFrom, T.Type1, T.Type2 FROM POKEMON AS P, POKENAME AS N, POKETYPE AS T WHERE P.PokedexID = N.PokedexID AND P.PokedexID = T.PokedexID AND P.PokedexID = '%d'" % (PokedexID)
			cur.execute(query)
			rows = cur.fetchall()
			printlist(rows)

		else:
			print("Invalid option")
	except:
		print("Failed to show pokemon")

	getch = input("Press ENTER to return")


def SearchMoves():
	try:	
		tmp = sp.call('clear', shell=True)
		print("Select search condition :")
		print("1. Pokemon")
		print("2. Type")
		ch = int(input("Enter your choice :"))
		if ch == 1:
			pokemon = input("Enter the name of the pokemon : ")
			query = "SELECT M.Name, M.Description, M.Accuracy, M.Category, M.PP, M.Power, M.Type FROM MOVES AS M, POKEMOVES AS PM, POKENAME AS P WHERE P.Name = '%s' AND P.PokedexID = PM.PokedexID AND PM.Move = M.Name" % (pokemon)
			cur.execute(query)
			rows = cur.fetchall()
			printlist(rows)

		elif ch == 2:
			print("Valid types are :\nNormal\t\tFighting\tBug\nDark\t\tDragon\t\tElectric\nFairy\t\tFiret\t\tFlying\nGhost\t\tGrass\t\tGround\nIce\t\tPoison\t\tPsychic\nRock\t\tSteel\t\tWater\n")
			type = input("Enter type (First letter capitalized ex: Fire): ")
			query = "SELECT M.Name, M.Description, M.Accuracy, M.Category, M.PP, M.Power FROM MOVES AS M WHERE M.Type = '%s'" % (type)
			cur.execute(query)
			rows = cur.fetchall()
			printlist(rows)

		else:
			print("Invalid option")
	except:
		print("Failed to display moves")

	getch = input("Press ENTER to return")


# Returns the weaknesses, resistances and immunities of the type/pokemon
def CheckEffect():
	try:
		tmp = sp.call('clear', shell=True)
		print("Select search condition : ")
		print("1. Type")
		print("2. Pokemon name")
		ch = int(input("Enter your choice : "))
		if ch == 1:
			print("Valid types are :\nNormal\t\tFighting\tBug\nDark\t\tDragon\t\tElectric\nFairy\t\tFiret\t\tFlying\nGhost\t\tGrass\t\tGround\nIce\t\tPoison\t\tPsychic\nRock\t\tSteel\t\tWater\n")
			type = input("Enter type (First letter capitalized ex: Fire): ")
			query = "SELECT Immunity FROM IMMUNITIES WHERE Name = '%s'" % (type)
			cur.execute(query)
			rows = cur.fetchall()
			if rows:
				printlist(rows)
				print()
			query = "SELECT Weakness FROM WEAKNESSES WHERE Name = '%s'" % (type)
			cur.execute(query)
			rows = cur.fetchall()
			if rows:
				printlist(rows)
				print()
			query = "SELECT Resistance FROM RESISTANCES WHERE Name = '%s'" % (type)
			cur.execute(query)
			rows = cur.fetchall()
			if rows:
				printlist(rows)
				print()
		elif ch == 2:
			query = "DROP VIEW IF EXISTS IM, WE, RE"
			cur.execute(query)
			pokemon = input("Enter the name of the pokemon : ")
			query = "CREATE VIEW IM AS SELECT I.Immunity AS Immunity FROM IMMUNITIES AS I, POKENAME AS N, POKETYPE AS T WHERE N.PokedexID = T.PokedexID AND (T.Type1 = I.Name OR T.Type2 = I.Name) AND N.Name = '%s'" % (pokemon)
			cur.execute(query)
			query = "CREATE VIEW RE AS SELECT R.Resistance AS Resistance FROM RESISTANCES AS R, POKENAME AS N, POKETYPE AS T WHERE N.PokedexID = T.PokedexID AND (T.Type1 = R.Name OR T.Type2 = R.Name) AND N.Name = '%s'" % (pokemon)
			cur.execute(query)
			query = "CREATE VIEW WE AS SELECT W.Weakness AS Weakness FROM WEAKNESSES AS W, POKENAME AS N, POKETYPE AS T WHERE N.PokedexID = T.PokedexID AND (T.Type1 = W.Name OR T.Type2 = W.Name) AND N.Name = '%s'" % (pokemon)
			cur.execute(query)
			query = "SELECT * FROM IM"
			cur.execute(query)
			rows = cur.fetchall()
			if rows:
				printlist(rows)			
			query = "SELECT * FROM RE WHERE Resistance NOT IN (SELECT * FROM IM UNION SELECT * FROM WE) GROUP BY Resistance"
			cur.execute(query)
			rows = cur.fetchall()
			if rows:
				printlist(rows)
			query = "SELECT * FROM WE WHERE Weakness NOT IN (SELECT * FROM IM UNION SELECT * FROM RE) GROUP BY Weakness"
			cur.execute(query)
			if rows:
				rows = cur.fetchall()
			printlist(rows)
		else:
			print("Invalid option")
	except:
		print("Failed to check effect")
	getch = input("Press ENTER to return")


def DispChampion():
	try:
		query = "SELECT  P.Name, P.PokedexID, C.Move1, C.Move2, C.Move3, C.Move4 FROM CHAMPION AS C, POKENAME AS P WHERE C.PokedexID = P.PokedexID"
		cur.execute(query)
		rows = cur.fetchall()
		if rows:
			printlist(rows)

	except:
		print("Failed to retrieve champion builds")
	getch = input("Press ENTER to return")


def AddChampion():
	try:
		PokedexID = int(input("Enter the PokedexID of the Pokemon : "))
		Move1 = input("Enter the first move  : ")
		Move2 = input("Enter the second move : ")
		Move3 = input("Enter the third move  : ")
		Move4 = input("Enter the fourth move : ")
		query = "INSERT INTO CHAMPION(PokedexID, Move1, Move2, Move3, Move4) VALUES (%d, '%s', '%s', '%s', '%s')" % (PokedexID, Move1, Move2, Move3, Move4)
		cur.execute(query)
		con.commit()
		print("Insertion successful")
	except:
		print("Insertion failed")

	getch = input("Press ENTER to return")


def EditChampion():
	try:
		PokedexID = int(input("Enter the PokedexID of the Pokemon : "))
		query = "SELECT * FROM CHAMPION WHERE PokedexID = %d" % (PokedexID)
		cur.execute(query)
		rows = cur.fetchall()
		if len(rows):
			print("Current data: ")
			print("PokedexID	Move1	Move2	Move3	Move4")
			for row in rows:
				print(row['PokedexID'], row['Move1'], row['Move2'], row['Move3'], row['Move4'])
			print("Enter new data:")
			move1 = input("Enter move1 : ")
			move2 = input("Enter move2 : ")
			move3 = input("Enter move3 : ")
			move4 = input("Enter move4 : ")
			query = "UPDATE CHAMPION SET Move1 = '%s', Move2 = '%s', Move3 = '%s', Move4 = '%s' WHERE PokedexID = %s" % (move1, move2, move3, move4, PokedexID)
			cur.execute(query)
			print("Successfully edited")
			con.commit()
		else:
			print("No champion build exists for this PokedexID")

	except: 
		print("Failed to edit champion build")
	getch = input("Press ENTER to return")


def RemoveChampion():
	try:
		PokedexID = int(input("Enter the PokedexID of the Pokemon : "))
		query = "DELETE FROM CHAMPION WHERE PokedexID = %d" % (PokedexID)
		cur.execute(query)
		print("Successfully deleted")
		con.commit()

	except:
		print("Failed to delete champion build")
	getch = input("Press ENTER to return")


def DispLegendary():
	try:
		tmp = sp.call('clear', shell=True)
		print("Select search condition : ")
		print("1. Name")
		print("2. PokedexID")
		print("3. Display All")
		ch = int(input("Enter your choice : "))
		if ch == 1:
			name = input("Enter name of pokemon : ")
			query = "SELECT P.PokedexID, N.Name, L.Lore FROM POKEMON AS P, POKENAME AS N, LEGENDARY AS L WHERE P.PokedexID = N.PokedexID AND P.PokedexID = L.PokedexID AND N.Name = '%s'" % (name)
			cur.execute(query)
			rows = cur.fetchall()
			if rows:
				for row in rows:
					t = PrettyTable([row['PokedexID'],row['Name']])
					print(t)
					print(row['Lore'],"\n\n")
			else:
				print("Selected legendary doesn't exist.")

		elif ch == 2:
			PokedexID = int(input("Enter PokedexID of pokemon : "))
			query = "SELECT P.PokedexID, N.Name, L.Lore FROM POKEMON AS P, POKENAME AS N, LEGENDARY AS L WHERE P.PokedexID = N.PokedexID AND P.PokedexID = L.PokedexID AND P.PokedexID = '%d'" % (PokedexID)
			cur.execute(query)
			rows = cur.fetchall()
			if rows:
				for row in rows:
					t = PrettyTable([row['PokedexID'],row['Name']])
					print(t)
					print(row['Lore'],"\n\n")
			else:
				print("Selected legendary doesn't exist.")

		elif ch == 3:
			query = "SELECT P.PokedexID, P.Name, L.Lore FROM POKENAME AS P, LEGENDARY AS L WHERE P.PokedexID = L.PokedexID"
			cur.execute(query)
			rows = cur.fetchall()
			if rows:
				for row in rows:
					t = PrettyTable([row['PokedexID'],row['Name']])
					print(t)
					print(row['Lore'],"\n\n")

		else:
			print("Invalid option")				
	except:
		print("Failed to display pokemon")
	getch = input("Press ENTER to return")

# Print Function

def printlist(rows):
	try:
		if not rows:
			print("\nRecord doesn't exist.\n")
			return
		print()
		temp = []
		headlist = []
		for head in rows[0]:
			headlist.append(head)
		t = PrettyTable(headlist)
		for row in rows:
			for value in row:
				temp.append(row[value])
			t.add_row(temp)
			temp.clear()
		print(t)
	except:
		print("Error displaying result")


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
					print("Invalid option")
					tmp = input("Enter any key to CONTINUE>")
				
	except:
		tmp = sp.call('clear', shell=True)
		print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
		tmp = input("Enter any key to CONTINUE>")