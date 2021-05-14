import plotly.express as px
import pandas as pd


def load_csv(path):
    """load_csv
    This function load the file from the path and save it as dataframe

    :param path: string to the csv file
    :return: df: the dataframe from the csv
    """
    df = pd.read_csv(path)
    df['parameter'] = pd.to_datetime(df.parameter, format='%Y-%m-%d')
    return df[['sub_series_name', 'parameter', 'value',]]


def clean_data(df):
    """clean_data
    This function filter the data to shows only rows after 2018
    Then filter the data to get monthly average arrivals by airport

    :param df:  the dataframe from the csv file
    :return: df_combine: the dataframe with average monthly arrivals
    """
    df = df[df['parameter'].dt.year > 2018]
    df = df.reset_index()
    df['parameter'] = df['parameter'].apply(lambda x: x.strftime('%Y-%m'))
    df = df[['sub_series_name','value', 'parameter']]
    df = df.groupby(["parameter", 'sub_series_name'])["value"].mean().reset_index()
    df.columns = ['Date', 'Airport', 'Arrivals']
    return df


def create_plot(df):
    """create_plot
    This function create the bubble plot, showing number of average monthly arrivals by airtport
    Then its save this plot as png file and html file

    :param df: the dataframe to the Naw Zealand data
    :return: None
    """
    fig = px.scatter(df, x="Date", y='Airport',
                     size="Arrivals", color="Arrivals",
                     hover_name="Airport", size_max=60, template='plotly_white')
    fig.update_layout(legend_title_text='Arrivals')
    fig.update_layout(title_font_size=30)
    fig.update_layout(
        title={
            'text': 'Airport arrivals'})
    fig.update_yaxes(
        title_text="Airport",
        title_font={"size": 20},
        title_standoff=25,
        tickfont_size=17)
    fig.update_xaxes(
        title_text="Date",
        title_font={"size": 20},
        title_standoff=25,
        tickfont_size=17)

    fig.write_image("../images/fig13.png",  scale=1, width=1000, height=800)
    fig.write_html('../images/fig13.html')


def main():
    df = load_csv('../data/arrivals_covid.csv')
    df = clean_data(df)
    create_plot(df)


if __name__=='__main__':
    main()