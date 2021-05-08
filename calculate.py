import core.polishCalculation as calculation
import core.transformationToPolish as transform

stack = [1, 2, 3]

while stack.pop() != '9':
    print(stack.pop())