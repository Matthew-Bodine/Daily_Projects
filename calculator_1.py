import math
history = []

while True:
    print('\n=== Scientific Calculator ===')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide') 
    print('5. Power')
    print('6. Square Root')
    print('7. Sin')
    print('8. Cos')
    print('9. Tan')
    print('10. View History')
    print('11. Clear History')
    print('12. Exit')

    choice = input('Select an operation (1-12): ')

    if choice == '12':
        break

    elif choice == '1':
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        result = num1 + num2
        print(f'The result is: {result}')
        history.append(f'{num1} + {num2} = {result}')

    elif choice =='2':
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        result = num1 - num2
        print(f'The result is: {result}')
        history.append(f'{num1} - {num2} = {result}')

    elif choice == '3': 
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        result = num1 * num2
        print(f'The result is: {result}')
        history.append(f'{num1} * {num2} = {result}')

    elif choice == '4':
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        if num2 != 0:
            result = num1 / num2
            print(f'The result is: {result}')
            history.append(f'{num1} / {num2} = {result}')
        else:
            print('Error: Division by zero is not allowed.')
            
    elif choice == '5':
        num1 = float(input('Enter base number: '))
        num2 = float(input('Enter exponent: '))
        result = num1 ** num2
        print(f'The result is: {result}')
        history.append(f'{num1} ^ {num2} = {result}')

    elif choice == '6':
        num = float(input('Enter a number: '))
        if num >= 0:
            result = math.sqrt(num)
            print(f'The result is: {result}')
            history.append(f'sqrt({num}) = {result}')
    
    elif choice == '7':
        angle = float(input('Enter angle in degrees: '))
        result = math.sin(math.radians(angle))
        print(f'The result is: {result}')
        history.append(f'sin({angle}) = {result}')

    elif choice == '8':
        angle = float(input('Enter angle in degrees: '))
        result = math.cos(math.radians(angle))
        print(f'The result is: {result}')
        history.append(f'cos({angle}) = {result}')

    elif choice == '9':
        angle = float(input('Enter angle in degrees: '))
        result = math.tan(math.radians(angle))
        print(f'The result is: {result}')
        history.append(f'tan({angle}) = {result}')

    elif choice == '10':
        print('\n=== Calculation History ===')
        for entry in history:
            print(entry)

    elif choice == '11':
        history.clear()
        print('History cleared.')

    else:
        print('Invalid Choice. Please select a valid option: ')