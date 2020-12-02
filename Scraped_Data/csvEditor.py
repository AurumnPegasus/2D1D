import pandas as pd
import random

df = pd.read_csv('MOVES.csv')
name = df.Name.to_list()
moveType = df.Type.to_list()
df = pd.read_csv('POKETYPE.csv')
ID = df.ID.to_list()
poketype1 = df.TYPE1.to_list()
poketyp2 = df.TYPE2.to_list()
allTypes =  [ "Normal", "Fire", "Fighting", "Water", "Flying", "Grass", "Poison", "Electric", "Ground", "Psychic", "Rock", "Ice", "Bug", "Dragon", "Ghost", "Dark", "Steel", "Fairy"]
pokemon = []
for i in allTypes:
    pokemon.append([])

for i in range(0, len(ID)):
    for t in range(0, len(allTypes)):
        if poketype1[i] == allTypes[t] or poketyp2[i] == allTypes[t]:
            pokemon[t].append(ID[i])
        else:
            pass

moves = []
for i in allTypes:
    moves.append([])
for i in range(0, len(name)):
    for t in range(0, len(allTypes)):
        if allTypes[t] == moveType[i]:
            moves[t].append(name[i])
            break

pokemove = []
for t in range(0, len(pokemon)):
    pt = allTypes[t]
    for pok in pokemon[t]:
        allmove = random.sample(moves[t], 4)
        for j in allmove:
            pokemove.append([pok, j])

df = pd.DataFrame(pokemove)
df.to_csv('POKEMOVE.csv', index=False)