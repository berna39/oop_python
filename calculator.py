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

    @staticmethod
    def start(self):
        first_number = input('enter the first number : \n')
        second_number = input('enter the second number : \n')
        operation = input("choose between these operations : 'add', 'sub', 'div', 'exp'")

        if operation == 'add':
            print(self.ddition(first_number, second_number))


Calculator.start()