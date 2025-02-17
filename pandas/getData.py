import sqlite3 as db
import pandas as pd


con = db.connect('/home/omar/Downloads/database.sqlite')

df = pd.read_sql("select * from Player",con)
print(df.head().describe())
print(df.head().describe().T)

df2 = df.head().describe().T
print(df.info(show_counts=True))
df2.to_csv("/home/omar/Desktop/data_fut.txt",sep=",", index=False)

print(df.shape)

print(df.columns)

df3=df.copy()

print(df3.describe)
df3.loc[100:104,'player_name']=None

print(df3.info())

print(df3.isnull())