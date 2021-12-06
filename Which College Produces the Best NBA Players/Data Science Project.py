import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df2 = pd.read_csv("CharlieKing_CSData - PlayerInfo.csv")
df1 = pd.read_csv("CharlieKing_CSData - PlayersStats.csv")

pd.set_option("display.max_columns", None)

# get rid of return
df2["PLAYER"] = df2["PLAYER"].replace('\n', ' ', regex=True)

# merge by mutual player name
data = pd.merge(df2, df1, how="inner", left_on="PLAYER", right_on="PLAYER")

# only include players from the 5 schools with the most NBA players
duke = data[data["COLLEGE"] == "Duke"]
kentucky = data[data["COLLEGE"] == "Kentucky"]
texas = data[data["COLLEGE"] == "Texas"]
nova = data[data["COLLEGE"] == "Villanova"]
ucla = data[data["COLLEGE"] == "UCLA"]
df = pd.merge(duke, kentucky, how='outer')
df = pd.merge(df, texas, how='outer')
df = pd.merge(df, nova, how='outer')
df = pd.merge(df, ucla, how='outer')

# create new column with 1 as the value for each row so that when I group by school I can have the number of players
player = 1
data['Players'] = player
# print(df)

# group players by college
colleges = df.groupby("COLLEGE").sum()

# pie chart of games played
colleges.plot.pie(y="GP")
plt.title("Top College's Sums of Player's Games Played in the NBA 2021 Season Relative to Each Other")

# bar graph of games played
ax = colleges.plot.bar(y='GP', rot=0, color='lightcoral')
plt.title("Top College's Sums of Players' Games Played in the NBA 2021 Season")

# pie chart of points
colleges.plot.pie(y="PTS")
plt.title("Top College's Sums of Player's Points Per Game in the NBA 2021 Season Relative to Each Other")

# bar graph of points
# print(df5)
ax = colleges.plot.bar(y='PTS', rot=0, color='darkviolet')
plt.title("Top College's Sums of Players' Points Per Game in the NBA 2021 Season")
plt.show()

# Isolate 8 colleges with the most players
topSchools = data.groupby("COLLEGE").sum()
topSchools = topSchools['Players'].nlargest(12)

# graph colleges with the most players
ax = topSchools.plot.bar(y='Players', rot=0, color='mediumslateblue')
plt.title("College's Number of NBA Players")
plt.show()