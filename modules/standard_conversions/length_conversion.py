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
            inp = input('Enter a value in ' + base_unit + ': ')
            if '*10^' in inp:
                value = float(inp.split('*10^')[0]) * 10 ** float(inp.split('*10^')[1])
            else:
                value = float(inp)
            break
        except ValueError:
            print('Invalid input')
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

    if base_unit == 'km':
        if target_unit == 'km':
            result = value
        elif target_unit == 'm':
            result = value * 1000
        elif target_unit == 'dm':
            result = value * 10000
        elif target_unit == 'cm':
            result = value * 100000
        elif target_unit == 'mm':
            result = value * 1000000
        elif target_unit == 'um':
            result = value * 1000000000
        elif target_unit == 'nm':
            result = value * 1000000000000
        elif target_unit == 'mi':
            result = value * 0.621371
        elif target_unit == 'yd':
            result = value * 1093.61
        elif target_unit == 'ft':
            result = value * 3280.84
        elif target_unit == 'in':
            result = value * 39370.1
    elif base_unit == 'm':
        if target_unit == 'km':
            result = value * 0.001
        elif target_unit == 'm':
            result = value
        elif target_unit == 'dm':
            result = value * 10
        elif target_unit == 'cm':
            result = value * 100
        elif target_unit == 'mm':
            result = value * 1000
        elif target_unit == 'um':
            result = value * 1000000
        elif target_unit == 'nm':
            result = value * 1000000000
        elif target_unit == 'mi':
            result = value * 0.000621371
        elif target_unit == 'yd':
            result = value * 1.09361
        elif target_unit == 'ft':
            result = value * 3.28084
        elif target_unit == 'in':
            result = value * 39.3701
    elif base_unit == 'dm':
        if target_unit == 'km':
            result = value * 0.0001
        elif target_unit == 'm':
            result = value * 0.1
        elif target_unit == 'dm':
            result = value
        elif target_unit == 'cm':
            result = value * 10
        elif target_unit == 'mm':
            result = value * 100
        elif target_unit == 'um':
            result = value * 100000
        elif target_unit == 'nm':
            result = value * 100000000
        elif target_unit == 'mi':
            result = value * 0.0000621371
        elif target_unit == 'yd':
            result = value * 0.109361
        elif target_unit == 'ft':
            result = value * 0.328084
        elif target_unit == 'in':
            result = value * 3.93701
    elif base_unit == 'cm':
        if target_unit == 'km':
            result = value * 0.00001
        elif target_unit == 'm':
            result = value * 0.01
        elif target_unit == 'dm':
            result = value * 0.1
        elif target_unit == 'cm':
            result = value
        elif target_unit == 'mm':
            result = value * 10
        elif target_unit == 'um':
            result = value * 10000
        elif target_unit == 'nm':
            result = value * 10000000
        elif target_unit == 'mi':
            result = value * 0.00000621371
        elif target_unit == 'yd':
            result = value * 0.0109361
        elif target_unit == 'ft':
            result = value * 0.0328084
        elif target_unit == 'in':
            result = value * 0.393701
    elif base_unit == 'mm':
        if target_unit == 'km':
            result = value * 0.000001
        elif target_unit == 'm':
            result = value * 0.001
        elif target_unit == 'dm':
            result = value * 0.01
        elif target_unit == 'cm':
            result = value * 0.1
        elif target_unit == 'mm':
            result = value
        elif target_unit == 'um':
            result = value * 1000
        elif target_unit == 'nm':
            result = value * 1000000
        elif target_unit == 'mi':
            result = value * 0.000000621371
        elif target_unit == 'yd':
            result = value * 0.00109361
        elif target_unit == 'ft':
            result = value * 0.00328084
        elif target_unit == 'in':
            result = value * 0.0393701
    elif base_unit == 'um':
        if target_unit == 'km':
            result = value * 0.000000001
        elif target_unit == 'm':
            result = value * 0.000001
        elif target_unit == 'dm':
            result = value * 0.00001
        elif target_unit == 'cm':
            result = value * 0.0001
        elif target_unit == 'mm':
            result = value * 0.001
        elif target_unit == 'um':
            result = value
        elif target_unit == 'nm':
            result = value * 1000
        elif target_unit == 'mi':
            result = value * 0.000000000621371
        elif target_unit == 'yd':
            result = value * 0.00000109361
        elif target_unit == 'ft':
            result = value * 0.00000328084
        elif target_unit == 'in':
            result = value * 0.0000393701
    elif base_unit == 'nm':
        if target_unit == 'km':
            result = value * 0.000000000001
        elif target_unit == 'm':
            result = value * 0.000000001
        elif target_unit == 'dm':
            result = value * 0.00000001
        elif target_unit == 'cm':
            result = value * 0.0000001
        elif target_unit == 'mm':
            result = value * 0.000001
        elif target_unit == 'um':
            result = value * 0.001
        elif target_unit == 'nm':
            result = value
        elif target_unit == 'mi':
            result = value * 0.000000000000621371
        elif target_unit == 'yd':
            result = value * 0.00000000109361
        elif target_unit == 'ft':
            result = value * 0.00000000328084
        elif target_unit == 'in':
            result = value * 0.0000000393701
    elif base_unit == 'mi':
        if target_unit == 'km':
            result = value * 1.60934
        elif target_unit == 'm':
            result = value * 1609.34
        elif target_unit == 'dm':
            result = value * 16093.4
        elif target_unit == 'cm':
            result = value * 160934
        elif target_unit == 'mm':
            result = value * 1609340
        elif target_unit == 'um':
            result = value * 1609340000
        elif target_unit == 'nm':
            result = value * 1609340000000
        elif target_unit == 'mi':
            result = value
        elif target_unit == 'yd':
            result = value * 1760
        elif target_unit == 'ft':
            result = value * 5280
        elif target_unit == 'in':
            result = value * 63360
    elif base_unit == 'yd':
        if target_unit == 'km':
            result = value * 0.0009144
        elif target_unit == 'm':
            result = value * 0.9144
        elif target_unit == 'dm':
            result = value * 9.144
        elif target_unit == 'cm':
            result = value * 91.44
        elif target_unit == 'mm':
            result = value * 914.4
        elif target_unit == 'um':
            result = value * 914400
        elif target_unit == 'nm':
            result = value * 914400000
        elif target_unit == 'mi':
            result = value * 0.000568182
        elif target_unit == 'yd':
            result = value
        elif target_unit == 'ft':
            result = value * 3
        elif target_unit == 'in':
            result = value * 36
    elif base_unit == 'ft':
        if target_unit == 'km':
            result = value * 0.0003048
        elif target_unit == 'm':
            result = value * 0.3048
        elif target_unit == 'dm':
            result = value * 3.048
        elif target_unit == 'cm':
            result = value * 30.48
        elif target_unit == 'mm':
            result = value * 304.8
        elif target_unit == 'um':
            result = value * 304800
        elif target_unit == 'nm':
            result = value * 304800000
        elif target_unit == 'mi':
            result = value * 0.000189394
        elif target_unit == 'yd':
            result = value * 0.333333
        elif target_unit == 'ft':
            result = value
        elif target_unit == 'in':
            result = value * 12
    elif base_unit == 'in':
        if target_unit == 'km':
            result = value * 0.0000254
        elif target_unit == 'm':
            result = value * 0.0254
        elif target_unit == 'dm':
            result = value * 0.254
        elif target_unit == 'cm':
            result = value * 2.54
        elif target_unit == 'mm':
            result = value * 25.4
        elif target_unit == 'um':
            result = value * 25400
        elif target_unit == 'nm':
            result = value * 25400000
        elif target_unit == 'mi':
            result = value * 0.0000157828
        elif target_unit == 'yd':
            result = value * 0.0277778
        elif target_unit == 'ft':
            result = value * 0.0833333
        elif target_unit == 'in':
            result = value

    if len(str(value)) > 8:
        print_dict_value = f'{value:.8e}'
    else:
        print_dict_value = value

    if base_unit == target_unit:
        print(f'{print_dict_value} {base_unit} = {result} {target_unit}')
        input('Press enter to continue')
        return

    if len(str(value)) > 8:
        print_dict_value = f'{value:.8e}'
    else:
        print_dict_value = value

    print_dict = {}

    if base_unit == 'km':
        if target_unit == 'm':
            print_dict[1] = [f'{print_dict_value} km', '1000 m']
            print_dict[2] = ['', '1 km']
        elif target_unit == 'dm':
            print_dict[1] = [f'{print_dict_value} km', '10000 dm']
            print_dict[2] = ['', '1 km']
        elif target_unit == 'cm':
            print_dict[1] = [f'{print_dict_value} km', '100000 cm']
            print_dict[2] = ['', '1 km']
        elif target_unit == 'mm':
            print_dict[1] = [f'{print_dict_value} km', '1000000 mm']
            print_dict[2] = ['', '1 km']
        elif target_unit == 'um':
            print_dict[1] = [f'{print_dict_value} km', '1000000000 um']
            print_dict[2] = ['', '1 km']
        elif target_unit == 'nm':
            print_dict[1] = [f'{print_dict_value} km', '1000000000000 nm']
            print_dict[2] = ['', '1 km']
        elif target_unit == 'mi':
            print_dict[1] = [f'{print_dict_value} km', '0.621371 mi']
            print_dict[2] = ['', '1 km']
        elif target_unit == 'yd':
            print_dict[1] = [f'{print_dict_value} km', '1093.61 yd']
            print_dict[2] = ['', '1 km']
        elif target_unit == 'ft':
            print_dict[1] = [f'{print_dict_value} km', '3280.84 ft']
            print_dict[2] = ['', '1 km']
        elif target_unit == 'in':
            print_dict[1] = [f'{print_dict_value} km', '39370.1 in']
            print_dict[2] = ['', '1 km']
    elif base_unit == 'm':
        if target_unit == 'km':
            print_dict[1] = [f'{print_dict_value} m', '0.001 km']
            print_dict[2] = ['', '1 m']
        elif target_unit == 'dm':
            print_dict[1] = [f'{print_dict_value} m', '10 dm']
            print_dict[2] = ['', '1 m']
        elif target_unit == 'cm':
            print_dict[1] = [f'{print_dict_value} m', '100 cm']
            print_dict[2] = ['', '1 m']
        elif target_unit == 'mm':
            print_dict[1] = [f'{print_dict_value} m', '1000 mm']
            print_dict[2] = ['', '1 m']
        elif target_unit == 'um':
            print_dict[1] = [f'{print_dict_value} m', '1000000 um']
            print_dict[2] = ['', '1 m']
        elif target_unit == 'nm':
            print_dict[1] = [f'{print_dict_value} m', '1000000000 nm']
            print_dict[2] = ['', '1 m']
        elif target_unit == 'mi':
            print_dict[1] = [f'{print_dict_value} m', '0.000621371 mi']
            print_dict[2] = ['', '1 m']
        elif target_unit == 'yd':
            print_dict[1] = [f'{print_dict_value} m', '1.09361 yd']
            print_dict[2] = ['', '1 m']
        elif target_unit == 'ft':
            print_dict[1] = [f'{print_dict_value} m', '3.28084 ft']
            print_dict[2] = ['', '1 m']
        elif target_unit == 'in':
            print_dict[1] = [f'{print_dict_value} m', '39.3701 in']
            print_dict[2] = ['', '1 m']
    elif base_unit == 'dm':
        if target_unit == 'km':
            print_dict[1] = [f'{print_dict_value} dm', '0.0001 km']
            print_dict[2] = ['', '1 dm']
        elif target_unit == 'm':
            print_dict[1] = [f'{print_dict_value} dm', '0.1 m']
            print_dict[2] = ['', '1 dm']
        elif target_unit == 'cm':
            print_dict[1] = [f'{print_dict_value} dm', '10 cm']
            print_dict[2] = ['', '1 dm']
        elif target_unit == 'mm':
            print_dict[1] = [f'{print_dict_value} dm', '100 mm']
            print_dict[2] = ['', '1 dm']
        elif target_unit == 'um':
            print_dict[1] = [f'{print_dict_value} dm', '100000 um']
            print_dict[2] = ['', '1 dm']
        elif target_unit == 'nm':
            print_dict[1] = [f'{print_dict_value} dm', '100000000 nm']
            print_dict[2] = ['', '1 dm']
        elif target_unit == 'mi':
            print_dict[1] = [f'{print_dict_value} dm', '0.0000621371 mi']
            print_dict[2] = ['', '1 dm']
        elif target_unit == 'yd':
            print_dict[1] = [f'{print_dict_value} dm', '0.109361 yd']
            print_dict[2] = ['', '1 dm']
        elif target_unit == 'ft':
            print_dict[1] = [f'{print_dict_value} dm', '0.328084 ft']
            print_dict[2] = ['', '1 dm']
        elif target_unit == 'in':
            print_dict[1] = [f'{print_dict_value} dm', '3.93701 in']
            print_dict[2] = ['', '1 dm']
    elif base_unit == 'cm':
        if target_unit == 'km':
            print_dict[1] = [f'{print_dict_value} cm', '0.00001 km']
            print_dict[2] = ['', '1 cm']
        elif target_unit == 'm':
            print_dict[1] = [f'{print_dict_value} cm', '0.01 m']
            print_dict[2] = ['', '1 cm']
        elif target_unit == 'dm':
            print_dict[1] = [f'{print_dict_value} cm', '0.1 dm']
            print_dict[2] = ['', '1 cm']
        elif target_unit == 'mm':
            print_dict[1] = [f'{print_dict_value} cm', '10 mm']
            print_dict[2] = ['', '1 cm']
        elif target_unit == 'um':
            print_dict[1] = [f'{print_dict_value} cm', '10000 um']
            print_dict[2] = ['', '1 cm']
        elif target_unit == 'nm':
            print_dict[1] = [f'{print_dict_value} cm', '10000000 nm']
            print_dict[2] = ['', '1 cm']
        elif target_unit == 'mi':
            print_dict[1] = [f'{print_dict_value} cm', '0.00000621371 mi']
            print_dict[2] = ['', '1 cm']
        elif target_unit == 'yd':
            print_dict[1] = [f'{print_dict_value} cm', '0.0109361 yd']
            print_dict[2] = ['', '1 cm']
        elif target_unit == 'ft':
            print_dict[1] = [f'{print_dict_value} cm', '0.0328084 ft']
            print_dict[2] = ['', '1 cm']
        elif target_unit == 'in':
            print_dict[1] = [f'{print_dict_value} cm', '0.393701 in']
            print_dict[2] = ['', '1 cm']
    elif base_unit == 'mm':
        if target_unit == 'km':
            print_dict[1] = [f'{print_dict_value} mm', '0.000001 km']
            print_dict[2] = ['', '1 mm']
        elif target_unit == 'm':
            print_dict[1] = [f'{print_dict_value} mm', '0.001 m']
            print_dict[2] = ['', '1 mm']
        elif target_unit == 'dm':
            print_dict[1] = [f'{print_dict_value} mm', '0.01 dm']
            print_dict[2] = ['', '1 mm']
        elif target_unit == 'cm':
            print_dict[1] = [f'{print_dict_value} mm', '0.1 cm']
            print_dict[2] = ['', '1 mm']
        elif target_unit == 'um':
            print_dict[1] = [f'{print_dict_value} mm', '1000 um']
            print_dict[2] = ['', '1 mm']
        elif target_unit == 'nm':
            print_dict[1] = [f'{print_dict_value} mm', '1000000 nm']
            print_dict[2] = ['', '1 mm']
        elif target_unit == 'mi':
            print_dict[1] = [f'{print_dict_value} mm', '0.000000621371 mi']
            print_dict[2] = ['', '1 mm']
        elif target_unit == 'yd':
            print_dict[1] = [f'{print_dict_value} mm', '0.00109361 yd']
            print_dict[2] = ['', '1 mm']
        elif target_unit == 'ft':
            print_dict[1] = [f'{print_dict_value} mm', '0.00328084 ft']
            print_dict[2] = ['', '1 mm']
        elif target_unit == 'in':
            print_dict[1] = [f'{print_dict_value} mm', '0.0393701 in']
            print_dict[2] = ['', '1 mm']
    elif base_unit == 'um':
        if target_unit == 'km':
            print_dict[1] = [f'{print_dict_value} um', '0.000000001 km']
            print_dict[2] = ['', '1 um']
        elif target_unit == 'm':
            print_dict[1] = [f'{print_dict_value} um', '0.000001 m']
            print_dict[2] = ['', '1 um']
        elif target_unit == 'dm':
            print_dict[1] = [f'{print_dict_value} um', '0.00001 dm']
            print_dict[2] = ['', '1 um']
        elif target_unit == 'cm':
            print_dict[1] = [f'{print_dict_value} um', '0.0001 cm']
            print_dict[2] = ['', '1 um']
        elif target_unit == 'mm':
            print_dict[1] = [f'{print_dict_value} um', '0.001 mm']
            print_dict[2] = ['', '1 um']
        elif target_unit == 'nm':
            print_dict[1] = [f'{print_dict_value} um', '1000 nm']
            print_dict[2] = ['', '1 um']
        elif target_unit == 'mi':
            print_dict[1] = [f'{print_dict_value} um', '0.000000000621371 mi']
            print_dict[2] = ['', '1 um']
        elif target_unit == 'yd':
            print_dict[1] = [f'{print_dict_value} um', '0.00000109361 yd']
            print_dict[2] = ['', '1 um']
        elif target_unit == 'ft':
            print_dict[1] = [f'{print_dict_value} um', '0.00000328084 ft']
            print_dict[2] = ['', '1 um']
        elif target_unit == 'in':
            print_dict[1] = [f'{print_dict_value} um', '0.0000393701 in']
            print_dict[2] = ['', '1 um']
    elif base_unit == 'nm':
        if target_unit == 'km':
            print_dict[1] = [f'{print_dict_value} nm', '0.000000000001 km']
            print_dict[2] = ['', '1 nm']
        elif target_unit == 'm':
            print_dict[1] = [f'{print_dict_value} nm', '0.000000001 m']
            print_dict[2] = ['', '1 nm']
        elif target_unit == 'dm':
            print_dict[1] = [f'{print_dict_value} nm', '0.00000001 dm']
            print_dict[2] = ['', '1 nm']
        elif target_unit == 'cm':
            print_dict[1] = [f'{print_dict_value} nm', '0.0000001 cm']
            print_dict[2] = ['', '1 nm']
        elif target_unit == 'mm':
            print_dict[1] = [f'{print_dict_value} nm', '0.000001 mm']
            print_dict[2] = ['', '1 nm']
        elif target_unit == 'um':
            print_dict[1] = [f'{print_dict_value} nm', '0.001 um']
            print_dict[2] = ['', '1 nm']
        elif target_unit == 'mi':
            print_dict[1] = [f'{print_dict_value} nm', '0.000000000000621371 mi']
            print_dict[2] = ['', '1 nm']
        elif target_unit == 'yd':
            print_dict[1] = [f'{print_dict_value} nm', '0.00000000109361 yd']
            print_dict[2] = ['', '1 nm']
        elif target_unit == 'ft':
            print_dict[1] = [f'{print_dict_value} nm', '0.00000000328084 ft']
            print_dict[2] = ['', '1 nm']
        elif target_unit == 'in':
            print_dict[1] = [f'{print_dict_value} nm', '0.0000000393701 in']
            print_dict[2] = ['', '1 nm']
    elif base_unit == 'mi':
        if target_unit == 'km':
            print_dict[1] = [f'{print_dict_value} mi', '1.60934 km']
            print_dict[2] = ['', '1 mi']
        elif target_unit == 'm':
            print_dict[1] = [f'{print_dict_value} mi', '1609.34 m']
            print_dict[2] = ['', '1 mi']
        elif target_unit == 'dm':
            print_dict[1] = [f'{print_dict_value} mi', '16093.4 dm']
            print_dict[2] = ['', '1 mi']
        elif target_unit == 'cm':
            print_dict[1] = [f'{print_dict_value} mi', '160934 cm']
            print_dict[2] = ['', '1 mi']
        elif target_unit == 'mm':
            print_dict[1] = [f'{print_dict_value} mi', '1609340 mm']
            print_dict[2] = ['', '1 mi']
        elif target_unit == 'um':
            print_dict[1] = [f'{print_dict_value} mi', '1609340000 um']
            print_dict[2] = ['', '1 mi']
        elif target_unit == 'nm':
            print_dict[1] = [f'{print_dict_value} mi', '1609340000000 nm']
            print_dict[2] = ['', '1 mi']
        elif target_unit == 'yd':
            print_dict[1] = [f'{print_dict_value} mi', '1760 yd']
            print_dict[2] = ['', '1 mi']
        elif target_unit == 'ft':
            print_dict[1] = [f'{print_dict_value} mi', '5280 ft']
            print_dict[2] = ['', '1 mi']
        elif target_unit == 'in':
            print_dict[1] = [f'{print_dict_value} mi', '63360 in']
            print_dict[2] = ['', '1 mi']
    elif base_unit == 'yd':
        if target_unit == 'km':
            print_dict[1] = [f'{print_dict_value} yd', '0.0009144 km']
            print_dict[2] = ['', '1 yd']
        elif target_unit == 'm':
            print_dict[1] = [f'{print_dict_value} yd', '0.9144 m']
            print_dict[2] = ['', '1 yd']
        elif target_unit == 'dm':
            print_dict[1] = [f'{print_dict_value} yd', '9.144 dm']
            print_dict[2] = ['', '1 yd']
        elif target_unit == 'cm':
            print_dict[1] = [f'{print_dict_value} yd', '91.44 cm']
            print_dict[2] = ['', '1 yd']
        elif target_unit == 'mm':
            print_dict[1] = [f'{print_dict_value} yd', '914.4 mm']
            print_dict[2] = ['', '1 yd']
        elif target_unit == 'um':
            print_dict[1] = [f'{print_dict_value} yd', '914400 um']
            print_dict[2] = ['', '1 yd']
        elif target_unit == 'nm':
            print_dict[1] = [f'{print_dict_value} yd', '914400000 nm']
            print_dict[2] = ['', '1 yd']
        elif target_unit == 'mi':
            print_dict[1] = [f'{print_dict_value} yd', '0.000568182 mi']
            print_dict[2] = ['', '1 yd']
        elif target_unit == 'ft':
            print_dict[1] = [f'{print_dict_value} yd', '3 ft']
            print_dict[2] = ['', '1 yd']
        elif target_unit == 'in':
            print_dict[1] = [f'{print_dict_value} yd', '36 in']
            print_dict[2] = ['', '1 yd']
    elif base_unit == 'ft':
        if target_unit == 'km':
            print_dict[1] = [f'{print_dict_value} ft', '0.0003048 km']
            print_dict[2] = ['', '1 ft']
        elif target_unit == 'm':
            print_dict[1] = [f'{print_dict_value} ft', '0.3048 m']
            print_dict[2] = ['', '1 ft']
        elif target_unit == 'dm':
            print_dict[1] = [f'{print_dict_value} ft', '3.048 dm']
            print_dict[2] = ['', '1 ft']
        elif target_unit == 'cm':
            print_dict[1] = [f'{print_dict_value} ft', '30.48 cm']
            print_dict[2] = ['', '1 ft']
        elif target_unit == 'mm':
            print_dict[1] = [f'{print_dict_value} ft', '304.8 mm']
            print_dict[2] = ['', '1 ft']
        elif target_unit == 'um':
            print_dict[1] = [f'{print_dict_value} ft', '304800 um']
            print_dict[2] = ['', '1 ft']
        elif target_unit == 'nm':
            print_dict[1] = [f'{print_dict_value} ft', '304800000 nm']
            print_dict[2] = ['', '1 ft']
        elif target_unit == 'mi':
            print_dict[1] = [f'{print_dict_value} ft', '0.000189394 ft']
            print_dict[2] = ['', '1 ft']
        elif target_unit == 'yd':
            print_dict[1] = [f'{print_dict_value} ft', '0.333333 yd']
            print_dict[2] = ['', '1 ft']
        elif target_unit == 'in':
            print_dict[1] = [f'{print_dict_value} ft', '12 in']
            print_dict[2] = ['', '1 ft']
    elif base_unit == 'in':
        if target_unit == 'km':
            print_dict[1] = [f'{print_dict_value} in', '0.0000254 km']
            print_dict[2] = ['', '1 in']
        elif target_unit == 'm':
            print_dict[1] = [f'{print_dict_value} in', '0.0254 m']
            print_dict[2] = ['', '1 in']
        elif target_unit == 'dm':
            print_dict[1] = [f'{print_dict_value} in', '0.254 dm']
            print_dict[2] = ['', '1 in']
        elif target_unit == 'cm':
            print_dict[1] = [f'{print_dict_value} in', '2.54 cm']
            print_dict[2] = ['', '1 in']
        elif target_unit == 'mm':
            print_dict[1] = [f'{print_dict_value} in', '25.4 mm']
            print_dict[2] = ['', '1 in']
        elif target_unit == 'um':
            print_dict[1] = [f'{print_dict_value} in', '25400 um']
            print_dict[2] = ['', '1 in']
        elif target_unit == 'nm':
            print_dict[1] = [f'{print_dict_value} in', '25400000 nm']
            print_dict[2] = ['', '1 in']
        elif target_unit == 'mi':
            print_dict[1] = [f'{print_dict_value} in', '0.0000157828 mi']
            print_dict[2] = ['', '1 in']
        elif target_unit == 'yd':
            print_dict[1] = [f'{print_dict_value} in', '0.0277778 yd']
            print_dict[2] = ['', '1 in']
        elif target_unit == 'ft':
            print_dict[1] = [f'{print_dict_value} in', '0.0833333 ft']
            print_dict[2] = ['', '1 in']

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