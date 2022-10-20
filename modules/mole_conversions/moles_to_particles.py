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
    for i in range(1, len(print_dict) + 1):
        for j in range(len(print_dict[i])):
            if len(print_dict[i][j]) < len(print_dict[i][j - 1]):
                print_dict[i][j] = (
                    ' ' * (len(print_dict[i][j - 1])
                    - len(print_dict[i][j])) + print_dict[i][j]
                )
            elif len(print_dict[i][j]) > len(print_dict[i][j - 1]):
                print_dict[i][j - 1] = (
                    ' ' * (len(print_dict[i][j])
                    - len(print_dict[i][j - 1])) + print_dict[i][j - 1]
                )

    for _, value in print_dict.items():
        print(' | '.join(value))

    print(f'\nFinal Answer: {str(moles * 6.022 * 10 ** 23)} particles {compound}')
    print(f'Final Answer (sci notation): {moles * 6.022 * 10 ** 23:.7e} particles {compound}')

    print(f'Remember to adjust for sigfigs, your input was {inp} mol of {compound}')
    input('Press enter to continue...')
    return
    