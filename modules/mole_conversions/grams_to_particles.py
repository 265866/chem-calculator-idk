"""Converts grams to particles."""
def grams_to_particles():
    """Grams to particles function"""

    from ..compounds_to_elements import compounds_to_elements as cte
    print("\033[H\033[J", end="")
    print('Particles to Grams')
    compound = input('Enter the compound: ')
    while True:
        try:
            inp = input('Enter the mass (g): ')
            if '*10^' in inp:
                grams = float(inp.split('*10^')[0]) * 10 ** float(inp.split('*10^')[1])
            else:
                grams = float(inp)
            break
        except ValueError:
            print('Invalid input')

    compound_dict = cte(compound)
    if compound_dict == -1:
        input('Invalid compound, press enter to continue')
        return

    periodic_table = {
        'H': 1.0079,
        'He': 4.0026,
        'Li': 6.941,
        'Be': 9.0122,
        'B': 10.811,
        'C': 12.0107,
        'N': 14.0067,
        'O': 15.9994,
        'F': 18.9984,
        'Ne': 20.1797,
        'Na': 22.9897,
        'Mg': 24.305,
        'Al': 26.9815,
        'Si': 28.0855,
        'P': 30.9738,
        'S': 32.065,
        'Cl': 35.453,
        'Ar': 39.948,
        'K': 39.0983,
        'Ca': 40.078,
        'Sc': 44.9559,
        'Ti': 47.867,
        'V': 50.9415,
        'Cr': 51.9961,
        'Mn': 54.938,
        'Fe': 55.845,
        'Co': 58.9332,
        'Ni': 58.6934,
        'Cu': 63.546,
        'Zn': 65.39,
        'Ga': 69.723,
        'Ge': 72.64,
        'As': 74.9216,
        'Se': 78.96,
        'Br': 79.904,
        'Kr': 83.8,
        'Rb': 85.4678,
        'Sr': 87.62,
        'Y': 88.9059,
        'Zr': 91.224,
        'Nb': 92.9064,
        'Mo': 95.94,
        'Tc': 98,
        'Ru': 101.07,
        'Rh': 102.9055,
        'Pd': 106.42,
        'Ag': 107.8682,
        'Cd': 112.411,
        'In': 114.818,
        'Sn': 118.71,
        'Sb': 121.76,
        'Te': 127.6,
        'I': 126.9045,
        'Xe': 131.293,
        'Cs': 132.9055,
        'Ba': 137.327,
        'La': 138.9055,
        'Ce': 140.116,
        'Pr': 140.9077,
        'Nd': 144.24,
        'Pm': 145,
        'Sm': 150.36,
        'Eu': 151.964,
        'Gd': 157.25,
        'Tb': 158.9253,
        'Dy': 162.5,
        'Ho': 164.9303,
        'Er': 167.259,
        'Tm': 168.9342,
        'Yb': 173.04,
        'Lu': 174.967,
        'Hf': 178.49,
        'Ta': 180.9479,
        'W': 183.84,
        'Re': 186.207,
        'Os': 190.23,
        'Ir': 192.217,
        'Pt': 195.078,
        'Au': 196.9665,
        'Hg': 200.59,
        'Tl': 204.3833,
        'Pb': 207.2,
        'Bi': 208.9804,
        'Po': 209,
        'At': 210,
        'Rn': 222,
        'Fr': 223,
        'Ra': 226,
        'Ac': 227,
        'Th': 232.0381,
        'Pa': 231.0359,
        'U': 238.0289,
        'Np': 237,
        'Pu': 244,
        'Am': 243,
        'Cm': 247,
        'Bk': 247,
        'Cf': 251,
        'Es': 252,
        'Fm': 257,
        'Md': 258,
        'No': 259,
        'Lr': 262,
        'Rf': 261,
        'Db': 262,
        'Sg': 266,
        'Bh': 264,
        'Hs': 277,
        'Mt': 268,
        'Ds': 281,
        'Rg': 272,
        'Cn': 285,
        'Nh': 284,
        'Fl': 289,
        'Mc': 288,
        'Lv': 293,
        'Ts': 294,
        'Og': 294
    }

    molar_mass = 0
    for element in compound_dict:
        molar_mass += compound_dict[element] * periodic_table[element]

    print("\033[H\033[J", end="")
    print('Molar Mass Equation Setup:')

    for element in compound_dict:
        print(f'{str(element)}: {str(compound_dict[element])} * {str(periodic_table[element])} = {str(compound_dict[element] * periodic_table[element])}')
    print(f'Molar Mass: {str(molar_mass)}\n')

    if len(str(grams)) > 6:
        print_dict_grams = f'{grams:.6e}'
    else:
        print_dict_grams = str(grams)

    print_dict = {}
    print_dict[1] = [f'{print_dict_grams} g {compound}', f'1 mol {compound}', f'6.022*10^23 par {compound}']
    print_dict[2] = ['', f'{molar_mass} g {compound}', f'1 mol {compound}']
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

    ans = grams / molar_mass * 6.022 * 10**23
    print(f'\nFinal Answer: {str(ans)} g {compound}')
    print(f'Final Answer (sci notation): {ans:.6e} g {compound}')

    print(f'Remember to adjust for sigfigs, your input was {inp} particles of {compound}')
    input('Press enter to continue...')
    return