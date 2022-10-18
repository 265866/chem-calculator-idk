"""Imports"""
from modules.conversions.length_conversion import length_conversion
from modules.conversions.mass_conversion import mass_conversion
from modules.conversions.volume_conversion import volume_conversion
from modules.conversions.temperature_conversion import temperature_conversion
#from modules.return_sigfigs import find_sigfigs as get_sigfigs

def main():
    """Main Function"""
    print("\033[H\033[J", end="")
    print('Select an option: ')
    print('1. Unit Conversion')
    print('2. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        unit_conversion()
    elif choice == '2':
        exit()
    else:
        print('Invalid choice')
        main()

def unit_conversion():
    """Unit Conversion Function"""
    print("\033[H\033[J", end="")
    print('Select an option: ')
    print('1. Mass Conversion')
    print('2. Volume Conversion')
    print('3. Temperature Conversion')
    print('4. Length Conversion')
    print('5. Back')
    choice = input('Enter your choice: ')
    if choice == '1':
        mass_conversion()
        main()
    elif choice == '2':
        volume_conversion()
        main()
    elif choice == '3':
        temperature_conversion()
    elif choice == '4':
        length_conversion()
    elif choice == '5':
        main()
    else:
        print('Invalid choice')
        unit_conversion()

if __name__ == '__main__':
    main()
