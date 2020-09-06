from lxml import html
import requests
import pymysql.cursors
import sqlite3
import mysql.connector
from datetime import datetime
from mysql.connector import Error
from mysql.connector import errorcode



page = requests.get('https://www.sporx.com/ingiltere-premier-lig-fikstur')
#page = requests.get('https://www.sporx.com/italya-serie-a-fikstur')

tree = html.fromstring(page.content)


teams = tree.xpath('//tr')

home_teams=[]
away_teams=[]

number_of_matches = 0
for l in teams:
    if number_of_matches == 11:
        break
    if number_of_matches == 0:
        number_of_matches = number_of_matches + 1
        continue

    home_team = l[1].text_content()
    away_team = l[3].text_content()

    home_team.lower().replace('.', '').replace(' ', '-')
    away_team.lower().replace('.', '').replace(' ', '-')
    print(home_team, away_team)

    home_teams.append(home_team)
    away_teams.append(away_team)

    number_of_matches = number_of_matches + 1


try:
    db_conn = mysql.connector.connect(host='localhost',
                                   database='footballApp',
                                   user='root',
                                   password='')
    cursor = db_conn.cursor()
    Delete_all_query = """truncate table last_week """
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


try:
    connection = mysql.connector.connect(host='localhost',
                            database='footballApp',
                            user='root',
                            password='')
    cursor = connection.cursor(prepared=True)

    for i in range(0,len(home_teams)):
        sql_insert_query = """ INSERT INTO `last_week`
                            (`id`, `home_team`, `away_team`) VALUES (%s,%s,%s)"""
        insert_tuple = (i+1, home_teams[i], away_teams[i])
        result  = cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()
        # print ("Record inserted successfully into last_week table")

except mysql.connector.Error as error :
    connection.rollback()
    print("Failed to insert into MySQL table {}".format(error))
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")