import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("owid-covid-data.csv")
del df["iso_code"], df["continent"]

df['date'] = df['date'].apply(lambda x: x[2:7])
df_NZL = df[df["location"] == "New Zealand"]
total_cases_deaths_date = df_NZL[["date", "new_deaths", "total_deaths"]]
final_df = total_cases_deaths_date.dropna()

def total_death(data):
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(11, 8))
    sns.lineplot(data=data, x="date", y="total_deaths", color="red")
    ax.set(xlabel="Report Date", ylabel="Number of cases [x100]")
    plt.title("Number of all deaths so far", y=0.6, fontsize=16)
    return plt.savefig("Number_of_all_deaths_so_far.png"), plt.close()

def new_death(data):
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(11, 8))
    sns.lineplot(data=data, x="date", y="new_deaths")
    ax.set(xlabel="Report Date", ylabel="Number of cases [x100]")
    plt.title("Number of deaths each month", y=0.85, fontsize=16)
    return plt.savefig("Number_of_deaths_each_month.png"), plt.close()

new_death(final_df)
total_death(final_df)

all_deaths = final_df["total_deaths"].count()