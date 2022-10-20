"""Converts mass units to other mass units."""
def mass_conversion():
    """Mass Conversion Function"""
    print("\033[H\033[J", end="")
    print('Select a base unit: ')
    print('1. Kilogram (kg)')
    print('2. Gram (g)')
    print('3. Milligram (mg)')
    print('4. Microgram (ug)')
    print('5. Back')
    choice = input('Enter your choice: ')
    if choice == '1':
        base_unit = 'kg'
    elif choice == '2':
        base_unit = 'g'
    elif choice == '3':
        base_unit = 'mg'
    elif choice == '4':
        base_unit = 'ug'
    elif choice == '5':
        return
    else:
        print('Invalid choice')
        mass_conversion()
    while True:
        try:
            value = float(input('Enter a value in ' + base_unit + ': '))
            break
        except ValueError:
            print('Invalid input')
    print("\033[H\033[J", end="")
    print('Select a target unit: ')
    print('1. Kilogram (kg)')
    print('2. Gram (g)')
    print('3. Milligram (mg)')
    print('4. Microgram (ug)')
    print('5. Back')
    choice = input('Enter your choice: ')
    if choice == '1':
        target_unit = 'kg'
    elif choice == '2':
        target_unit = 'g'
    elif choice == '3':
        target_unit = 'mg'
    elif choice == '4':
        target_unit = 'ug'
    elif choice == '5':
        mass_conversion()
    else:
        print('Invalid choice')
        mass_conversion()

    #if base unit is not kg, convert to kg
    if base_unit != 'kg':
        if base_unit == 'g':
            in_kg = value / 1000
        elif base_unit == 'mg':
            in_kg = value / 1000000
        elif base_unit == 'ug':
            in_kg = value / 1000000000
    else:
        in_kg = value

    print_dict = {
        1: [f'{value} {base_unit}', '1 kg'],
    }
    if target_unit != 'kg':
        if target_unit == 'g':
            print_dict[1] = [f'{value} {base_unit}', '1 kg', f'1000 {target_unit}']
            print_dict[2] = [' ' * len(f'{value} {base_unit}'), f'1000 {base_unit}', '1 kg']

        if target_unit == 'mg':
            print_dict[1] = [f'{value} {base_unit}', '1 kg', f'1000000 {target_unit}']
            print_dict[2] = [' ' * len(f'{value} {base_unit}'), f'1000000 {base_unit}', '1 kg']

        if target_unit == 'ug':
            print_dict[1] = [f'{value} {base_unit}', '1 kg', f'1000000000 {target_unit}']
            print_dict[2] = [' ' * len(f'{value} {base_unit}'), f'1000000000 {base_unit}', '1 kg']
    if target_unit == 'kg':
        if base_unit == 'g':
            print_dict[1] = [f'{value} {base_unit}', '1 kg']
            print_dict[2] = [' ' * len(f'{value} {base_unit}'), f'1000 {base_unit}']
        if base_unit == 'mg':
            print_dict[1] = [f'{value} {base_unit}', '1 kg']
            print_dict[2] = [' ' * len(f'{value} {base_unit}'), f'1000000 {base_unit}']
        if base_unit == 'ug':
            print_dict[1] = [f'{value} {base_unit}', '1 kg']
            print_dict[2] = [' ' * len(f'{value} {base_unit}'), f'1000000000 {base_unit}']

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
    print('Final Answer: ')
    if target_unit == 'kg':
        print(f'{in_kg} {target_unit}')
    elif target_unit == 'g':
        print(f'{in_kg * 1000} {target_unit}')
    elif target_unit == 'mg':
        print(f'{in_kg * 1000000} {target_unit}')
    elif target_unit == 'ug':
        print(f'{in_kg * 1000000000} {target_unit}')

    #print final conversion in scientific notation
    if target_unit == 'kg':
        print(f'{in_kg:.6e} {target_unit}')
    elif target_unit == 'g':
        print(f'{in_kg * 1000:.6e} {target_unit}')
    elif target_unit == 'mg':
        print(f'{in_kg * 1000000:.6e} {target_unit}')
    elif target_unit == 'ug':
        print(f'{in_kg * 1000000000:.6e} {target_unit}')

    print(f'Remember to adjust for sigfigs, your input was {value} {base_unit}')
    input('Press enter to continue...')
    return
