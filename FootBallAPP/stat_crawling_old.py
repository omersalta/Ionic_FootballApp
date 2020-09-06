from lxml import html
import requests
import pymysql.cursors
import sqlite3
import mysql.connector
from datetime import datetime
from mysql.connector import Error
from mysql.connector import errorcode




class Team():
    """Team Class"""
    def __init__(self,name, played_games, wins, draws, losses, goals_scored, goals_shipped, goals, points):
        self.name = name
        self.played_games = played_games
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.goals_scored = goals_scored
        self.goals_shipped = goals_shipped
        self.goals = goals
        self.points = points


#page = requests.get('https://www.sporx.com/italya-serie-a-puan-durumu')
page = requests.get('https://www.sporx.com/ingiltere-premier-lig-puan-durumu')

tree = html.fromstring(page.content)


teams = tree.xpath('//tr')

#[len(T) for T in teams[:12]]

#Create empty list
team_list=[]
team2_list=[]


name = ""
played_games = ""
wins = ""
draws = ""
losses = ""
goals_scored = ""
goals_shipped = ""
goals = ""
points = ""
i = 0 
#For each row, store each first element (header) and an empty list
for l in teams:
    if len(l) == 10:
            
        name = l[1].text_content()
        played_games = l[2].text_content()
        wins = l[3].text_content()
        draws = l[4].text_content()
        losses = l[5].text_content()
        goals_scored = l[6].text_content()
        goals_shipped = l[7].text_content()
        goals = l[8].text_content()
        points = l[9].text_content()
        #name=t.text_content()
        #print '%d:"%s"'%(i,name)
        #team_array.append((name,[]))
        #print (name, played_games, wins, draws, losses, goals_scored, goals_shipped, goals, points)

        if name != "Takım" and i == 1 :
        
            t = Team(name, played_games, wins, draws, losses, goals_scored, goals_shipped, goals, points)
            team_list.append(t)
            
        if name != "Takım" and i == 2 :
            t = Team(name, played_games, wins, draws, losses, goals_scored, goals_shipped, goals, points)
            team2_list.append(t)

        if name == "Takım" :
                i=i+1
        


for t in team_list:
    print(t.name, t.played_games, t.wins, t.draws, t.losses, 
            t.goals_scored, t.goals_shipped, t.goals, t.points)

print("------------------------")
for t in team2_list:
    print(t.name, t.played_games, t.wins, t.draws, t.losses, 
            t.goals_scored, t.goals_shipped, t.goals, t.points)





try:
    db_conn = mysql.connector.connect(host='localhost',
                                   database='footballApp',
                                   user='root',
                                   password='')
    cursor = db_conn.cursor()
    Delete_all_query = """truncate table away_stats """
    cursor.execute(Delete_all_query)
    Delete_all_query = """truncate table home_stats """
    cursor.execute(Delete_all_query)
    db_conn.commit()
    print("All Record Deleted successfully ")
except mysql.connector.Error as error:
    print("Failed to Delete all records from database table: {}".format(error))
finally:
    # closing database connection.
    if (db_conn.is_connected()):
        cursor.close()
        db_conn.close()
        print("MySQL connection is closed")           





i=0
try:
        connection = mysql.connector.connect(host='localhost',
                             database='footballapp',
                             user='root',
                             password='')
        cursor = connection.cursor(prepared=True)
        for t in team_list:
                i=i+1
                sql_insert_query = """ INSERT INTO `home_stats`
                                (`id`, `name`, `played_games`, `wins`, `draws`, `losses`, `goals_scored`, `goals_shipped`, `goals`, `points`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                insert_tuple = (i, t.name, t.played_games, t.wins, t.draws, t.losses, t.goals_scored, t.goals_shipped, t.goals, points)
                result  = cursor.execute(sql_insert_query, insert_tuple)
                connection.commit()
                print ("Record inserted successfully into home_stats table")
except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to insert into MySQL table {}".format(error))
finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
i=0

try:
        connection = mysql.connector.connect(host='localhost',
                             database='footballapp',
                             user='root',
                             password='')
        cursor = connection.cursor(prepared=True)
        for t in team2_list:
                i=i+1
                sql_insert_query = """ INSERT INTO `away_stats`
                                (`id`, `name`, `played_games`, `wins`, `draws`, `losses`, `goals_scored`, `goals_shipped`, `goals`, `points`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                insert_tuple = (i, t.name, t.played_games, t.wins, t.draws, t.losses, t.goals_scored, t.goals_shipped, t.goals, points)
                result  = cursor.execute(sql_insert_query, insert_tuple)
                connection.commit()
                print ("Record inserted successfully into home_stats table")
except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to insert into MySQL table {}".format(error))
finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

