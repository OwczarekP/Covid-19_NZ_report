#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("flevy.com-coronavirus-new-zealand.csv")
df["Date"] = df["Date"].apply(lambda x: x[2:7])
df_total = df[["Date", "Total Deaths", "Total Cases", "Total Recoveries", "Active Cases"]]
df_new = df[["Date", "New Cases", "New Deaths", "New Recoveries", "Total Deaths", "Active Cases"]]
df_total.dropna()
df_new.dropna()
df_total = df_total.iloc[::-1]
df_new = df_new.iloc[::-1]

def death(df):
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(2, 1, figsize=(10, 6.5), sharex='col', sharey='row')
    ax[0].set_title("Number of deaths each month")
    ax[0].set(ylabel="Number of cases")
    sns.lineplot(ax=ax[0], data=df, x="Date", y="New Deaths", color="red")
    ax[1].set_title("Number of all deaths so far")
    ax[1].set(xlabel="Date", ylabel="Number of cases")
    sns.lineplot(ax=ax[1], data=df, x="Date", y="Total Deaths", color="red")
    return plt.savefig("number_of_deaths.png"), plt.close
death(df_new)

def total(df):
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(2, 1, figsize=(10, 6.5), sharex='col', sharey='row')
    ax[0].set_title("Comparing number of cases, recovered and deaths ")
    ax[0].set(ylabel="Number of cases")
    sns.lineplot(ax=ax[0], data=df, x="Date", y="New Cases", color="orange")
    sns.lineplot(ax=ax[0], data=df, x="Date", y="New Deaths", color="red")
    sns.lineplot(ax=ax[0], data=df, x="Date", y="New Recoveries")
    plt.legend(["New Cases", "New Deaths", "New Recoveries"], bbox_to_anchor=(1, 1), prop={'size': 12})
    ax[1].set_title("Adding active cases to graph above")
    ax[1].set(ylabel="Number of cases")
    sns.lineplot(ax=ax[1], data=df, x="Date", y="Active Cases", color="green")
    sns.lineplot(ax=ax[1], data=df, x="Date", y="New Cases", color="orange")
    sns.lineplot(ax=ax[1], data=df, x="Date", y="New Deaths", color="red")
    sns.lineplot(ax=ax[1], data=df, x="Date", y="New Recoveries")
    plt.xticks(rotation=20)
    plt.legend(["Active Cases", "New Cases", "New Deaths", "New Recoveries"], bbox_to_anchor=(1, 2.2), prop={'size': 11})
    return plt.savefig("new_cases.png"), plt.close()
total(df_new)

def total_cases(df):
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(11, 8))
    sns.lineplot(data=df, x="Date", y="Active Cases", color="green")
    sns.lineplot(data=df, x="Date", y="Total Cases", color="orange")
    sns.lineplot(data=df, x="Date", y="Total Recoveries")
    sns.lineplot(data=df, x="Date", y="Total Deaths", color="red")
    ax.set(ylabel="Number of cases")
    plt.legend(["Active Cases", "Total Cases", "Total Recoveries", "Total Deaths"], bbox_to_anchor=(0.25, 1),
               prop={'size': 12})
    return plt.savefig("total_cases.png"), plt.close()
total_cases(df_total)

