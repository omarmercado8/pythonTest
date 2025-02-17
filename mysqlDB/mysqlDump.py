import mysql.connector
import sqliteTest


def runn() :

    mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="admin")



    CREATE_DATABASE="CREATE DATABASE football"

    cursor = mydb.cursor()

    mydb.cursor().execute("DROP DATABASE football")

    database = cursor.execute(CREATE_DATABASE)

    mydb.close()

    mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="admin", database="football")


    CREATE_TABLE="CREATE TABLE players (player_id int AUTO_INCREMENT, name varchar(100) NOT NULL, height int(10) NOT NULL, weight int(10) NOT NULL,PRIMARY KEY(player_id))"


    cursor = mydb.cursor()

    cursor.execute(CREATE_TABLE)


    INSERT_DATA="INSERT INTO players (name, height, weight) VALUES ('TEst',1,1)"

    cursor.execute(INSERT_DATA)

    SELECT_DATA="SELECT * FROM players"

    data = cursor.execute(SELECT_DATA)
    id,name, height, weight = cursor.fetchone()
    print(id,name, height, weight)

    mydb.commit()


    playersSqlite = sqliteTest.getAllPlayersData()

    for x in playersSqlite:
        print("--------------------------------------------------------------------------")
        pn,h,w =x
        INSERT_MULTIPLE="""INSERT INTO players (name,height,weight)VALUES(%s,%s,%s)"""
        print(pn,h,w)
        cursor.execute(INSERT_MULTIPLE,(pn,h,w),multi=True)
        mydb.commit()


    cursor.close()
    mydb.close()




def getAllPlayers() :
    runn()
    mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="admin", database="football")
    cursor = mydb.cursor()
    SELECT_ALL="SELECT name,height,weight FROM players"
    cursor.execute(SELECT_ALL)
    data = cursor.fetchall()
    return data