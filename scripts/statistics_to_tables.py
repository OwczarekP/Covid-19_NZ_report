#!/usr/bin/env python

# summary statistics to make tables by hand

import pandas as pd


def load_csv(path):
    """load_csv
    This function load the file from the path and save it as dataframe

    :param path: string to the csv file
    :return: df: the dataframe from the csv
    """
    df = pd.read_csv(path)
    return df


def get_data(df):
    """get_data
    This function get the data needed to write table 1 and table 3 in report
    Counts the number of covid-19 cases by gender and overseas travel

    :param df:  the dataframe from the csv file
    :return:
    """
    counts_all_sex = df["Sex"].count()
    counts_value_sex = df["Sex"].value_counts()

    per_female = round((1347/counts_value_sex)*100, 2)
    per_male = round((1296/counts_value_sex)*100, 2)

    counts_value_status = df["Case Status"].value_counts()

    counts_value_travel = df["Overseas travel"].value_counts()

    confirmed_Probable = 2287 + 356
    per_travel = round((1466/confirmed_Probable)*100, 2)
    per_no_travel = round(((1171+6)/confirmed_Probable)*100, 2)

    number_confirmed = df['Case Status'].value_counts()
    
    population_NZL = 4917000
    deaths = 26
    caes_in_population = round((confirmed_Probable/population_NZL)*100, 2)
    deaths_in_population = round((deaths/population_NZL)*100, 2)


def main():
    df = load_csv('../data/covid_cases_2021-05-11.csv')
    get_data(df)


if __name__=='__main__':
    main()
