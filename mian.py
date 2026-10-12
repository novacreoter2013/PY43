import pandas as pd

print(' --- PART 1: PANDAS SERIES --- ')
scores = [98500 , 87200 , 76400 , 65100 , 54800]
players = pd.Series(scores , index = ['NIGHTMARE' , 'SHADOW' , 'BLAZE' , 'FROST' , 'EMBER'])
print(players)

print()
print(' --- PART 2: PANDAS DATAFRAME --- ')
data = {
    'Player' : ['NIGHTMARE' , 'SHADOW' , 'BLAZE' , 'FROST' , 'EMBER'],
    'Level' : [42,39,1000,23,67],
    'Score' : [98500 , 872000, 76400 , 65100 , 54800],
    'Wins' : [210,212,234,590,679]
}
df = pd.DataFrame(data)
print(df)

print(
    print(' --- PART 3 : ACCESSING ROES ---')
)
print('Row.0(top player) :')
print(df.loc[0])
print()
print('Rows 2 and 3 :')
print(df.loc[[2,3]])


print()
print(' --- PART 4 : READING CSV FILES --- ')
full_df = pd.read_csv('leaderboard.csv')
print('FIRST 5 ROWS (head) :')
print(full_df.head())
print()
print('LAST 3 rows (tail) :')
print(full_df.tail(3))
print()
print('DATASET INFO :')
print(full_df.info())


print()
print(' --- PART 5 : CLEANING DATA --- ')
print('Rows With Missing Values :')
print('Rows with missing values removed (dropna):')
cleaned_df = full_df.dropna()
print(cleaned_df.to_string())
print()
print('Missing Values Filled with 0 (fillna):')
filled_df = full_df.fillna(0)
print(filled_df.to_string())