import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("CharlieKing_CSData - PlayerInfo.csv")
df1 = pd.read_csv("CharlieKing_CSData - PlayersStats.csv")

df["PLAYER"] = df["PLAYER"].replace('\n', ' ', regex=True)

df3 = pd.merge(df, df1, how="inner", left_on="PLAYER", right_on="PLAYER")

# print(df["PLAYER"])
# print(df1["PLAYER"])
print(df3.to_string())