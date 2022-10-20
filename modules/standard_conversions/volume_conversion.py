"""Converts volume units to other volume units."""
def volume_conversion():
    """Volume Conversion Function"""
    print("\033[H\033[J", end="")
    print('Select a base unit: ')
    print('1. Liter (L)')
    print('2. Milliliter (mL)')
    print('3. Microliter (uL)')
    print('4. Cubic Centimeter (cm^3)')
    print('5. Cubic Meter (m^3)')
    print('6. Back')
    choice = input('Enter your choice: ')
    if choice == '1':
        base_unit = 'L'
    elif choice == '2':
        base_unit = 'mL'
    elif choice == '3':
        base_unit = 'uL'
    elif choice == '4':
        base_unit = 'cm^3'
    elif choice == '5':
        base_unit = 'm^3'
    elif choice == '6':
        return
    else:
        print('Invalid choice')
        volume_conversion()
    while True:
        try:
            inp = input('Enter a value in ' + base_unit + ': ')
            if '*10^' in inp:
                value = float(inp.split('*10^')[0]) * 10 ** float(inp.split('*10^')[1])
            else:
                value = float(inp)
            break
        except ValueError:
            print('Invalid input')
    print("\033[H\033[J", end="")
    print('Select a target unit: ')
    print('1. Liter (L)')
    print('2. Milliliter (mL)')
    print('3. Microliter (uL)')
    print('4. Cubic Centimeter (cm^3)')
    print('5. Cubic Meter (m^3)')
    print('6. Back')
    choice = input('Enter your choice: ')
    if choice == '1':
        target_unit = 'L'
    elif choice == '2':
        target_unit = 'mL'
    elif choice == '3':
        target_unit = 'uL'
    elif choice == '4':
        target_unit = 'cm^3'
    elif choice == '5':
        target_unit = 'm^3'
    elif choice == '6':
        volume_conversion()
    else:
        print('Invalid choice')
        volume_conversion()
    
    if base_unit == 'L':
        if target_unit == 'L':
            result = value
        elif target_unit == 'mL':
            result = value * 1000
        elif target_unit == 'uL':
            result = value * 1000000
        elif target_unit == 'cm^3':
            result = value * 1000
        elif target_unit == 'm^3':
            result = value / 1000
    elif base_unit == 'mL':
        if target_unit == 'L':
            result = value / 1000
        elif target_unit == 'mL':
            result = value
        elif target_unit == 'uL':
            result = value * 1000
        elif target_unit == 'cm^3':
            result = value
        elif target_unit == 'm^3':
            result = value / 1000000
    elif base_unit == 'uL':
        if target_unit == 'L':
            result = value / 1000000
        elif target_unit == 'mL':
            result = value / 1000
        elif target_unit == 'uL':
            result = value
        elif target_unit == 'cm^3':
            result = value / 1000
        elif target_unit == 'm^3':
            result = value / 1000000000
    elif base_unit == 'cm^3':
        if target_unit == 'L':
            result = value / 1000
        elif target_unit == 'mL':
            result = value
        elif target_unit == 'uL':
            result = value * 1000
        elif target_unit == 'cm^3':
            result = value
        elif target_unit == 'm^3':
            result = value / 1000000
    elif base_unit == 'm^3':
        if target_unit == 'L':
            result = value * 1000
        elif target_unit == 'mL':
            result = value * 1000000
        elif target_unit == 'uL':
            result = value * 1000000000
        elif target_unit == 'cm^3':
            result = value * 1000000
        elif target_unit == 'm^3':
            result = value

    if len(str(value)) > 8:
        print_dict_value = f'{value:.6e}'
    else:
        print_dict_value = str(value)

    if base_unit == target_unit:
        print(f'{print_dict_value} {base_unit} = {result} {target_unit}')
        input('Press enter to continue...')
        return

    print_dict = {}
    if base_unit == 'L':
        if target_unit == 'm^3':
            print_dict[1] = [f'{print_dict_value} L', '1 L']
            print_dict[2] = ['', '1000 m^3']
        if target_unit == 'cm^3':
            print_dict[1] = [f'{print_dict_value} L', '1 L']
            print_dict[2] = ['', '0.001 cm^3']
        if target_unit == 'uL':
            print_dict[1] = [f'{print_dict_value} L', '1 L']
            print_dict[2] = ['', '1000000 uL']
        if target_unit == 'mL':
            print_dict[1] = [f'{print_dict_value} L', '1 L']
            print_dict[2] = ['', '1000 mL']
    elif base_unit == 'm^3':
        if target_unit == 'L':
            print_dict[1] = [f'{print_dict_value} m^3', '1 m^3']
            print_dict[2] = ['', '0.001 L']
        if target_unit == 'cm^3':
            print_dict[1] = [f'{print_dict_value} m^3', '1 m^3']
            print_dict[2] = ['', '1000000 cm^3']
        if target_unit == 'uL':
            print_dict[1] = [f'{print_dict_value} m^3', '1 m^3']
            print_dict[2] = ['', '1000000000000 uL']
        if target_unit == 'mL':
            print_dict[1] = [f'{print_dict_value} m^3', '1 m^3']
            print_dict[2] = ['', '1000000 mL']
    elif base_unit == 'cm^3':
        if target_unit == 'L':
            print_dict[1] = [f'{print_dict_value} cm^3', '1 cm^3']
            print_dict[2] = ['', '0.001 L']
        if target_unit == 'm^3':
            print_dict[1] = [f'{print_dict_value} cm^3', '1 cm^3']
            print_dict[2] = ['', '0.000001 m^3']
        if target_unit == 'uL':
            print_dict[1] = [f'{print_dict_value} cm^3', '1 cm^3']
            print_dict[2] = ['', '1000 uL']
        if target_unit == 'mL':
            print_dict[1] = [f'{print_dict_value} cm^3', '1 cm^3']
            print_dict[2] = ['', '1 mL']
    elif base_unit == 'uL':
        if target_unit == 'L':
            print_dict[1] = [f'{print_dict_value} uL', '1 uL']
            print_dict[2] = ['', '0.000001 L']
        if target_unit == 'm^3':
            print_dict[1] = [f'{print_dict_value} uL', '1 uL']
            print_dict[2] = ['', '0.000000000001 m^3']
        if target_unit == 'cm^3':
            print_dict[1] = [f'{print_dict_value} uL', '1 uL']
            print_dict[2] = ['', '0.001 cm^3']
        if target_unit == 'mL':
            print_dict[1] = [f'{print_dict_value} uL', '1 uL']
            print_dict[2] = ['', '0.001 mL']
    elif base_unit == 'mL':
        if target_unit == 'L':
            print_dict[1] = [f'{print_dict_value} mL', '1 mL']
            print_dict[2] = ['', '0.001 L']
        if target_unit == 'm^3':
            print_dict[1] = [f'{print_dict_value} mL', '1 mL']
            print_dict[2] = ['', '0.000001 m^3']
        if target_unit == 'cm^3':
            print_dict[1] = [f'{print_dict_value} mL', '1 mL']
            print_dict[2] = ['', '1 cm^3']
        if target_unit == 'uL':
            print_dict[1] = [f'{print_dict_value} mL', '1 mL']
            print_dict[2] = ['', '1000 uL']

    print("\033[H\033[J", end="")
    print('Table Setup:')
    mx_length_per_column = {}
    for key in print_dict:
        for data in print_dict[key]:
            if print_dict[key].index(data) not in mx_length_per_column:
                mx_length_per_column[print_dict[key].index(data)] = len(data)
            elif len(data)>mx_length_per_column[print_dict[key].index(data)]:
                mx_length_per_column[print_dict[key].index(data)] = len(data)


    column_wise_width = mx_length_per_column
    for key in print_dict:
        line = ''
        for data in print_dict[key]:
            temp_variable = data
            if len(temp_variable)<column_wise_width[print_dict[key].index(data)]:
                temp_variable = data + ' '*(column_wise_width[print_dict[key].index(data)] - len(temp_variable))
            else:
                temp_variable = data
            line += '| '+ temp_variable+' '
        line = line.lstrip()+'|'
        print(line)

    ans = result
    print(f'\nFinal Answer: {str(ans)} {target_unit}')
    print(f'Final Answer (sci notation): {ans:.6e} {target_unit}')

    print(f'Remember to adjust for sigfigs, your input was {inp} {base_unit}.')
    input('Press enter to continue...')
    return
