import operator
import math


def ctg(x):
    return 1 / math.tan(x)


def arcctg(x):
    return 1 / math.atan(x)


OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': math.pow,
             'div': operator.floordiv, '%': operator.mod}

FUNCTIONS = {'cos': math.cos, 'sin': math.sin, 'tg': math.tan, 'arctg': math.atan, 'ctg': ctg,
             'arcctg': arcctg, 'abs': abs, 'sqrt': math.sqrt}

PRIORITY = {1: ['+', '-', ], 2: ['*', '/', 'div', '%'],
            3: ['sin', 'cos', 'tg', 'artctg', 'ctg', 'arcctg', 'abs', 'sqrt', '^']}


# def polishCalculation(srt):
#     stack = []
#     str = srt
#     lst = list(srt.split(' '))
#     print(lst)
#     for i in str:
#         if i.isdigit():
#             stack.append(i)
#             lst.remove(i)
#         else:
#             cnt1, cnt2 = stack.pop(), stack.pop()
#             stack.append(OPERATORS[i](int(cnt2), int(cnt1)))
#             lst.remove(i)
#     return stack.pop()

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
            value1 = stack.pop()
            stack.append(FUNCTIONS[i](int(value1)))

    return stack.pop()
