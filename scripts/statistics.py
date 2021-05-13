#!/usr/bin/env python

import pandas as pd

df = pd.read_csv("covid_cases_2021-05-11.csv")
print(df.columns)

counts_all_sex = df["Sex"].count()
counts_value_sex = df["Sex"].value_counts()

per_female = round((1347/counts_value_sex)*100, 2)
per_male = round((1296/counts_value_sex)*100, 2)

counts_value_status = df["Case Status"].value_counts()

counts_value_travel = df["Overseas travel"].value_counts()

confirmed_Probable = 2287 + 356
per_travel = round((1466/confirmed_Probable)*100, 2)
per_no_travel = round(((1171+6)/confirmed_Probable)*100, 2)
