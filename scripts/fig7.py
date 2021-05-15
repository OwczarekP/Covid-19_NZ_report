#!/usr/bin/env python

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def load_csv(path):
    """load_csv
    This function load the file from the path and save it as dataframe

    :param path: string to the csv file
    :return: df: the dataframe from the csv
    """
    df = pd.read_csv(path)
    df['Report Date'] = df['Report Date'].apply(lambda x: x[2:7])
    df_reverse = df.iloc[::-1]
    return df


def create_plot(df):
    """create_plot
    This function create the bar plot, showing total covid-19 cases by age

    :param df: the dataframe to the Naw Zealand data
    :return: bar plot
    """
    # Number of confirmed cases vs age
    sns.set(font_scale=1.1)
    sns.set_style("whitegrid")
    ax = sns.displot(df, x="Age group", height=6, aspect=10/6, color="cornflowerblue", edgecolor="darkblue")
    ax.set(xlabel="Age group", ylabel="Number of cases")
    plt.title("Number of confirmed cases vs age group", y=0.85, x=0.65, fontsize=17)
    return plt.savefig("../images/fig7"), plt.close()


def main():
    df = load_csv("../data/covid_cases_2021-05-11.csv")
    create_plot(df)


if __name__=='__main__':
    main()



