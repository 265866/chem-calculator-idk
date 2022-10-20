"""Imports"""
from modules.standard_conversions.length_conversion import length_conversion
from modules.standard_conversions.mass_conversion import mass_conversion
from modules.standard_conversions.volume_conversion import volume_conversion
from modules.standard_conversions.temperature_conversion import temperature_conversion
from modules.mole_conversions.grams_to_moles import grams_to_moles
from modules.mole_conversions.moles_to_grams import moles_to_grams
#from modules.mole_conversions.moles_to_particles import moles_to_particles
#from modules.mole_conversions.particles_to_moles import particles_to_moles
#from modules.mole_conversions.particles_to_grams import particles_to_grams
#from modules.mole_conversions.grams_to_particles import grams_to_particles
from modules.return_sigfigs import find_sigfigs as get_sigfigs
from modules.compounds_to_elements import compounds_to_elements as cte

def main():
    """Main Function"""
    print("\033[H\033[J", end="")
    print('Select an option: ')
    print('1. Unit Conversions')
    print('2. Mole Conversions')
    print('3. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        unit_conversion()
    elif choice == '2':
        mole_conversion()
    elif choice == '3':
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
        main()
    elif choice == '4':
        length_conversion()
        main()
    elif choice == '5':
        main()
    else:
        print('Invalid choice')
        unit_conversion()

def mole_conversion():
    """Mole Conversion Function"""
    print("\033[H\033[J", end="")
    print('Select an option: ')
    print('1. Grams to Moles')
    print('2. Moles to Grams')
    print('3. Moles to Particles')
    print('4. Particles to Moles')
    print('5. Grams to Particles')
    print('6. Particles to Grams')
    print('7. Back')
    choice = input('Enter your choice: ')
    if choice == '1':
        grams_to_moles()
        main()
    elif choice == '2':
        moles_to_grams()
        main()
    elif choice == '3':
        moles_to_particles()
        main()
    elif choice == '4':
        particles_to_moles()
        main()
    elif choice == '5':
        grams_to_particles()
        main()
    elif choice == '6':
        particles_to_grams()
        main()
    elif choice == '7':
        main()
    else:
        print('Invalid choice')
        mole_conversion()

if __name__ == '__main__':
    main()
