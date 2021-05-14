#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
import numpy as np
import seaborn as sns

df = pd.read_csv("alert_cases.csv")
df["Date"] = df["Date"].apply(lambda x: x[2:7])
cases = np.array(list(df["New_cases"]))
alert = np.array(list(df["Alert_level"]))

casses_array = [[i] for i in cases]
alert_array = [[i] for i in alert]


def linear_regression(x, y):
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
    return plt.savefig("regression.png"), print('Coefficients: \n', regr.coef_)

linear_regression(alert_array, casses_array)
