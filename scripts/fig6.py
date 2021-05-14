#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def load_csv(path):
    """load_csv
    This function load the file from the path and save it as dataframe

    :param path: string to the csv file
    :return: df: the dataframe from the csv
    """
    df = pd.read_csv(path)
    return df


def clean_csv(df):
    """clean_csv
    This function filter the data to shows selected data
    Then it clean the data from empty and NaN rows

    :param df:  the dataframe from the csv file
    :return: df_new: the dataframe with selected columns
    """
    df["Date"] = df["Date"].apply(lambda x: x[2:7])
    df_total = df[["Date", "Total Deaths", "Total Cases", "Total Recoveries", "Active Cases"]]
    df_new = df[["Date", "New Cases", "New Deaths", "New Recoveries", "Total Deaths", "Active Cases"]]
    df_total.dropna()
    df_new.dropna()
    df_total = df_total.iloc[::-1]
    df_new = df_new.iloc[::-1]
    return df_total


def create_plot(df):
    """create_plot
    This function create the line plot showing the number selected data
    Then its save this plot as png file

    :param df: the dataframe with the deaths data
    :return: None
    """
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(11, 8))
    sns.lineplot(data=df, x="Date", y="Active Cases", color="green")
    sns.lineplot(data=df, x="Date", y="Total Cases", color="orange")
    sns.lineplot(data=df, x="Date", y="Total Recoveries")
    sns.lineplot(data=df, x="Date", y="Total Deaths", color="red")
    ax.set(ylabel="Number of cases")
    plt.legend(["Active Cases", "Total Cases", "Total Recoveries", "Total Deaths"], bbox_to_anchor=(0.25, 1),
               prop={'size': 12})
    return plt.savefig("../images/fig6.png"), plt.close()


def main():
    df = load_csv("../data/flevy.com-coronavirus-new-zealand.csv")
    df = clean_csv(df)
    create_plot(df)


if __name__=='__main__':
    main()

