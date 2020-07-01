try: 
    x = int(input('enter first number here: '))
    y = int(input('enter second number here: '))
    operators = ['+','-','*', '/']
    operator = input(f'Do you want to add, multiply, subtract or divide these numbers? use {operators}')
    def add(x, y):
        result = x + y
        return result
    def subtract(x, y):
        result = x - y
        return result
    def multiply(x, y):
        result = x * y
        return result
    def divide(x, y):
        result = x / y
        return result
    
    if operator == operators[0]:
        print(add(x,y))
    elif operator == operators[1]:
        print(subtract(x,y))
    elif operator == operators[2]:
        print(multiply(x, y))
    elif operator == operators[3]:
        print(divide(x, y))
    else:
        print('idk')
except ValueError:
    print('enter number please')
