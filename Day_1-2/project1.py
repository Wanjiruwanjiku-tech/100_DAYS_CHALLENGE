def calculator():

    try:
        print("Enter desired numbers in correct order...\n")
        number1 = float(input('Enter the first number:'))
        number2 = float(input('Enter the second number'))
        op = input('Select the operation to perform(+, -, *, /, %, **, //): ')


        if number1 is None or number2 is None or op is None:
            print("Please enter all the values")

        if op == '+':
            print("Your Oprration is Addition")
            print('{} {} {} = {}'.format(number1, op, number2, number1 + number2))

        elif op == '-':
            print("Your Oprration is Subtraction")
            print('{} {} {} = {}'.format(number1, op, number2, number1 - number2))
        
        elif op == '*':
            print("Your Oprration is Multiplication")
            print('{} {} {} = {}'.format(number1, op, number2, number1 * number2))
        
        elif op == '/':
            print("Your Oprration is Division")
            print('{} {} {} = {}'.format(number1, op, number2, number1 / number2))
        
        elif op == '%':
            print("Your Oprration is Modulus")
            print('{} {} {} = {}'.format(number1, op, number2, number1 % number2))

        elif op == '**':
            print("Your Oprration is Exponent")
            print('{} {} {} = {}'.format(number1, op, number2, number1 ** number2))
        
        elif op == '//':
            print("Your Oprration is Floor Division")
            print('{} {} {} = {}'.format(number1, op, number2, number1 // number2))
        
        else:
            print("Invalid Operation")
        
    except ValueError:
        print("Invalid Input")
    
