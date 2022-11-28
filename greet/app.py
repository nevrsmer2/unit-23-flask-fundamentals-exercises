from flask import Flask, request

app = Flask(__name__)

# Greet Routes

# 1. /Welcome
@app.route('/welcome')
def greet_user():
    '''returns welcome'''
    # return "Welcome!"
    # or:
    html = '''<htm>
    <body>
     <h1>Welcome!</h1>
    </body>
     </html>'''
    return html


# 2. /welcome/home
@app.route('/welcome/home')
def welcome_home():
    '''returns Welcome home!'''
    # return "Welcome home!"
    # or:
    html = '''<htm>
    <body>
     <h1>Welcome home!</h1>
    </body>
     </html>'''
    return html


# 2. /welcome/back
@app.route('/welcome/back')
def welcome_back():
    '''returns Welcome back!'''
    # return "Welcome back!"
    # or:
    html = '''<htm>
    <body>
     <h1>Welcome back!</h1>
    </body>
     </html>'''
    return html
