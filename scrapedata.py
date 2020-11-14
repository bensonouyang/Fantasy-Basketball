from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# NBA season we will be analyzing
year = 2020

# URL page we will scraping
url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)

# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html, features="lxml")

# use findALL() to get the column headers
soup.findAll('tr', limit=2)

# use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

# exclude the first column as we will not need the
#ranking order from Basketball Reference for the analysis
headers = headers[1:]
headers

##Header Meaning
#Player = Name of Player
#Pos = Position
#Age = Age
#Tm = Team
#G = Games Played
#GS = Games Started
#MP = Minutes Played Per Game
#FG = Field Goals Per Game
#FGA = Field Goal Attempts Per Game
#FG% = Field Goal Percentage
#3P = 3-Point Field Goals Per Game
#3PA = 3-Point Field Goal Attempts Per Game
#3P% = 3-Point Field Goal Percentage
#2P = 2-Point Field Goals Per Game
#2PA = 2-Point Field Goal Attempts Per Game
#2P% = 2-Point Field Goal Percentage
#eFG% = Effective Field Goal Percentage
#FT = Free Throws Per Game
#FTA = Free Throw Attempts Per Game
#FT% = Free Throw Percentage
#ORB = Offensive Rebounds Per Game
#DRB = Defensive Rebounds Per Game
#TRB = Total Rebounds Per Game
#AST = Assists Per Game
#BLK = Blocks Per Game
#TOV = Turnover Per Game
#PF = Personal Fouls Per Game
#PTS = Points Per Game


# avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]

stats = pd.DataFrame(player_stats, columns = headers)

#print(stats)
stats.to_csv("stats.csv")
