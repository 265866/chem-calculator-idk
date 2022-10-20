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
            value = float(input('Enter a value in ' + base_unit + ': '))
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
    #if base unit is not L, convert to L
    if base_unit != 'L':
        if base_unit == 'mL':
            in_l = value / 1000
        elif base_unit == 'uL':
            in_l = value / 1000000
        elif base_unit == 'cm^3':
            in_l = value / 1000
        elif base_unit == 'm^3':
            in_l = value * 1000
    else:
        in_l = value

    print_dict = {
        1: [f'{value} {base_unit}', '1 L'],
    }
    if target_unit != 'L':
        if target_unit == 'mL':
            print_dict[1] = [f'{value} {base_unit}', '1 L', f'1000 {target_unit}']
            print_dict[2] = [' ' * len(f'{value} {base_unit}'), f'1000 {base_unit}', '1 L']

        if target_unit == 'uL':
            print_dict[1] = [f'{value} {base_unit}', '1 L', f'1000000 {target_unit}']
            print_dict[2] = [' ' * len(f'{value} {base_unit}'), f'1000000 {base_unit}', '1 L']

        if target_unit == 'cm^3':
            print_dict[1] = [f'{value} {base_unit}', '1 L', f'1000 {target_unit}']
            print_dict[2] = [' ' * len(f'{value} {base_unit}'), f'1000 {base_unit}', '1 L']

        if target_unit == 'm^3':
            print_dict[1] = [f'{value} {base_unit}', '1 L', f'0.001 {target_unit}']
            print_dict[2] = [' ' * len(f'{value} {base_unit}'), f'0.001 {base_unit}', '1 L']
    if target_unit == 'L':
        if base_unit == 'mL':
            print_dict[1] = [f'{value} {base_unit}', '1 L']
            print_dict[2] = [' ' * len(f'{value} {base_unit}'), f'1000 {base_unit}']
        if base_unit == 'uL':
            print_dict[1] = [f'{value} {base_unit}', '1 L']
            print_dict[2] = [' ' * len(f'{value} {base_unit}'), f'1000000 {base_unit}']
        if base_unit == 'cm^3':
            print_dict[1] = [f'{value} {base_unit}', '1 L']
            print_dict[2] = [' ' * len(f'{value} {base_unit}'), f'1000 {base_unit}']
        if base_unit == 'm^3':
            print_dict[1] = [f'{value} {base_unit}', '1 L']
            print_dict[2] = [' ' * len(f'{value} {base_unit}'), f'0.001 {base_unit}']

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
    print('\n')
    #print final conversion
    print('Final Answer:')
    if target_unit == 'L':
        print(f'{in_l} {target_unit}')
    elif target_unit == 'mL':
        print(f'{in_l * 1000} {target_unit}')
    elif target_unit == 'uL':
        print(f'{in_l * 1000000} {target_unit}')
    elif target_unit == 'cm^3':
        print(f'{in_l * 1000} {target_unit}')
    elif target_unit == 'm^3':
        print(f'{in_l / 1000} {target_unit}')
    #print final conversion in scientific notation
    if target_unit == 'L':
        print(f'{in_l:.6e} {target_unit}')
    elif target_unit == 'mL':
        print(f'{in_l * 1000:.6e} {target_unit}')
    elif target_unit == 'uL':
        print(f'{in_l * 1000000:.6e} {target_unit}')
    elif target_unit == 'cm^3':
        print(f'{in_l * 1000:.6e} {target_unit}')
    elif target_unit == 'm^3':
        print(f'{in_l / 1000:.6e} {target_unit}')
    print('\n')

    print(f'Remember to adjust for sigfigs, your input was {value} {base_unit}')
    input('Press enter to continue...')
    return
