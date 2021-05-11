import plotly.express as px
import pandas as pd

def load_csv(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
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
    fig = px.line(df, x="date", y=df.columns,
                  hover_data={"date": "|%B %d, %Y"},
                  title='Total cases of COVID-19 per million', template='plotly_white')
    fig.update_yaxes(title_text='Cases per million')
    fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y")
    fig.update_layout(legend_title_text='Country code')
    fig.show()
    fig.write_html('../images/fig2.html')
    fig.write_image("../images/fig2.png")

def main():
    df = load_csv('../data/owid-covid-data.csv')
    df = clean_data(df)
    create_plot(df)


if __name__=='__main__':
    main()