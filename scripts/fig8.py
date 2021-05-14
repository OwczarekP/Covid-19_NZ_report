import plotly.express as px
import pandas as pd


def load_csv(path):
    """load_csv
    This function load the file from the path and save it as dataframe

    :param path: string to the csv file
    :return: df: the dataframe from the csv
    """
    df = pd.read_csv(path)
    return df


def clean_data_cases(df):
    """clean_data_cases
    This function filter the covid-19 data, to get only daily new cases
    and change the title of column to create plot


    :param df: the data about covid-19 cases in New Zealand
    :return: df: the data about date and daily new cases in New Zealand
    """
    df_nzl = df.loc[df['iso_code'] == 'NZL']
    df_nzl = df_nzl[['date', 'new_cases']]
    return df_nzl


def clean_data_vacc(df):
    """clean_data_vacc
    This function filter the vaccination data, to get only daily vaccination,
    and change the title of column to create plot

    :param df: the data about vaccination in New Zealand
    :return: df: the data about date and daily vaccination in New Zealand
    """
    df = df.loc[df['indicator_name'] == 'Covid-19 Vaccines Administered – Daily total']
    df['date'] = df['parameter']
    df['daily_vaccination'] = df['value']
    df = df[['date', 'daily_vaccination']]
    return df


def create_plot(df, df_vacc):
    """create_plot
    This function create the line plot, showing total covid-19 cases and deaths
    It shows the period od alert level 4
    Then its save this plot as png file

    :param df: the dataframe to the Naw Zealand data
        df_vacc: the dataframe to the data about vaccination
    :return:
    """
    df = df.merge(df_vacc, on='date')
    fig = px.line(df, x="date", y=df.columns,
                  hover_data={"date": "|%B %d, %Y"},
                  title='COVID-19 - daily vaccination vs daily cases', template='plotly_white')
    fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",
        title_standoff=25,
        title_font={"size": 20},
        tickfont_size=17)
    fig.update_yaxes(
        title_text="Total cases",
        title_font={"size": 20},
        title_standoff=25,
        tickfont_size=17)
    fig.write_image("../images/fig8.png",  scale=1, width=1000, height=800)


def main():
    df = load_csv('../data/owid-covid-data.csv')
    df_vacc = load_csv('../data/covid_19_data_vaccination.csv')
    df_vacc = clean_data_vacc(df_vacc)
    df = clean_data_cases(df)
    create_plot(df, df_vacc)


if __name__=='__main__':
    main()