import sqlite3 as db



def getAllPlayersData() :
    con = db.connect('/home/omar/Downloads/database.sqlite')
    cursor = con.cursor()
    return cursor.execute("select player_name,height,weight from Player").fetchall()
