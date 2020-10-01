import pandas as pd
import random

def textFile():
    f = open('evolution.txt', 'r+')
    lines = f.readlines()
    Line = []
    for line in lines:
        Line.append(line)
    return Line

def getDict(df):
    ids = df.ID.to_list()
    name = df.Name.to_list()
    remove_pokemon = {}
    for i in range(0, len(name)):
        if ids[i] not in remove_pokemon:
            remove_pokemon[ids[i]] = name[i]
    pokemon = dict(map(reversed, remove_pokemon.items())) 
    return pokemon

def getPokemonFamily(line):
    evolutionFam = []
    for i in range(1, len(line), 2):
        l = line[i]
        evolutionFam.append(l)
    df = pd.read_csv('pokemon.csv')
    pokemon = getDict(df)
    c = 0
    evolve = {}
    for i in evolutionFam:
        fam = []
        sent = i.split()
        for word in sent:
            fam.append(word)
        if fam[0] not in pokemon:
            ev = pokemon[fam[1]]
        else:
            ev = pokemon[fam[0]]
        for pok in fam:
            try:
                pokemon[pok]
                if pok not in evolve:
                    evolve[pok] = ev
                    ev = pokemon[pok]
            except:
                pass
    return evolve, pokemon

def writeStuff(evolve, pokemon):
    gen = [1, 2, 3, 4, 5, 6, 7, 8]
    tier = ['OU', 'UU', 'AU']
    final = []
    for pok in pokemon:
        if pok not in evolve:
            final.append([pokemon[pok], random.choice(gen), random.choice(tier), pokemon[pok]])
        else:
            final.append([pokemon[pok], random.choice(gen), random.choice(tier), evolve[pok]])
    
    df = pd.DataFrame(final)
    df.to_csv('POKEMON.csv', index=False, header=False)

lines = textFile()
evolve, pokemon = getPokemonFamily(lines)
writeStuff(evolve, pokemon)