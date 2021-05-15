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
    This function filter the data to shows only New Zealand cases
    Then it save new dataframe with only date, total cases and total deaths

    :param df:  the dataframe from the csv file
    :return: df_nzl: the dataframe for New Zealand with selected columns
    """
    df_nzl = df.loc[df['iso_code'] == 'NZL']
    df_nzl = df_nzl[['date', 'total_cases', 'total_deaths',]]
    return df_nzl


def create_plot(df):
    """create_plot
    This function create the line plot, showing total covid-19 cases and deaths
    It shows the period od alert level 4
    Then its save this plot as png file

    :param df: the dataframe to the Naw Zealand data
    :return:
    """
    fig = px.line(df, x="date", y=df.columns,
                  hover_data={"date": "|%B %d, %Y"},
                  title='Total COVID-19 cases', template='plotly_white',)
    fig.add_vrect(x0="2020-03-25", x1="2020-05-13",
                  annotation_text="alert level 4", annotation_position="top left",
                  fillcolor="red", opacity=0.15, line_width=0)
    fig.update_traces(line=dict(width=3.5))
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
    fig.write_image("../images/fig1.png",  scale=1, width=1000, height=800)


def main():
    df = load_csv('../data/owid-covid-data.csv')
    df = clean_data(df)
    create_plot(df)


if __name__=='__main__':
    main()