import plotly as pl
import plotly.graph_objects as go



class Graph:
    def __init__(self):
        self.graph = go.Figure()


    def get_graph(self):
        dj_graph = pl.offline.plot(self.graph, output_type='div')
        return dj_graph