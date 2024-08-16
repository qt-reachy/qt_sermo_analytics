# Import packages
from dash import Dash, dcc, html, Input, Output, State, callback
import functions
from functions import BuildDataFrame

# Incorporate data
Users = BuildDataFrame('logs.csv')
data = Users.main()

# Initialize the app
app = Dash(__name__)
app.title = 'QT Analytics'

# Custom variables
title = '''
# QT Analtics
Analytics for QT robot @ArcadaUAS
'''

credits = '''
Made by Kristoffer Kuvaja Adolfsson, ArcadaUAS 2024
'''

DropDown = data['user'].tolist()

Actions = data.loc[:, data.columns != 'user'].columns.values.tolist()

# App layout
app.layout = html.Div(children=[
    dcc.Markdown(children=title, style={'textAlign': 'center'}),
    # top div
    html.Div([
        # Filter by user
        html.Button("Select/Unselect All", id="select-all-users", n_clicks=0),
        html.Div([
            dcc.Dropdown(
            options=DropDown,
            value=DropDown,
            multi=True,
            id='filter-user'
        )
        ]),
        html.Div([
            dcc.Checklist(
                options=Actions,
                value=Actions,
                inline=True
            )
        ])
    ]),
])

@app.callback(
    Output("filter-user", "value"),
    [Input("select-all-users", "n_clicks")],
    [State("filter-user", "value")])
def select_all_users(n_clicked, value):
    if len(value) > 0 and n_clicked > 0:
        return []
    else:
        return DropDown

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
