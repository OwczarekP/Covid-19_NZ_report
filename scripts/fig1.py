import plotly.express as px
import pandas as pd

def load_csv(path):
    df = pd.read_csv(path)
    return df


def clean_data(df):
    df_nzl = df.loc[df['iso_code'] == 'NZL']
    df_nzl = df_nzl[['date', 'total_cases', 'total_deaths',]]
    print(df_nzl.head())
    return df_nzl


def create_plot(df):
    fig = px.line(df, x="date", y=df.columns,
                  hover_data={"date": "|%B %d, %Y"},
                  title='Total COVID-19 cases', template='plotly_white')
    fig.add_vrect(x0="2020-03-25", x1="2020-05-13",
                  annotation_text="alert level 4", annotation_position="top left",
                  fillcolor="red", opacity=0.15, line_width=0)
    fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",
        title_standoff=25,
        title_font={"size": 20},)
    fig.update_yaxes(
        title_text="Total cases",
        title_font={"size": 20},
        title_standoff=25)
    fig.write_image("../images/fig1.png",  scale=1, width=1000, height=800)


def main():
    df = load_csv('../data/owid-covid-data.csv')
    df = clean_data(df)
    create_plot(df)


if __name__=='__main__':
    main()