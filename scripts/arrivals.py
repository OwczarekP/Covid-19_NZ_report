import plotly.express as px
import pandas as pd

def load_csv(path):
    df = pd.read_csv(path,)
    df['parameter'] = pd.to_datetime(df.parameter, format='%Y-%m-%d')
    return df[['sub_series_name', 'parameter', 'value',]]


def clean_data(df):
    df = df[df['parameter'].dt.year > 2018]
    df = df.reset_index()
    df['parameter'] = df['parameter'].apply(lambda x: x.strftime('%Y-%m'))
    df = df[['sub_series_name','value', 'parameter']]
    df = df.groupby(["parameter", 'sub_series_name'])["value"].mean().reset_index()
    return df


def create_plot(df):
    pass
    fig = px.scatter(df, x="parameter", y='sub_series_name',
                     size="value", color="sub_series_name",
                     hover_name="sub_series_name", size_max=60, template='plotly_white')
    fig.show()
    fig.write_image("../images/arrivals.png",  scale=1, width=1000, height=800)
    fig.write_html('../images/arrivals.html')


def main():
    df = load_csv('../data/arrivals_covid.csv')
    df = clean_data(df)
    create_plot(df)


if __name__=='__main__':
    main()