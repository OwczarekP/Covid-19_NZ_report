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


def clean_data(df):
    """clean_data
    This function filter the data to shows selected countries
    Then it save new dataframe with only date and total cases per million,
    and merge all countries into one dataframe

    :param df:  the dataframe from the csv file
    :return: df_combine: the dataframe for selected countries with selected columns
    """
    df_nzl = df.loc[df['iso_code'] == 'NZL']
    df_nzl = df_nzl[['date', 'total_cases_per_million']]
    df_nzl.columns = ['date', 'NZL']
    df_ner = df.loc[df['iso_code'] == 'NER']
    df_ner = df_ner[['date', 'total_cases_per_million']]
    df_ner.columns = ['date', 'NER']
    df_pol = df.loc[df['iso_code'] == 'POL']
    df_pol = df_pol[['date', 'total_cases_per_million']]
    df_pol.columns = ['date', 'POL']
    df_eu = df.loc[df['iso_code'] == 'OWID_EUN']
    df_eu = df_eu[['date', 'total_cases_per_million']]
    df_eu.columns = ['date', 'EU']
    df_aus = df.loc[df['iso_code'] == 'AUS']
    df_aus = df_aus[['date', 'total_cases_per_million']]
    df_aus.columns = ['date', 'AUS']
    df_nor = df.loc[df['iso_code'] == 'NOR']
    df_nor = df_nor[['date', 'total_cases_per_million']]
    df_nor.columns = ['date', 'NOR']
    df_combine = pd.concat([df_aus, df_eu, df_pol, df_ner, df_nzl, df_nor])
    return df_combine


def create_plot(df):
    """create_plot
    This function create the line plot, showing total covid-19 cases per million for selected countries
    Then its save this plot as png file and html file

    :param df: the dataframe to the Naw Zealand data
    :return:
    """
    fig = px.line(df, x="date", y=df.columns,
                  hover_data={"date": "|%B %d, %Y"},
                  title='Total cases of COVID-19 per million', template='plotly_white')
    fig.update_yaxes(title_text='Cases per million',
        title_standoff=25,
        title_font={"size": 20},
        tickfont_size=17)
    fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",
        title_standoff=25,
        title_font={"size": 20},
        tickfont_size=17)
    fig.update_layout(legend_title_text='Country code')
    fig.write_html('../images/fig2.html')
    fig.write_image("../images/fig2.png")


def main():
    df = load_csv('../data/owid-covid-data.csv')
    df = clean_data(df)
    create_plot(df)


if __name__=='__main__':
    main()