"""Converts particles to moles."""
def particles_to_moles():
    """Particles to Moles Function"""
    from ..compounds_to_elements import compounds_to_elements as cte
    print("\033[H\033[J", end="")
    print('Particles to Moles')
    compound = input('Enter the compound: ')
    while True:
        try:
            inp = input('Enter the particles (par): ')
            if '*10^' in inp:
                particles = float(inp.split('*10^')[0]) * 10 ** float(inp.split('*10^')[1])
            else:
                particles = float(inp)
            break
        except ValueError:
            print('Invalid input')

    if len(str(particles)) > 6:
        print_dict_particles = f'{particles:.6e}'
    else:
        print_dict_particles = str(particles)

    print_dict = {}
    print_dict[1] = [f'{str(print_dict_particles)} par {str(compound)}', f'1 mol {str(compound)}']
    print_dict[2] = ['', f'6.022*10^23 par {str(compound)}']
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

    print(f'\nFinal Answer: {str(particles / (6.022 * 10 ** 23))} mol {compound}')
    print(f'Final Answer (sci notation): {particles / (6.022 * 10 ** 23):.7e} mol {compound}')

    print(f'Remember to adjust for sigfigs, your input was {inp} particles of {compound}')
    input('Press enter to continue...')
    return
