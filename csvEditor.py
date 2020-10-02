import pandas as pd
import random

df = pd.read_csv('MOVES.csv')
df_reorder = df[['Name', 'Description', 'Accuracy', 'Category', 'PP', 'Power', 'Type']] # rearrange column here
df_reorder.to_csv('MOVES.csv', index=False)