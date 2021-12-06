import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df2 = pd.read_csv("CharlieKing_CSData - PlayerInfo.csv")
df1 = pd.read_csv("CharlieKing_CSData - PlayersStats.csv")

pd.set_option("display.max_columns", None)

df2["PLAYER"] = df2["PLAYER"].replace('\n', ' ', regex=True)

#merge by mutual player name
df3 = pd.merge(df2, df1, how="inner", left_on="PLAYER", right_on="PLAYER")

# print(df2["PLAYER"])
# print(df1["PLAYER"])
# print(df3.to_string())

# only include players from the 6 schools with the most NBA players
duke = df3[df3["COLLEGE"] == "Duke"]
kentucky = df3[df3["COLLEGE"] == "Kentucky"]
texas = df3[df3["COLLEGE"] == "Texas"]
nova = df3[df3["COLLEGE"] == "Villanova"]
ucla = df3[df3["COLLEGE"] == "UCLA"]
df = pd.merge(duke, kentucky, how='outer')
df = pd.merge(df, texas, how='outer')
df = pd.merge(df, nova, how='outer')
df = pd.merge(df, ucla, how='outer')

# create new column with 1 as the value for each row so that when I group by school I can have the number of players
player = 1
df3['Players'] = player
# print(df)

# group players by college
df5 = df.groupby("COLLEGE").sum()

# pie chart of games played
df5.plot.pie(y="GP")
plt.title("Top College's Sums of Player's Games Played in the NBA 2021 Season Relative to Each Other")

# bar graph of games played
# print(df5)
ax = df5.plot.bar(y='GP', rot=0, color='lightcoral')
plt.title("Top College's Sums of Players' Games Played in the NBA 2021 Season")

# pie chart of points
df5.plot.pie(y="PTS")
plt.title("Top College's Sums of Player's Points Per Game in the NBA 2021 Season Relative to Each Other")

# bar graph of points
# print(df5)
ax = df5.plot.bar(y='PTS', rot=0, color='darkviolet')
plt.title("Top College's Sums of Players' Points Per Game in the NBA 2021 Season")
plt.show()

# Isolate 8 colleges with the most players
df15 = df3.groupby("COLLEGE").sum()
df15 = df15['Players'].nlargest(12)

# graph colleges with the most players
ax = df15.plot.bar(y='Players', rot=0, color='mediumslateblue')
plt.title("College's Number of NBA PLayers")
plt.show()