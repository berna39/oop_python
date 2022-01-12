class Calculator:
    def __init__(self, number_one, number_two, operand):
        pass
    def addition(first_number, second_number): #for addition operation
        return first_number + second_number

    def substraction(first_number, second_number):
        return first_number - second_number

    def multiply(first_number, second_number):
        return first_number * second_number

    def divide(first_number, second_number):
        return first_number / second_number

    @classmethod 
    def start(cls):
        first_number = int(input('enter the first number : \n'))
        second_number = int(input('enter the second number : \n'))
        operation = input("choose between these operations : 'add', 'sub', 'mult', 'div', 'exp' :\n")

        if operation == 'add':
            print(cls.addition(first_number, second_number))
        if operation == 'sub':
            print(cls.substraction(first_number, second_number))
        if operation == 'mult':
            print(cls.multiply(first_number, second_number))
        if operation == 'div':
            print(cls.divide(first_number, second_number))


Calculator.start()