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
    return df


def create_plot(df):
    """create_plot
    This function create the bar plot, showing number of confirmed cases vs reported day
    Then its save this plot as png file

    :param df: the dataframe to the Naw Zealand data
    :return: png plot in .../images/fig3 png
    """
    sns.set_style("whitegrid")
    df_reverse = df.iloc[::-1]
    ax = sns.displot(df_reverse, x="Report Date", height=6, aspect=12/6, color="mediumseagreen", edgecolor="darkgreen")
    ax.set(xlabel="Report Date", ylabel="Number of cases")
    plt.title("Number of confirmed cases vs reported month", y=0.85, fontsize=16)
    return plt.savefig("../images/fig3"), plt.close()


def main():
    df = load_csv("../data/covid_cases_2021-04-29.csv")
    create_plot(df)


if __name__=='__main__':
    main()