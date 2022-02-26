import pandas as pd
import plotly.express as px
from .graph import Graph


class TasksGraph(Graph):
    def __init__(self):
        super().__init__()
        self.__graph_df = self.__prepare_data()
        self.graph = self.__prepare_graph()


    def __prepare_graph(self):
        fig = px.bar(self.__graph_df, y='[%]', x='x', color='Task type', text='text')
        fig.update_traces(
            textfont=dict(
                size=16,
                color='white',
                family='Arial'
            )
        )
        fig.update_layout(
            title=dict(
                text='My current job tasks includes 4 main sectors:',
                font_size=20,
                font=dict(family='Arial')
            ),
        )
        fig.update_xaxes(title=None)
        fig.update_yaxes(range=[0, 120])

        return fig


    def __prepare_data(self):
        values = [30, 30, 25, 15]
        tasks = ['Data visualization', 'Web dashboardapp development', 'Unsupervised ML', 'Supervised ML']
        x = ['Task type' for i in range(len(values))]
        texts = [f'{text} [{value}%]' for text, value in zip(tasks, values)]

        graph_df = pd.DataFrame({
            '[%]': values,
            'x': x,
            'Task type': tasks,
            'text': texts
        })

        return graph_df