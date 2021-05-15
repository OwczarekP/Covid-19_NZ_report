#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def load_csv(path):
    """load_csv
    This function load the file from the path and save it as dataframe

    :param path: string to the csv file
    :return: df: dataframe with the data
    """
    df = pd.read_csv(path)
    df["Date"] = df["Date"].apply(lambda x: x[2:7])
    return df


def influence_alerts_cases(df):
    """influence_alert_cases
    This function read the data and return the plot
    showing the alert level on daily new cases

    :param df: the dataframe with the data about new cases and alert level
    :return:
    """
    sns.set_style("whitegrid")
    plt.subplots(figsize=(10, 6))
    plt.title(f"Influence of alerts on new cases", y=1, x=0.5, fontsize=18)
    sns.lineplot(data=df, x="Date", y="New_cases", color='blue')
    plt.ylabel("Number of cases")
    plt.xticks(rotation=15)
    sns.scatterplot(data=df, y="New_cases", x="Alert_level", color="black")
    return plt.savefig("../images/fig11.png")


def main():
    df = load_csv("../data/alert_cases.csv")
    influence_alerts_cases(df)


if __name__=='__main__':
    main()
