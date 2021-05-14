#!/usr/bin/env python

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("covid_cases_2021-05-11.csv")
df['Report Date'] = df['Report Date'].apply(lambda x: x[2:7])
df_reverse = df.iloc[::-1]

def report_day(df):
    # Number of confirmed cases vs reported day
    sns.set(font_scale=1.2)
    df_reverse = df.iloc[::-1]
    sns.set_style("whitegrid")
    ax = sns.displot(df_reverse, x="Report Date", height=7, aspect=13/7, color="mediumseagreen", edgecolor="darkgreen")
    ax.set(xlabel="Report Date", ylabel="Number of cases")
    plt.title("Number of confirmed cases vs reported month", y=0.85, x=0.6, fontsize=18)
    return plt.savefig("cases_month"), plt.close()

def age_group(df):
    # Number of confirmed cases vs age
    sns.set(font_scale=1.1)
    sns.set_style("whitegrid")
    ax = sns.displot(df, x="Age group", height=6, aspect=10/6, color="cornflowerblue", edgecolor="darkblue")
    ax.set(xlabel="Age group", ylabel="Number of cases")
    plt.title("Number of confirmed cases vs age group", y=0.85, x=0.65, fontsize=17)
    return plt.savefig("cases_age"), plt.close()

report_day(df)
age_group(df)


