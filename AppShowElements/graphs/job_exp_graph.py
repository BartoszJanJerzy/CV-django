import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly as pl
import pandas as pd
import numpy as np
from datetime import datetime

from .graph import Graph


class JobExperienceGraph(Graph):
    def __init__(self):
        super().__init__()
        self.graph = self.__make_graph()


    def __get_colors(self) -> dict:
        colors = dict(
            grey1 = 'rgba(130, 130, 130, 0.35)',
            grey2 = 'rgba(70, 70, 70, 0.35)',
            grey3 = 'rgba(20, 20, 20, 0.35)',
            blue = 'rgba(0, 0, 255, 0.5)'
        )

        return colors


    def __get_trace_data(self, start: str, periods: int, value) -> dict:
        dates = pd.date_range(start=start, periods=periods, freq='M')
        values = [value for i in range(periods)]
        trace_dict = {d: v for d, v in zip(dates, values)}

        return trace_dict


    def __get_trace(self, name, x, y, color) -> go.Scatter:
        return go.Scatter(
            name=name,
            x=x,
            y=y,
            line=dict(
                color=color,
                width=15,
            ),
            mode='lines'
        )


    def __diff_month(self, d1, d2):
        return (d1.year - d2.year) * 12 + d1.month - d2.month


    def __make_graph(self) -> go.Figure():
        colors = self.__get_colors()

        fig = make_subplots(
            cols=1, rows=2,
            specs=[
                [{'type':'xy', "secondary_y": True}],
                [{'type':'table'}]
            ]
        )

        # Data Scientist
        periods_data = self.__diff_month(datetime.now(), datetime(2021, 7, 31))
        trace_dict = self.__get_trace_data('08/1/2021', periods_data, 3)
        fig.add_trace(
            self.__get_trace('Data Scientist', list(trace_dict.keys()), list(trace_dict.values()), colors['blue']),
            row = 1, col = 1
        )

        # Junior Research Specialist
        periods_research = 9
        trace_dict = self.__get_trace_data('11/1/2020', periods_research, 2)
        fig.add_trace(
            self.__get_trace('R&D Specialist', list(trace_dict.keys()), list(trace_dict.values()), colors['grey3']),
            row = 1, col = 1
        )

        # Social science
        periods_science = 28
        trace_dict = self.__get_trace_data('10/1/2019', periods_science, 1)
        fig.add_trace(
            self.__get_trace('PhD in Social Science', list(trace_dict.keys()), list(trace_dict.values()), colors['grey2']),
            row = 1, col = 1
        )

        # Other
        periods_other = 4
        trace_dict = self.__get_trace_data('7/1/2019', periods_other, 0)
        fig.add_trace(self.__get_trace('Other', list(trace_dict.keys()), list(trace_dict.values()), colors['grey1']),
            row = 1, col = 1
        )

        # Job satisfaction
        periods = self.__diff_month(datetime.now(), datetime(2019, 6, 30))
        dates = list(pd.date_range(start='7/1/2019', periods=periods, freq='M'))
        values_other = [10 + np.random.uniform(-0.2, 0.2) for i in range(periods_other)]
        values_science = [40 + np.random.uniform(-2, 2) for i in range(periods_science - 7)]
        values_data = [97 + np.random.uniform(-3, 3) for i in range(periods_data)]
        values = values_other + values_science + values_data
        fig.add_trace(go.Scatter(
            name='Job Satisfaction [%]',
            x=dates,
            y=values,
            mode='lines',
            line=dict(color='orange')
        ), secondary_y=True, row=1, col=1)

        #Table
        data_science_length = None
        if len(values_data) == 12:
            data_science_length = '1y'
        elif len(values_data) > 12:
            y = int(periods / 12)
            m = periods % 12
            data_science_length = f'{y}y {m}m'
        else:
            data_science_length = f'{len(values_data)}m'


        fig.add_trace(go.Table(
            header=dict(
                values = ['', 'Other', 'PhD', 'R&D Specialist', 'Data Scientist'],
                align = 'center',
                fill_color = ['white', colors['grey1'], colors['grey2'], colors['grey3'], colors['blue']]
            ),
            cells = dict(
                values = [['Time spent'], ['4m'], ['2y 4m'], ['9m'], [data_science_length]],
                align = 'center'
            )
        ), row=2, col=1)

        fig.update_layout(
            title=dict(
                text='History of my professional experience:<br>I switched industry to a Data Science and it strongly increased my job satisfaction.',
                font_size = 20,
                font = dict(family='Arial')
            ),
            yaxis=dict(visible=False),
            yaxis2=dict(
                title=None,
                titlefont=dict(color="orange"),
                tickfont=dict(color="orange"),
                anchor="free",
                side="right",
            ),
            margin = dict(b=0)
        )

        return fig