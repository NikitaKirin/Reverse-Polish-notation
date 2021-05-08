import math
import operator


def ctg(x):
    return 1 / math.tan(x)


def arcctg(x):
    return 1 / math.atan(x)


OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': math.pow,
             'div': operator.floordiv, '%': operator.mod}

FUNCTIONS = {'cos': math.cos, 'sin': math.sin, 'tg': math.tan, 'arctg': math.atan, 'ctg': ctg,
             'arcctg': arcctg, 'abs': abs, 'sqrt': math.sqrt, 'deg': math.radians}

PRIORITY = {1: ['+', '-', ], 2: ['*', '/', 'div', '%'],
            3: ['sin', 'cos', 'tg', 'artctg', 'ctg', 'arcctg', 'abs', 'sqrt', '^', 'deg']}


def set_priority(value: str) -> int:
    for k, v in PRIORITY.items():
        if value in v:
            return k
    return -1


def transform_to_polish(str):
    stack_of_operations = []
    result_string = ''
    current_string = str.split(' ')
    for i in current_string:
        if i == ' ':
            continue
        if i.isdigit():  # Если символ - число, то добавляем его к выходной строке
            result_string += ' '
            result_string += i
        if i == '(':
            stack_of_operations.append(i)
        # Если символ - закрывающаяся скобка, то смотрим стек операций и добавляем в выходную строку все операции,
        # пока не дойдём до открывающей скобки
        if i == ')':
            current_element = stack_of_operations.pop()
            while current_element != '(':
                result_string += ' '
                result_string += current_element
                current_element = stack_of_operations.pop()
        if i in OPERATORS.keys():
            if len(stack_of_operations) != 0:
                last_operation = stack_of_operations.pop()
                if set_priority(last_operation) <= set_priority(i):
                    stack_of_operations.append(last_operation)
                    stack_of_operations.append(i)
                else:
                    while set_priority(last_operation) > set_priority(i):
                        result_string += ' '
                        result_string += last_operation
                        if len(stack_of_operations) != 0:
                            last_operation = stack_of_operations.pop()
                        else:
                            break
                    stack_of_operations.append(i)
            else:
                stack_of_operations.append(i)
        if i in FUNCTIONS.keys():
            stack_of_operations.append(i)
    for h in reversed(stack_of_operations):
        result_string += ' '
        result_string += h
    return result_string.strip()  # Удаление пробельных символов в начале и конце строки
