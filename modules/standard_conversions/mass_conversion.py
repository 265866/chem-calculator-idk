"""Converts mass units to other mass units."""
def mass_conversion():
    """Mass Conversion Function"""
    print("\033[H\033[J", end="")
    print('Select a base unit: ')
    print('1. Kilogram (kg)')
    print('2. Gram (g)')
    print('3. Milligram (mg)')
    print('4. Microgram (ug)')
    print('5. Pound (lb)')
    print('6. Ounce (oz)')
    print('7. Back')
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
        base_unit = 'lb'
    elif choice == '6':
        base_unit = 'oz'
    elif choice == '7':
        return
    else:
        print('Invalid choice')
        mass_conversion()
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
    print('1. Kilogram (kg)')
    print('2. Gram (g)')
    print('3. Milligram (mg)')
    print('4. Microgram (ug)')
    print('5. Pound (lb)')
    print('6. Ounce (oz)')
    print('7. Back')
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
        target_unit = 'lb'
    elif choice == '6':
        target_unit = 'oz'
    elif choice == '7':
        mass_conversion()
    else:
        print('Invalid choice')
        mass_conversion()

    if base_unit == 'kg':
        if target_unit == 'kg':
            result = value
        elif target_unit == 'g':
            result = value * 1000
        elif target_unit == 'mg':
            result = value * 1000000
        elif target_unit == 'ug':
            result = value * 1000000000
        elif target_unit == 'lb':
            result = value * 2.20462
        elif target_unit == 'oz':
            result = value * 35.274
    elif base_unit == 'g':
        if target_unit == 'kg':
            result = value / 1000
        elif target_unit == 'g':
            result = value
        elif target_unit == 'mg':
            result = value * 1000
        elif target_unit == 'ug':
            result = value * 1000000
        elif target_unit == 'lb':
            result = value / 453.592
        elif target_unit == 'oz':
            result = value / 28.3495
    elif base_unit == 'mg':
        if target_unit == 'kg':
            result = value / 1000000
        elif target_unit == 'g':
            result = value / 1000
        elif target_unit == 'mg':
            result = value
        elif target_unit == 'ug':
            result = value * 1000
        elif target_unit == 'lb':
            result = value / 453592
        elif target_unit == 'oz':
            result = value / 28349.5
    elif base_unit == 'ug':
        if target_unit == 'kg':
            result = value / 1000000000
        elif target_unit == 'g':
            result = value / 1000000
        elif target_unit == 'mg':
            result = value / 1000
        elif target_unit == 'ug':
            result = value
        elif target_unit == 'lb':
            result = value / 453592000
        elif target_unit == 'oz':
            result = value / 28349500
    elif base_unit == 'lb':
        if target_unit == 'kg':
            result = value / 2.20462
        elif target_unit == 'g':
            result = value * 453.592
        elif target_unit == 'mg':
            result = value * 453592
        elif target_unit == 'ug':
            result = value * 453592000
        elif target_unit == 'lb':
            result = value
        elif target_unit == 'oz':
            result = value * 16
    elif base_unit == 'oz':
        if target_unit == 'kg':
            result = value / 35.274
        elif target_unit == 'g':
            result = value * 28.3495
        elif target_unit == 'mg':
            result = value * 28349.5
        elif target_unit == 'ug':
            result = value * 28349500
        elif target_unit == 'lb':
            result = value / 16
        elif target_unit == 'oz':
            result = value

    if len(str(value)) > 8:
        print_dict_value = f'{value:.8e}'
    else:
        print_dict_value = value

    if base_unit == target_unit:
        print(f'{print_dict_value} {base_unit} = {result} {target_unit}')
        input('Press enter to continue')
        return
    
    print_dict = {}
    if base_unit == 'kg':
        if target_unit == 'g':
            print_dict[1] = [f'{print_dict_value} kg', '1000 g']
            print_dict[2] = ['', '1 kg']
        elif target_unit == 'mg':
            print_dict[1] = [f'{print_dict_value} kg', '1000000 mg']
            print_dict[2] = ['', '1 kg']
        elif target_unit == 'ug':
            print_dict[1] = [f'{print_dict_value} kg', '1000000000 ug']
            print_dict[2] = ['', '1 kg']
        elif target_unit == 'lb':
            print_dict[1] = [f'{print_dict_value} kg', '2.20462 lb']
            print_dict[2] = ['', '1 kg']
        elif target_unit == 'oz':
            print_dict[1] = [f'{print_dict_value} kg', '35.274 oz']
            print_dict[2] = ['', '1 kg']
    elif base_unit == 'g':
        if target_unit == 'kg':
            print_dict[1] = [f'{print_dict_value} g', '1 kg']
            print_dict[2] = ['', '1000 g']
        elif target_unit == 'mg':
            print_dict[1] = [f'{print_dict_value} g', '1000 mg']
            print_dict[2] = ['', '1 g']
        elif target_unit == 'ug':
            print_dict[1] = [f'{print_dict_value} g', '1000000 ug']
            print_dict[2] = ['', '1 g']
        elif target_unit == 'lb':
            print_dict[1] = [f'{print_dict_value} g', '0.00220462 lb']
            print_dict[2] = ['', '1 g']
        elif target_unit == 'oz':
            print_dict[1] = [f'{print_dict_value} g', '0.035274 oz']
            print_dict[2] = ['', '1 g']
    elif base_unit == 'mg':
        if target_unit == 'kg':
            print_dict[1] = [f'{print_dict_value} mg', '1 kg']
            print_dict[2] = ['', '1000000 mg']
        elif target_unit == 'g':
            print_dict[1] = [f'{print_dict_value} mg', '1 g']
            print_dict[2] = ['', '1000 mg']
        elif target_unit == 'ug':
            print_dict[1] = [f'{print_dict_value} mg', '1000 ug']
            print_dict[2] = ['', '1 mg']
        elif target_unit == 'lb':
            print_dict[1] = [f'{print_dict_value} mg', '0.00000220462 lb']
            print_dict[2] = ['', '1 mg']
        elif target_unit == 'oz':
            print_dict[1] = [f'{print_dict_value} mg', '0.000035274 oz']
            print_dict[2] = ['', '1 mg']
    elif base_unit == 'ug':
        if target_unit == 'kg':
            print_dict[1] = [f'{print_dict_value} ug', '1 kg']
            print_dict[2] = ['', '1000000000 ug']
        elif target_unit == 'g':
            print_dict[1] = [f'{print_dict_value} ug', '1 g']
            print_dict[2] = ['', '1000000 ug']
        elif target_unit == 'mg':
            print_dict[1] = [f'{print_dict_value} ug', '1 mg']
            print_dict[2] = ['', '1000 ug']
        elif target_unit == 'lb':
            print_dict[1] = [f'{print_dict_value} ug', '0.00000000220462 lb']
            print_dict[2] = ['', '1 ug']
        elif target_unit == 'oz':
            print_dict[1] = [f'{print_dict_value} ug', '0.000000035274 oz']
            print_dict[2] = ['', '1 ug']
    elif base_unit == 'lb':
        if target_unit == 'kg':
            print_dict[1] = [f'{print_dict_value} lb', '1 kg']
            print_dict[2] = ['', '2.20462 lb']
        elif target_unit == 'g':
            print_dict[1] = [f'{print_dict_value} lb', '453.592 g']
            print_dict[2] = ['', '1 lb']
        elif target_unit == 'mg':
            print_dict[1] = [f'{print_dict_value} lb', '453592 mg']
            print_dict[2] = ['', '1 lb']
        elif target_unit == 'ug':
            print_dict[1] = [f'{print_dict_value} lb', '453592000 ug']
            print_dict[2] = ['', '1 lb']
        elif target_unit == 'oz':
            print_dict[1] = [f'{print_dict_value} lb', '16 oz']
            print_dict[2] = ['', '1 lb']
    elif base_unit == 'oz':
        if target_unit == 'kg':
            print_dict[1] = [f'{print_dict_value} oz', '1 kg']
            print_dict[2] = ['', '35.274 oz']
        elif target_unit == 'g':
            print_dict[1] = [f'{print_dict_value} oz', '28.3495 g']
            print_dict[2] = ['', '1 oz']
        elif target_unit == 'mg':
            print_dict[1] = [f'{print_dict_value} oz', '28349.5 mg']
            print_dict[2] = ['', '1 oz']
        elif target_unit == 'ug':
            print_dict[1] = [f'{print_dict_value} oz', '28349500 ug']
            print_dict[2] = ['', '1 oz']
        elif target_unit == 'lb':
            print_dict[1] = [f'{print_dict_value} oz', '1 lb']
            print_dict[2] = ['', '16 oz']

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
    