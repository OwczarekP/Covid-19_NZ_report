import plotly.express as px
import pandas as pd

def load_csv(path):
    df = pd.read_csv(path)
    return df


def clean_data_cases(df):
    df_nzl = df.loc[df['iso_code'] == 'NZL']
    df_nzl = df_nzl[['date', 'new_cases']]
    return df_nzl


def clean_data_vacc(df):
    df = df.loc[df['indicator_name'] == 'Covid-19 Vaccines Administered – Daily total']
    df['date'] = df['parameter']
    df['daily_vaccination'] = df['value']
    df = df[['date', 'daily_vaccination']]
    return df


def create_plot(df, df_vacc):
    df = df.merge(df_vacc, on='date')
    fig = px.line(df, x="date", y=df.columns,
                  hover_data={"date": "|%B %d, %Y"},
                  title='COVID-19 - daily vaccination vs daily cases', template='plotly_white')
    fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",
        title_standoff=25,
        title_font={"size": 20},)
    fig.update_yaxes(
        title_text="Total cases",
        title_font={"size": 20},
        title_standoff=25)
    fig.write_image("../images/fig5.png",  scale=1, width=1000, height=800)


def main():
    df = load_csv('../data/owid-covid-data.csv')
    df_vacc = load_csv('../data/covid_19_data_vaccination.csv')
    df_vacc = clean_data_vacc(df_vacc)
    df = clean_data_cases(df)
    create_plot(df, df_vacc)


if __name__=='__main__':
    main()