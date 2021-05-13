#!/usr/bin/env python

# gener

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("unemployment.csv")

sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(11, 8))
ax = sns.lineplot(data=df, x="date", y="Poland", color="red", linewidth=4)
ax = sns.lineplot(data=df, x="date", y="Norway", color="tab:orange", linewidth=4)
ax = sns.lineplot(data=df, x="date", y="Australia", color="green", linewidth=4)
ax = sns.lineplot(data=df, x="date", y="European Union average", color="m", linewidth=4)
ax = sns.lineplot(data=df, x="date", y="New Zeland", color="blue", linewidth=4)
plt.axvline(3, linewidth=4, color="k")
ax.set(xlabel="date", ylabel="Percentage of unemployment [%]")
plt.title("Percentage of unemployment during the pandemic", y=1, x=0.5, fontsize=18)
plt.xticks(rotation=30)
plt.legend(['POL', 'NOW', 'AUS', 'EU', 'NZL'], bbox_to_anchor=(1, 1), prop={'size': 12})
plt.savefig("unemployment_rate.png")
