from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def load_csv(path):
    df = pd.read_csv(path)
    df['not_vaccinated']= df['total_population'].tolist() - df['total_vaccination']
    return df[['country', 'total_vaccination', 'not_vaccinated']]

def create_plot(df):
    # Create subplots, using 'domain' type for pie charts
    countries = df['country'].unique()
    labels = ['not vaccinated', 'vaccinated']

    fig = make_subplots(rows=1, cols=3, specs=[[{"type": "pie"}, {"type": "pie"}, {"type": "pie"}]],
                        subplot_titles=['New Zealand','Poland', 'Australia'])

    i = 1
    for country in countries:
        temp = df.loc[df['country'] == country]
        fig.add_trace(go.Pie(labels=labels, values=[temp.iloc[0]['not_vaccinated'], temp.iloc[0]['total_vaccination']],
                             name=country, marker_colors=px.colors.qualitative.Bold), row=1, col=i)
        i += 1

    fig.update_layout(title_text='Covid-19 vaccination ratio')
    # plot(fig)
    fig.show()
    fig.write_image("../images/fig7.png",  scale=1, width=1000, height=600)


def main():
    df = load_csv('../data/vacc_pop.csv')
    create_plot(df)


if __name__=='__main__':
    main()