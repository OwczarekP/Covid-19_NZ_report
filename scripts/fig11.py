#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
import numpy as np
import seaborn as sns


def load_csv(path):
    """load_csv
    This function load the file from the path and save it as dataframe
    Then, it convert the cases and alert level to the array format

    :param path: string to the csv file
    :return: alert_array: array with the alert level number
            cases_array: array with new day cases
    """
    df = pd.read_csv(path)
    df["Date"] = df["Date"].apply(lambda x: x[2:7])
    cases = np.array(list(df["New_cases"]))
    alert = np.array(list(df["Alert_level"]))

    cases_array = [[i] for i in cases]
    alert_array = [[i] for i in alert]
    return alert_array, cases_array


def linear_regression(x, y):
    """linear regression
    This function create linear regression between alert level and new cases
    calculating its coefficient
    and create regression plot

    :param x: the array with the alert level
    :param y: the array with the daily new cases
    :return: regression plot, regression coefficient
    """
    regr = linear_model.LinearRegression()
    regr.fit(x, y)
    predictor_y = regr.predict(x)
    # plot output
    sns.set(font_scale=1.1)
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.scatter(x, y, color='black')
    plt.plot(x, predictor_y, color='blue', linewidth=3)
    plt.xlabel("Alert")
    plt.ylabel("Number of daily cases")
    plt.title(f"Influence of new cases on New Zealand COVID-19 alert level", y=1, x=0.5, fontsize=13)
    return plt.savefig("../images/fig11.png"), print('Coefficients: \n', regr.coef_)


def main():
    alert_array, cases_array = load_csv("../data/alert_cases.csv")
    linear_regression(alert_array, cases_array)


if __name__=='__main__':
    main()