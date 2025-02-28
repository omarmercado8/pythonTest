import sqlite3 as db
import pandas as pd
import matplotlib.pyplot as plt



con = db.connect('/Users/mmmerca/Downloads/database.sqlite')

df = pd.read_sql("select * from Player",con)
print(df.columns)

print(df.head(5))

jugadores = df.head(5)

print(jugadores)
print(jugadores['height']< 180)

jugadores_chaparros = jugadores[jugadores['height']< 180]

jugadores_altos = jugadores[jugadores['height']>= 180]

print("chaparros  ---------------------------------------------")
print(jugadores_chaparros)

print("altos  ---------------------------------------------")
print(jugadores_altos)

print('group by-------------------------------------------')
print((jugadores.groupby('height').get_group(182.88)))
print(jugadores["weight"])


fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot(jugadores["weight"], jugadores["height"])  # Plot some data on the Axes.
plt.show()


Grafica de altura mas alta por equipo
Grafic de peso mas alto por pais