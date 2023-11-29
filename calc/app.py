"""simple calculator"""

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get('/add')
def get_add_result():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(add(a, b))

@app.get('/sub')
def get_sub_result():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(sub(a, b))

@app.get('/mult')
def get_mult_result():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(mult(a, b))

@app.get('/div')
def get_div_result():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(div(a, b))