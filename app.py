# Import packages
from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import functions
from functions import UsersDataFrame

# Incorporate data
Users = UsersDataFrame('logs.csv')

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'QT Analytics'

# Custom variables
title = '''
# QT Analtics @ArcadaUAS
'''

credits = '''
Made by Kristoffer Kuvaja Adolfsson, ArcadaUAS 2024
'''

DropDown = Users.get_users()
Actions = Users.get_actions()

# App layout
app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col(html.Img(src="assets/arcada_crop.png",
                style={"max-width": 250}), width=4),
        dbc.Col(html.H1(children=['QT Analtics App']),
                width=8, style={"textAlign": "right", "font-family": "futura-pt, fallback, arial, sans-serif"}),
    ], style={"max-height": 200, "padding": "2vh"}, justify='start'),
    dbc.Tabs([
        dbc.Tab(label="Selector", children=[
            dbc.Row([
                dcc.Dropdown(
                    options=DropDown,
                    value=DropDown,
                    multi=True,
                    id='filter-user'
                )
            ]),
            dbc.Row([
                dbc.Col(dbc.Button("Select/Unselect All",
                                   id="select-all-users", n_clicks=0), width=4)
            ]),
            dbc.Row([
                dbc.Checklist(
                    options=Actions,
                    value=Actions,
                    switch=True
                )
            ])
        ]),
        dbc.Tab(label="Graphs", children=[
            dbc.Container(id='plots-graphs')
        ]),
        dbc.Tab(label="Table", children=[
            dbc.Row(id='user-table')
        ]),
        dbc.Tab(label="Raw", children=[
            dbc.Table.from_dataframe(
                Users.get_raw_data(), bordered=True, hover=True, id='raw-data')
        ]),
    ])
])


@ app.callback(
    Output("filter-user", "value"),
    [Input("select-all-users", "n_clicks")],
    [State("filter-user", "value")])
def select_all_users(n_clicked, value):
    if len(value) > 0 and n_clicked > 0:
        return []
    else:
        return DropDown


@ app.callback(
    Output('user-table', 'children'),
    [Input('filter-user', 'value')],
)
def update_user_table(value):
    _df = Users.get_exploded_user(value)
    return dbc.Table.from_dataframe(_df, bordered=True, hover=True)

@ app.callback(
    Output('plots-graphs', 'children'),
    [Input('filter-user', 'value')],
)
def plots_and_graphs(value):
    _df = Users.get_exploded_user(value)
    # fig = functions.simple_time(_df)
    fig = functions.bar_chart_interactions(_df)
    return dcc.Graph(figure=fig)



# Run the app
if __name__ == '__main__':
    app.run(debug=True)
