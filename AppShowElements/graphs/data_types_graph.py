import pandas as pd
import plotly.express as px
from .graph import Graph


class DataTypesGraph(Graph):
    def __init__(self):
        super().__init__()
        self.__graph_df = self.__prepare_data()
        self.graph = self.__prepare_graph()


    def __prepare_graph(self):
        fig = px.bar(self.__graph_df, y='[%]', x='x', color='Data type', text='text')
        fig.update_traces(
            textfont=dict(
                size=16,
                # color='white',
                family='Arial'
            )
        )
        fig.update_layout(
            title=dict(
                text='I analyse mainly FMCG producers and customers data:',
                font_size=20,
                font=dict(family='Arial')
            ),
        )
        fig.update_xaxes(title=None)
        fig.update_yaxes(range=[0, 120])

        return fig


    def __prepare_data(self):
        values = [80, 15, 5]
        tasks = ['FMCG sector', 'Invoice behavior', 'Natural language texts']
        x = ['Data type' for i in range(len(values))]
        texts = [f'{text} [{value}%]' for text, value in zip(tasks, values)]

        graph_df = pd.DataFrame({
            '[%]': values,
            'x': x,
            'Data type': tasks,
            'text': texts
        })

        return graph_df