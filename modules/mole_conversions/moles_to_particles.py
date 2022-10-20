"""Converts moles to particles."""
def moles_to_particles():
    """Moles to Particles Function"""
    from ..compounds_to_elements import compounds_to_elements as cte
    print("\033[H\033[J", end="")
    print('Moles to particles')
    compound = input('Enter the compound: ')
    while True:
        try:
            inp = input('Enter the moles (mol): ')
            if '*10^' in inp:
                moles = float(inp.split('*10^')[0]) * 10 ** float(inp.split('*10^')[1])
            else:
                moles = float(inp)
            break
        except ValueError:
            print('Invalid input')

    if len(str(moles)) > 6:
        print_dict_moles = f'{moles:.6e}'
    else:
        print_dict_moles = str(moles)

    print_dict = {}
    print_dict[1] = [f'{str(print_dict_moles)} mol {str(compound)}', f'6.022*10^23 par {str(compound)}']
    print_dict[2] = ['', f'1 mol {str(compound)}']
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

    print(f'\nFinal Answer: {str(moles * 6.022 * 10 ** 23)} particles {compound}')
    print(f'Final Answer (sci notation): {moles * 6.022 * 10 ** 23:.7e} particles {compound}')

    print(f'Remember to adjust for sigfigs, your input was {inp} mol of {compound}')
    input('Press enter to continue...')
    return
    