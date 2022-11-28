from flask import Flask, request
from operator import add, sub, mul, truediv

app = Flask(__name__)

# Part 1

# Addition
@app.route('/add')
def add_ints():

    '''Return the sum of parameters a and b'
        >>>> http://127.0.0.1:5000/add?a=10&b=50 
        >>>> Returns: 60
'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    sum = a + b
    return str(sum)

  
#   Subtraction
@app.route('/subtract')
def subtract():

    '''Return the difference between parameters a and b
        >>>> http://127.0.0.1:5000/subtract?a=10&b=50 
        >>>> Returns: -40
'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    difference = a - b
    return str(difference)


# Multiplications
@app.route('/multiply')
def multiply():

    '''Returns the product of parameters a and b
            >>>>http://127.0.0.1:5000/multiply?a=10&b=50
            >>>>Returns: 500
    '''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    product = a * b
    return str(product)


# Division
@app.route('/divide')
def divide():

    '''Returns the quotient of parameters a and b
        >>>>http://127.0.0.1:5000/divide?a=10&b=50 returns 
        >>>>Returns: 0.2'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    quotient = a / b
    return str(quotient)


'''-----------------------------------'''


#  Part 2

#  Create dictionairy  for mathematical operations  functions

OPERATIONS = {
    'add': add,
    'subtract': sub,
    'multiply': mul,
    'divide': truediv,
}


@app.route('/operations/<operator>')
def do_math(operator):

    '''Route that performs the mathematical operations in the dictionary OPERATIONS when  called by a user

        >>>  http://127.0.0.1:5000/operations/add?a=10&b=50
        60

        >>> http://127.0.0.1:5000/operations/subtract?a=10&b=50
        -40

        >>> http://127.0.0.1:5000/operations/multiply?a=10&b=50
        500

        >>>  http://127.0.0.1:5000/operations/divide?a=10&b=50
        0.2
'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    operation = OPERATIONS[operator]
    
    result = operation(a, b)

    return str(result)
