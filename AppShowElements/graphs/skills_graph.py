import plotly.graph_objects as go
from .graph import Graph


class SkillsGraph(Graph):
    def __init__(self):
        super().__init__()
        self.labels, self.values = self.__prepare_data()
        self.graph = self.__prepare_graph()


    def __prepare_data(self):
        labels = ['Python', 'Git version control', 'Front-end (HTML, CSS, JS)', 'SQL']
        values = [1 for i in range(len(labels))]

        return labels, values


    def __prepare_graph(self):
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            name = 'Yet beginner',
            y = self.labels[1:],
            x = self.values[1:],
            mode = 'markers',
            marker = dict(
                symbol = 'square',
                size = 30,
                color = 'rgba(0,200,0,0.75)'
            )
        ))
        fig.add_trace(go.Scatter(
            name = 'Already upper-intermediate',
            y = self.labels[:1],
            x = self.values[:1],
            mode = 'markers',
            marker = dict(
                symbol = 'hexagram',
                size = 50,
                color = 'orange'
            )
        ))

        fig.update_xaxes(visible=False)

        fig.update_layout(
            title=dict(
                text='My programming skills are based on Python:',
                font_size=20,
                font=dict(family='Arial')
            ),
        )

        return fig