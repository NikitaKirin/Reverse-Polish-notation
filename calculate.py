import core.polishCalculation as calc
import core.transformationToPolish as transform


def get_polish_notation(command):
    if command == '1':
        print('*** Выбран способ введения уравнения с переменной *** \n')
        expression = input("Введите уравнение строго по образцу: 'A + B * cos ( 40 )' \n")
        result = transform.transform_to_polish(expression)
        print("Преобразование в польскую запись: " + result + '\n')
        variable = input('Введите значение переменной:')
        result_polish_notation = change_sym(result, 'X', variable)
        answer = calc.calculate_polish(result_polish_notation)
        print("Ответ: " + str(answer))

    if command == '2':
        print('*** Выбран способ введения уравнения без переменных *** \n')
        expression = input("Введите уравнение строго по образцу: 'A + B * cos ( 40 )' \n")
        result = transform.transform_to_polish(expression)
        print("Преобразование в польскую запись: " + result + '\n')
        answer = calc.calculate_polish(result)
        print("Ответ: " + str(answer))


def change_sym(ch, ca1, ca2):
    b = ''
    for x in ch:
        if x != ca1:
            b += x
        else:
            b += ca2
    return b


inpt = input("Выберите одну из возможных команд: \n "
             "'уравнение с переменной' - 1 \n "
             "'уравнение без перемменной' - 2 \n")

get_polish_notation(inpt)
