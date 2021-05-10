import operator
import math


def ctg(x):
    return 1 / math.tan(x)


def arcctg(x):
    return 1 / math.atan(x)


OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': math.pow,
             'div': operator.floordiv, '%': operator.mod}

FUNCTIONS = {'cos': math.cos, 'arccos': math.acos, 'sin': math.sin, 'arcsin': math.asin, 'tg': math.tan,
             'arctg': math.atan, 'ctg': ctg,
             'arcctg': arcctg, 'abs': abs, 'sqrt': math.sqrt, 'deg': math.radians, 'exp': math.exp, 'log': math.log}

PRIORITY = {1: ['+', '-', ], 2: ['*', '/', 'div', '%'],
            3: ['sin', 'asin', 'cos', 'acos', 'tg', 'artctg', 'ctg', 'arcctg', 'abs', 'sqrt', '^', 'deg', 'exp', 'log']}


def calculate_polish(str):
    stack = []
    str = str.split()
    for i in str:
        if i.isdigit():
            stack.append(i)
        if i in OPERATORS.keys():
            value1, value2 = stack.pop(), stack.pop()
            stack.append(OPERATORS[i](int(value2), int(value1)))
        if i in FUNCTIONS.keys():
            if i == 'log':
                value1, value2 = stack.pop(), stack.pop()
                stack.append(FUNCTIONS[i](int(value2), int(value1)))
            else:
                value1 = stack.pop()
                stack.append(FUNCTIONS[i](float(value1)))

    return stack.pop()
