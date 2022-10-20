"""Converts temperature units to other temperature units."""
def temperature_conversion():
    """Temperature Conversion Function"""
    print("\033[H\033[J", end="")
    print('Select a base unit: ')
    print('1. Celsius')
    print('2. Fahrenheit')
    print('3. Kelvin')
    print('4. Back')
    choice = input('Enter your choice: ')
    if choice == '1':
        base_unit = 'C'
    elif choice == '2':
        base_unit = 'F'
    elif choice == '3':
        base_unit = 'K'
    elif choice == '4':
        return
    else:
        print('Invalid choice')
        temperature_conversion()
    while True:
        try:
            value = float(input('Enter a value in ' + base_unit + ': '))
            break
        except ValueError:
            print('Invalid input')
    print("\033[H\033[J", end="")
    print('Select a target unit: ')
    print('1. Celsius')
    print('2. Fahrenheit')
    print('3. Kelvin')
    print('4. Back')
    choice = input('Enter your choice: ')
    if choice == '1':
        target_unit = 'C'
    elif choice == '2':
        target_unit = 'F'
    elif choice == '3':
        target_unit = 'K'
    elif choice == '4':
        temperature_conversion()
    else:
        print('Invalid choice')
        temperature_conversion()

    #if base unit is not C, convert to C
    if base_unit != 'C':
        if base_unit == 'F':
            in_c = (value - 32) * (5 / 9)
        elif base_unit == 'K':
            in_c = value - 273.15
    else:
        in_c = value

    print("\033[H\033[J", end="")
    print('Final Answer: ')
    #print final conversion
    if target_unit == 'C':
        print(f'{in_c} {target_unit}')
    elif target_unit == 'F':
        print(f'{in_c * (9 / 5) + 32} {target_unit}')
    elif target_unit == 'K':
        print(f'{in_c + 273.15} {target_unit}')

    #print final conversion in scientific notation
    if target_unit == 'C':
        print(f'{in_c:.6e} {target_unit}')
    elif target_unit == 'F':
        print(f'{in_c * (9 / 5) + 32:.6e} {target_unit}')
    elif target_unit == 'K':
        print(f'{in_c + 273.15:.6e} {target_unit}')

    print(f'Remember to adjust for sigfigs, your input was {value} {base_unit}')
    input('Press enter to continue...')
    return
