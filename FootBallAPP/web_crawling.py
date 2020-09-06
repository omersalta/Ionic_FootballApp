from lxml import html
import requests
import pymysql.cursors
import sqlite3
import mysql.connector
from datetime import datetime
from mysql.connector import Error
from mysql.connector import errorcode
import requests

class Team():
    """Team Class"""
    def __init__(self,name, played_games, wins, draws, losses, goals_scored, goals_shipped):
        self.name = name
        self.played_games = played_games
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.goals_scored = goals_scored
        self.goals_shipped = goals_shipped

class Match():
    """Match Class"""
    def __init__(self,home_team, away_team, half_score_0, half_score_1, score_0, score_1):
        self.home_team = home_team
        self.away_team = away_team
        self.half_score_0 = half_score_0
        self.half_score_1 = half_score_1
        self.score_0 = score_0
        self.score_1 = score_1

        
        
#page = requests.get('https://www.sporx.com/ingiltere-premier-lig-
# puan-durumu')
page = requests.get('https://www.sporx.com/italya-serie-a-takimlar')
tree = html.fromstring(page.content)
tr_items = tree.xpath('//tr')

#[len(T) for T in tr_items[:12]]

#Create empty list
stats = []
teams = []
link_names = []
link = ""
say = 0
name = ""
played_games = ""
wins = ""
draws = ""
losses = ""
goals_scored = ""
goals_shipped = ""
goals = ""
points = ""

isTakingAway = 0



#For each row, store each first element (header) and an empty list

for l in tr_items:
	name = l[2].text_content()
	if name.endswith(' '): name = name.replace(' ', '')

	link_name = l[2].text_content().lower().replace('.', '').replace(' ', '-')
	if link_name.endswith('-') : link_name = link_name.replace('-', '')
	
	if name != "Takım":
		t = Team(name, played_games, wins, draws, losses, goals_scored, goals_shipped)
		teams.append(t)
		link_names.append(link_name)
		print(link_name)


index = 0
for t in teams:

	try:
		connection = mysql.connector.connect(host='localhost',
								database='footballApp',
								user='root',
								password='')
		cursor = connection.cursor(prepared=True)
		cursor.execute("DROP TABLE `footballApp`.`{table_name}`".format(table_name=t.name))

		connection.commit()
		print ("Table dropped successfully into {table_name} table".format(table_name=t.name))

	except mysql.connector.Error as error :
		connection.rollback()
		print("Failed to drop MySQL table {}".format(error))
	finally:
		#closing database connection.
		if(connection.is_connected()):
			cursor.close()
			connection.close()
			# print("MySQL connection is closed")	

	try:
		connection = mysql.connector.connect(host='localhost',
								database='footballApp',
								user='root',
								password='')
		cursor = connection.cursor(prepared=True)
		
		#print("CREATE TABLE `footballApp`.`{table_name}` (`home_team` TEXT NOT NULL, `away_team` TEXT NOT NULL, `half_score_0` INT NOT NULL, half_score_1 INT NOT NULL, score_0 INT NOT NULL, score_1 INT NOT NULL) ENGINE = InnoDB".format(table_name=t.name))
		cursor.execute("CREATE TABLE `footballApp`.`{table_name}` (`home_team` TEXT NOT NULL, `away_team` TEXT NOT NULL, `half_score_0` INT NOT NULL, half_score_1 INT NOT NULL, score_0 INT NOT NULL, score_1 INT NOT NULL) ENGINE = InnoDB".format(table_name=t.name))

		connection.commit()
		# print ("Record inserted successfully into python_users table")

	except mysql.connector.Error as error :
		connection.rollback()
		print("Failed to insert into MySQL table {}".format(error))
	finally:
		#closing database connection.
		if(connection.is_connected()):
			cursor.close()
			connection.close()
			# print("MySQL connection is closed")	
	
	print(link_names[index])
	link = "https://www.sporx.com/"+link_names[index]+"-fiksturu-ve-mac-sonuclari"
	index = index + 1
	print (link)
	page = requests.get( link )
	tree = html.fromstring( page.content )
	tr_items = tree.xpath('//tr')
	for l in tr_items :
		if l[3].text_content() != "Ev Sahibi" and l[6].text_content() != "-":
			home_team = l[3].text_content()
			away_team = l[5].text_content()

			half_score = l[6].text_content().split("-")
			final_score = l[4].text_content().split("-")

			half_score_0 = int(half_score[0])
			half_score_1 = int(half_score[1])
			score_0 = int(final_score[0])
			score_1 = int(final_score[1])

			# print(home_team,away_team,half_score_0,half_score_1,half_score_0,score_0,score_1)

			m = Match(home_team, away_team, half_score_0, half_score_1, score_0, score_1)

			try:
				connection = mysql.connector.connect(host='localhost',
										database='footballApp',
										user='root',
										password='')
				cursor = connection.cursor(prepared=True)

				#print("INSERT INTO `{table_name}` (`home_team`, `away_team`, `half_score_0`, `half_score_1`, `score_0`, `score_1`) VALUES ({h},{a},{h0},{h1},{s0},{s1})".format(table_name=t.name, h=m.home_team, a=m.away_team, h0=m.half_score_0, h1=m.half_score_1, s0=m.score_0, s1=m.score_1))
				cursor.execute("INSERT INTO `{table_name}` (`home_team`, `away_team`, `half_score_0`, `half_score_1`, `score_0`, `score_1`) VALUES ('{h}','{a}',{h0},{h1},{s0},{s1})".format(table_name=t.name, h=m.home_team, a=m.away_team, h0=m.half_score_0, h1=m.half_score_1, s0=m.score_0, s1=m.score_1))

				connection.commit()
				# print ("Record inserted successfully into python_users table")

			except mysql.connector.Error as error :
				connection.rollback()
				print("Failed to insert into MySQL table {}".format(error))
			finally:
				#closing database connection.
				if(connection.is_connected()):
					cursor.close()
					connection.close()
					# print("MySQL connection is closed")

	# Her takim için php script yazdır













