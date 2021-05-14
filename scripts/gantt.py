import plotly.express as px
import pandas as pd
import plotly.figure_factory as FF


def load_csv(path):
    df = pd.read_csv(path)
    #because gannt otherwise put whole 2 years as x axis:
    df['start'] = df.start.str.replace('2021', '2020')
    df['end'] = df.end.str.replace('2021', '2020')
    print(df.head(20))
    return df


def create_plot(df):
    color_dict = {1: 'rgb(47, 186, 47)',
                  2: 'rgb(233, 218, 47)',
                  3: 'rgb(206, 88, 47)',
                  4: 'rgb(206, 0, 0)',
                  }
    df['Task'] = df['year']
    df['Start'] = df['start']
    df['Finish'] = df['end']
    fig = FF.create_gantt(df, colors=color_dict, index_col='level', show_colorbar=True,
                          title='Alert levels in 2020-2021 in New Zealand', group_tasks=True,
                          bar_width=0.5)
    fig.layout.xaxis.tickformat = '%d-%m'
    fig.update_yaxes(autorange="reversed")


    fig.show()
    fig.write_image("../images/gantt.png",  scale=1, width=1000, height=500)
    fig.write_html('../images/gantt.html')


def main():
    df = load_csv('../data/alerts.csv')
    create_plot(df)


if __name__=='__main__':
    main()