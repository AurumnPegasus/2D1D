import pandas as pd
import random

df = pd.read_csv('pokemon.csv')
ids = df.ID.to_list()
typeing = df.Type.to_list()
data = []
for i in range(0, len(ids)):
    data.append([ids[i], typeing[i]])

sorted(data)

data2 = []
for i in range(0, len(ids)):
    if i == 0:
        data2.append(data[i])
        pass
    if data[i][0] == data2[int(len(data2))-1][0]:
        pass
    else:
        data2.append(data[i])

final = []
for i in data2:
    t = i[1]
    t = t.split()
    if len(t) == 1:
        final.append([i[0], t[0], 'NULL'])
    else:
        final.append([i[0], t[0], t[1]])

df = pd.DataFrame(final)
df.to_csv('POKETYPE.csv')
