history = {}

result = 0

iterations = 0 

print("======================= Calculator =======================")

while True:
    print('Please insert first number:')
    a = float(input('> '))
    print('Choose the operation you desire to compute:')
    print('You may choose: +, -, *, /. Any other operation will result in an error')
    operation = input('> ')
    print('Please insert second number:')
    b = float(input('> '))

    var = f"{a} {operation} {b}"

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b != 0:
         result = a / b
        else: print("MathError")
    else: print("TypeError")

    print(f"Result = {result}")

    iterations +=1

    history[var] = result

    print('Other operations needed?')
    print('Type \'Yes\' if indeed needed')
    print('Type \'No\' if not needed')



    loop = input('> ')

    if loop.lower() == 'yes':
        print('Would you like to see your history?')
        print('Type \'Yes\' if indeed needed')
        print('Type \'No\' if not needed')
        history_needed = input('> ')
        if history_needed.lower() == 'yes':
                for operation, result in history.items():
                 print(f"{operation} = {result}")


        else:
                continue
        continue
    elif loop.lower() == 'no':
         print('Would you like to see your history?')
         print('Type \'Yes\' if indeed needed')
         print('Type \'No\' if not needed')
         history_needed = input('> ')
         if history_needed.lower() == 'yes':
            for operation, result in history.items():
                 print(f"{iterations}. {operation} = {result}")

         break
    else: print('TypeError')
