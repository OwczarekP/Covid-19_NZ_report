
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
    return df


def create_plot(df):
    """create_plot
    This function select the countries from the data,
    Then create the line plot showing the unemployment rate in selected countries
    Then its save this plot as png file and html file

    :param df: the dataframe with unemployment between countries
    :return: None
    """
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(11, 8))
    ax = sns.lineplot(data=df, x="date", y="Poland", color="red", linewidth=4)
    ax = sns.lineplot(data=df, x="date", y="Norway", color="tab:orange", linewidth=4)
    ax = sns.lineplot(data=df, x="date", y="Australia", color="green", linewidth=4)
    ax = sns.lineplot(data=df, x="date", y="European Union average", color="m", linewidth=4)
    ax = sns.lineplot(data=df, x="date", y="New Zeland", color="blue", linewidth=4)
    plt.axvline(3, linewidth=4, color="k")
    ax.set(xlabel="date", ylabel="Percentage of unemployment [%]")
    plt.title("Percentage of unemployment during the pandemic", y=1, x=0.5, fontsize=18)
    plt.xticks(rotation=30)
    plt.legend(['POL', 'NOW', 'AUS', 'EU', 'NZL'], bbox_to_anchor=(1, 1), prop={'size': 12})
    return plt.savefig("../images/fig12"), plt.close()


def main():
    df = load_csv('../data/unemployment.csv')
    create_plot(df)


if __name__=='__main__':
    main()