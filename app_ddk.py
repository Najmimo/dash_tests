"""AI is creating summary for

Returns:
    [type]: [description]
"""

import random as rd
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import Dash, html, dash_table, dcc, Output, Input, callback


class StatDynamics:
    """
    DocStrings explaining this class.
    """

    # List of countries (you can adjust this as needed)
    COUNTRIES = [
        "Austria",
        "Belgium",
        "Bulgaria",
        "Croatia",
        "Cyprus",
        "Czech Republic",
        "Denmark",
        "Estonia",
        "Finland",
        "France",
        "Germany",
        "Greece",
        "Hungary",
        "Ireland",
        "Italy",
        "Latvia",
        "Lithuania",
        "Luxembourg",
        "Malta",
        "Netherlands",
        "Poland",
        "Portugal",
        "Romania",
        "Slovakia",
        "Slovenia",
        "Spain",
        "Sweden",
        "United Kingdom",
    ]

    def __init__(self):
        self.app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])
        self.stat_dataframe = pd.DataFrame()
        # Schedule the update every 1 second
        # task = threading.Timer(1, self.update_data())
        # task.start()
        self.init_data_frame()
        self.build_layouts()

        if self.app is not None and hasattr(self, "callbacks_dash_table"):
            self.callbacks_dash_table(self.app)
        if self.app is not None and hasattr(self, "callbacks_dash_histo"):
            self.callbacks_dash_histo(self.app)

    def init_data_frame(self):
        """AI is creating summary for init_data_frame"""
        self.stat_dataframe = pd.DataFrame(
            [
                {
                    "Country": ele,
                    "1Y_Rate": rd.uniform(3, 5.1),
                    "5Y_Rate": rd.uniform(1.5, 4.5),
                    "10Y_Rate": rd.uniform(2.5, 3.0),
                    "Unemployment": rd.uniform(3.0, 12.0),
                    "GDP_Growth": rd.uniform(-2.0, 5.0),
                }
                for ele in self.COUNTRIES
            ]
        )

    def generate_random_data(self):
        """AI is creating summary for generate_random_data

        Returns:
            [type]: [description]
        """
        return [
            {
                "Country": ele,
                "1Y_Rate": rd.uniform(0, 5.1),
                "5Y_Rate": rd.uniform(1.5, 4.5),
                "10Y_Rate": rd.uniform(2.5, 3.0),
                "Unemployment": rd.uniform(3.0, 15.0),
                "GDP_Growth": rd.uniform(-2.0, 5.0),
            }
            for ele in self.COUNTRIES
        ]

    def update_data(self):
        """Update data every 10 secondes"""
        return pd.DataFrame(self.generate_random_data())

    def build_layouts(self):
        """AI is creating summary for build_layouts"""
        self.app.layout = dbc.Container(
            [
                dbc.Row(
                    [
                        html.Div(
                            "Dynamics Rates indicators",
                            className="text-primary text-center fs-3",
                            style={"border": "1px solid black"},
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dash_table.DataTable(
                            id="Data_Table",
                            columns=[
                                {"name": col, "id": col}
                                for col in self.stat_dataframe.columns
                            ],
                            data=self.stat_dataframe.to_dict("records"),
                            style_table={
                                "height": "300px",
                                "overflowY": "auto",
                                "border": "1px solid black",
                            },
                            style_cell={
                                "textAlign": "center"
                            },  # Align cell text to the left
                            style_header={
                                "backgroundColor": "lightgreen",
                                "fontWeight": "bold",
                                "border": "2px solid black",  # Add a solid black border
                            },  # Customize header background color
                            style_data={"border": "2px solid black"},
                            style_data_conditional=[
                                {
                                    "if": {
                                        "filter_query": f"{{{col}}} >= 2.1 && {{{col}}} <= 2.5",
                                        "column_id": col,
                                    },
                                    "backgroundColor": "#FFA500",  # Set your desired background color
                                    "color": "black",  # You can customize the font color here
                                    "fontWeight": "bold",
                                    # "animation": {
                                    # "name": "blinking",
                                    # "duration": 1,  # Duration in seconds
                                    # "iterationCount": "infinite",  # Infinite blinking
                                    # },
                                }
                                for col in self.stat_dataframe.columns[1:]
                            ]
                            + [
                                {
                                    "if": {
                                        "filter_query": "{GDP_Growth} <= 0.5",
                                        "column_id": "GDP_Growth",
                                    },
                                    "backgroundColor": "red",  # Set your desired background color
                                    "color": "black",  # You can customize the font color here
                                    "fontWeight": "bold",
                                    # "animation": {
                                    # "name": "blinking",
                                    # "duration": 1,  # Duration in seconds
                                    # "iterationCount": "infinite",  # Infinite blinking
                                    # },
                                }
                            ]
                            + [
                                {
                                    "if": {
                                        "filter_query": "{GDP_Growth} >= 4.5",
                                        "column_id": "GDP_Growth",
                                    },
                                    "backgroundColor": "lightgreen",  # Set your desired background color
                                    "color": "black",  # You can customize the font color here
                                    "fontWeight": "bold",
                                    # "animation": {
                                    # "name": "blinking",
                                    # "duration": 1,  # Duration in seconds
                                    # "iterationCount": "infinite",  # Infinite blinking
                                    # },
                                }
                            ]
                            + [
                                {
                                    "if": {
                                        "filter_query": "{Unemployment} <= 4.5",
                                        "column_id": "Unemployment",
                                    },
                                    "backgroundColor": "lightgreen",  # Set your desired background color
                                    "color": "black",  # You can customize the font color here
                                    "fontWeight": "bold",
                                    "animation": {
                                        "name": "blinking",
                                        "duration": 5,  # Duration in seconds
                                        "iterationCount": "infinite",  # Infinite blinking
                                    },
                                }
                            ],
                        ),
                    ]
                ),
                html.Br(),  # Add vertical space
                dbc.Row(
                    dcc.RadioItems(
                        id="chart-radio",
                        labelStyle={
                            "display": "inline-block",
                            "margin-right": "10px",
                        },  # Add margin-right
                        options=[
                            {"label": col, "value": col}
                            for col in self.stat_dataframe.columns[1:]
                        ],
                        inputStyle={
                            "margin-right": "4px"
                        },  # Add space to the right of the radio button
                        value=self.stat_dataframe.columns[1],
                    ),
                ),
                html.Br(),  # Add vertical space
                dbc.Row(
                    [
                        html.Div(
                            "Average data per country",
                            className="text-center fs-3",
                            style={
                                "font-family": "Arial, sans-serif",  # Change font family
                                "color": "red",  # You can customize the font color here
                                "fontWeight": "bold",
                            },
                        ),
                        dcc.Graph(
                            id="histogram-chart",
                            style={"border": "2px solid #000", "border-radius": "5px"},
                            figure={
                                "data": [],  # Your data (leave empty for now)
                                "layout": {
                                    "xaxis": {
                                        "title": "Indicateurs économiques"
                                    },  # Customize x-axis label
                                    "yaxis": {
                                        "title": "Moyenne indicateur économique"
                                    },  # Customize y-axis label
                                },
                            },
                        ),
                    ]
                ),
                dcc.Interval(
                    id="table_update",
                    interval=5 * 1000,  # Update every 10 seconds (in milliseconds)
                    n_intervals=0,
                ),
            ]
        )

    def callbacks_dash_histo(self, app):
        """AI is creating summary for update_table

        Args:
            _ ([type]): [description]

        Returns:
            [type]: [description]
        """

        @app.callback(
            Output("histogram-chart", "figure"),
            Input("table_update", "n_intervals"),
            # Input("histogram-chart", "relayoutData")
        )
        def update_histogram(_):
            """AI is creating summary for update_table

            Args:
                _ ([type]): [description]

            Returns:
                [type]: [description]
            """
            relevant_columns = [
                "1Y_Rate",
                "5Y_Rate",
                "10Y_Rate",
                "Unemployment",
                "GDP_Growth",
            ]
            avg_values = self.stat_dataframe[relevant_columns].mean()

            # Create a histogram figure
            fig = px.histogram(
                avg_values,
                x=avg_values.index,
                y=avg_values.values,
                labels={"x": "Column", "y": "Average Value"},
            )
            # Customize axis labels
            fig.update_xaxes(title_text="Indicateurs économiques")
            fig.update_yaxes(title_text="Moyenne Indicateur économique")
            return fig

    def callbacks_dash_table(self, app):
        """AI is creating summary for update_table

        Args:
            _ ([type]): [description]

        Returns:
            [type]: [description]
        """

        @app.callback(
            Output("Data_Table", "data"), [Input("table_update", "n_intervals")]
        )
        def update_table(_):
            """AI is creating summary for update_table

            Args:
                _ ([type]): [description]

            Returns:
                [type]: [description]
            """
            self.stat_dataframe = self.update_data()
            return self.stat_dataframe.to_dict("records")


if __name__ == "__main__":
    stat_dynamics_instance = StatDynamics()
    stat_dynamics_instance.app.run(debug=True)
