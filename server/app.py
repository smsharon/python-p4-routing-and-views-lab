#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route ('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h2>'

@app.route ('/print/<string:string>')
def print_string(string):
    print(string)
    return string

@app.route ('/count/<int:number>')
def count(number):
    numbers = "\n".join([str(i) for i in range(1, number + 1)])
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        result = "Invalid operation"

    return f"Result: {result}"
if __name__ == '__main__':
    app.run(port=5555, debug=True)
