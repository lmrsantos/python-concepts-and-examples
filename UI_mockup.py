'''
This code will create a simple web app with a text input field and a submit button. 
When the user clicks the submit button, the output of the input field will be displayed in the output div
'''
import dash
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div([
    html.H1('Mockup UI'),
    dcc.Input(id='input', type='text'),
    html.Button('Submit', id='submit'),
    html.Div(id='output')
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8000)