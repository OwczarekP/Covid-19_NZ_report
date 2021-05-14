from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def load_csv(path):
    """load_csv
    This function load the file from the path and save it as dataframe
    Additionaly its create new column which is subtract of two other columns

    :param path: string to the csv file
    :return: df: the dataframe from the csv
    """
    df = pd.read_csv(path)
    df['not_vaccinated']= df['total_population'].tolist() - df['total_vaccination']
    return df[['country', 'total_vaccination', 'not_vaccinated']]


def create_plot(df):
    """create_plot
    This function create the pie chart, showing the number of vaccinated and not-vaccinated people
    in selected countries
    Then its save this plot as png file and html file

    :param df: the dataframe to the Naw Zealand data
    :return: None
    """
    countries = df['country'].unique()
    labels = ['not vaccinated', 'vaccinated']

    fig = make_subplots(rows=1, cols=3, specs=[[{"type": "pie"}, {"type": "pie"}, {"type": "pie"}]],
                        subplot_titles=['New Zealand','Poland', 'Australia'])

    i = 1
    for country in countries:
        temp = df.loc[df['country'] == country]
        fig.add_trace(go.Pie(labels=labels, values=[temp.iloc[0]['not_vaccinated'], temp.iloc[0]['total_vaccination']],
                             name=country, marker_colors=px.colors.qualitative.Antique), row=1, col=i)
        i += 1

    for j in fig['layout']['annotations']:
        j['font'] = dict(size=25,)

    fig.update_layout(title_text='Covid-19 vaccination ratio')
    fig.update_layout(title_font_size=30)
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20)
    # plot(fig)
    fig.show()
    fig.write_image("../images/fig9.png",  scale=1, width=1000, height=600)


def main():
    df = load_csv('../data/vacc_pop.csv')
    create_plot(df)


if __name__=='__main__':
    main()