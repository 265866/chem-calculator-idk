"""Converts length units to other length units"""
def length_conversion():
    """Length Conversion Function"""
    print("\033[H\033[J", end="")
    print('Length Conversion')
    print('1. Kilometer (km)')
    print('2. Meter (m)')
    print('3. Decimeter (dm)')
    print('4. Centimeter (cm)')
    print('5. Millimeter (mm)')
    print('6. Micrometer (um)')
    print('7. Nanometer (nm)')
    print('8. Mile (mi)')
    print('9. Yard (yd)')
    print('10. Foot (ft)')
    print('11. Inch (in)')
    print('12. Back')
    choice = input('Enter your choice: ')
    if choice == '1':
        base_unit = 'km'
    elif choice == '2':
        base_unit = 'm'
    elif choice == '3':
        base_unit = 'dm'
    elif choice == '4':
        base_unit = 'cm'
    elif choice == '5':
        base_unit = 'mm'
    elif choice == '6':
        base_unit = 'um'
    elif choice == '7':
        base_unit = 'nm'
    elif choice == '8':
        base_unit = 'mi'
    elif choice == '9':
        base_unit = 'yd'
    elif choice == '10':
        base_unit = 'ft'
    elif choice == '11':
        base_unit = 'in'
    elif choice == '12':
        return
    else:
        length_conversion()
    while True:
        try:
            value = float(input('Enter the value in ' + base_unit + ': '))
            break
        except ValueError:
            print('Invalid input, try again')
    print("\033[H\033[J", end="")
    print('Select a target unit')
    print('1. Kilometer (km)')
    print('2. Meter (m)')
    print('3. Decimeter (dm)')
    print('4. Centimeter (cm)')
    print('5. Millimeter (mm)')
    print('6. Micrometer (um)')
    print('7. Nanometer (nm)')
    print('8. Mile (mi)')
    print('9. Yard (yd)')
    print('10. Foot (ft)')
    print('11. Inch (in)')
    print('12. Back')
    choice = input('Enter your choice: ')
    if choice == '1':
        target_unit = 'km'
    elif choice == '2':
        target_unit = 'm'
    elif choice == '3':
        target_unit = 'dm'
    elif choice == '4':
        target_unit = 'cm'
    elif choice == '5':
        target_unit = 'mm'
    elif choice == '6':
        target_unit = 'um'
    elif choice == '7':
        target_unit = 'nm'
    elif choice == '8':
        target_unit = 'mi'
    elif choice == '9':
        target_unit = 'yd'
    elif choice == '10':
        target_unit = 'ft'
    elif choice == '11':
        target_unit = 'in'
    elif choice == '12':
        length_conversion()

    #convert to base unit
    if base_unit == 'km':
        in_m = value * 1000
    elif base_unit == 'm':
        in_m = value
    elif base_unit == 'dm':
        in_m = value / 10
    elif base_unit == 'cm':
        in_m = value / 100
    elif base_unit == 'mm':
        in_m = value / 1000
    elif base_unit == 'um':
        in_m = value / 1000000
    elif base_unit == 'nm':
        in_m = value / 1000000000
    elif base_unit == 'mi':
        in_m = value * 1609.344
    elif base_unit == 'yd':
        in_m = value * 0.9144
    elif base_unit == 'ft':
        in_m = value * 0.3048
    elif base_unit == 'in':
        in_m = value * 0.0254

    d = {
        1: [f'{value} {base_unit}', '1 m'],
    }

    if target_unit != 'm':
        if target_unit == 'mm':
            d[1] = [f'{value} {base_unit}', '1 m', f'1000 {target_unit}']
            d[2] = [' ' * len(f'{value} {base_unit}'), f'1000 {base_unit}', '1 m']
        if target_unit == 'km':
            d[1] = [f'{value} {base_unit}', '1 m', f'0.001 {target_unit}']
            d[2] = [' ' * len(f'{value} {base_unit}'), f'0.001 {base_unit}', '1 m']
        if target_unit == 'dm':
            d[1] = [f'{value} {base_unit}', '1 m', f'10 {target_unit}']
            d[2] = [' ' * len(f'{value} {base_unit}'), f'10 {base_unit}', '1 m']
        if target_unit == 'cm':
            d[1] = [f'{value} {base_unit}', '1 m', f'100 {target_unit}']
            d[2] = [' ' * len(f'{value} {base_unit}'), f'100 {base_unit}', '1 m']
        if target_unit == 'um':
            d[1] = [f'{value} {base_unit}', '1 m', f'1000000 {target_unit}']
            d[2] = [' ' * len(f'{value} {base_unit}'), f'1000000 {base_unit}', '1 m']
        if target_unit == 'nm':
            d[1] = [f'{value} {base_unit}', '1 m', f'1000000000 {target_unit}']
            d[2] = [' ' * len(f'{value} {base_unit}'), f'1000000000 {base_unit}', '1 m']
        if target_unit == 'mi':
            d[1] = [f'{value} {base_unit}', '1 m', f'0.000621371 {target_unit}']
            d[2] = [' ' * len(f'{value} {base_unit}'), f'0.000621371 {base_unit}', '1 m']
        if target_unit == 'yd':
            d[1] = [f'{value} {base_unit}', '1 m', f'1.09361 {target_unit}']
            d[2] = [' ' * len(f'{value} {base_unit}'), f'1.09361 {base_unit}', '1 m']
        if target_unit == 'ft':
            d[1] = [f'{value} {base_unit}', '1 m', f'3.28084 {target_unit}']
            d[2] = [' ' * len(f'{value} {base_unit}'), f'3.28084 {base_unit}', '1 m']
        if target_unit == 'in':
            d[1] = [f'{value} {base_unit}', '1 m', f'39.3701 {target_unit}']
            d[2] = [' ' * len(f'{value} {base_unit}'), f'39.3701 {base_unit}', '1 m']
    if target_unit == 'm':
        if base_unit == 'mm':
            d[1] = [f'{value} {base_unit}', '1 m']
            d[2] = [' ' * len(f'{value} {base_unit}'), '1000 mm']
        if base_unit == 'km':
            d[1] = [f'{value} {base_unit}', '1 m']
            d[2] = [' ' * len(f'{value} {base_unit}'), '0.001 km']
        if base_unit == 'dm':
            d[1] = [f'{value} {base_unit}', '1 m']
            d[2] = [' ' * len(f'{value} {base_unit}'), '10 dm']
        if base_unit == 'cm':
            d[1] = [f'{value} {base_unit}', '1 m']
            d[2] = [' ' * len(f'{value} {base_unit}'), '100 cm']
        if base_unit == 'um':
            d[1] = [f'{value} {base_unit}', '1 m']
            d[2] = [' ' * len(f'{value} {base_unit}'), '1000000 um']
        if base_unit == 'nm':
            d[1] = [f'{value} {base_unit}', '1 m']
            d[2] = [' ' * len(f'{value} {base_unit}'), '1000000000 nm']
        if base_unit == 'mi':
            d[1] = [f'{value} {base_unit}', '1 m']
            d[2] = [' ' * len(f'{value} {base_unit}'), '0.000621371 mi']
        if base_unit == 'yd':
            d[1] = [f'{value} {base_unit}', '1 m']
            d[2] = [' ' * len(f'{value} {base_unit}'), '1.09361 yd']
        if base_unit == 'ft':
            d[1] = [f'{value} {base_unit}', '1 m']
            d[2] = [' ' * len(f'{value} {base_unit}'), '3.28084 ft']
        if base_unit == 'in':
            d[1] = [f'{value} {base_unit}', '1 m']
            d[2] = [' ' * len(f'{value} {base_unit}'), '39.3701 in']

    #adjust spacing
    for i in range(1, len(d) + 1):
        for j in range(len(d[i])):
            if len(d[i][j]) < len(d[i][j - 1]):
                d[i][j] = ' ' * (len(d[i][j - 1]) - len(d[i][j])) + d[i][j]
            elif len(d[i][j]) > len(d[i][j - 1]):
                d[i][j - 1] = ' ' * (len(d[i][j]) - len(d[i][j - 1])) + d[i][j - 1]

    #print conversion
    print("\033[H\033[J", end="")
    for _, value in d.items():
        print(' | '.join(value))
    print('\n')
    #print final conversion
    print('Final Answer:')
    if target_unit == 'm':
        print(f'{in_m} {target_unit}')
    elif target_unit == 'mm':
        print(f'{in_m * 1000} {target_unit}')
    elif target_unit == 'km':
        print(f'{in_m / 1000} {target_unit}')
    elif target_unit == 'dm':
        print(f'{in_m * 10} {target_unit}')
    elif target_unit == 'cm':
        print(f'{in_m * 100} {target_unit}')
    elif target_unit == 'um':
        print(f'{in_m * 1000000} {target_unit}')
    elif target_unit == 'nm':
        print(f'{in_m * 1000000000} {target_unit}')
    elif target_unit == 'mi':
        print(f'{in_m / 1609.34} {target_unit}')
    elif target_unit == 'yd':
        print(f'{in_m * 1.09361} {target_unit}')
    elif target_unit == 'ft':
        print(f'{in_m * 3.28084} {target_unit}')
    elif target_unit == 'in':
        print(f'{in_m * 39.3701} {target_unit}')
    #print final conversion in scientific notation
    if target_unit == 'm':
        print(f'{in_m:.6e} {target_unit}')
    elif target_unit == 'mm':
        print(f'{in_m * 1000:.6e} {target_unit}')
    elif target_unit == 'km':
        print(f'{in_m / 1000:.6e} {target_unit}')
    elif target_unit == 'dm':
        print(f'{in_m * 10:.6e} {target_unit}')
    elif target_unit == 'cm':
        print(f'{in_m * 100:.6e} {target_unit}')
    elif target_unit == 'um':
        print(f'{in_m * 1000000:.6e} {target_unit}')
    elif target_unit == 'nm':
        print(f'{in_m * 1000000000:.6e} {target_unit}')
    elif target_unit == 'mi':
        print(f'{in_m / 1609.34:.6e} {target_unit}')
    elif target_unit == 'yd':
        print(f'{in_m * 1.09361:.6e} {target_unit}')
    elif target_unit == 'ft':
        print(f'{in_m * 3.28084:.6e} {target_unit}')
    elif target_unit == 'in':
        print(f'{in_m * 39.3701:.6e} {target_unit}')

    print('\n')

    print(f'Remember to adjust for sigfigs, your input was {value} {base_unit}')
    input('Press enter to continue...')
    return
