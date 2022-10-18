"""Returns the number of sigfigs within a number"""
def find_sigfigs(number_input):
    """Returns the number of significant digits in a number. This takes into account
        strings formatted in 1.23e+3 format and even strings such as 123.450"""
    # change all the 'E' to 'e'
    number_input = number_input.lower()
    if 'e' in number_input:
        # return the length of the numbers before the 'e'
        my_str = number_input.split('e')
        return len( my_str[0] ) - 1 # to compenstate for the decimal point

    # put it in e format and return the result of that
    ### NOTE: because of the 8 below, it may do crazy things when it parses 9 sigfigs
    final = f'{number_input:.8e}'.split('e')
    # remove and count the number of removed user added zeroes. (these are sig figs)
    if '.' in number_input:
        temp = number_input.replace('.', '')
        #number of zeroes to add back in
        leng = len(temp) - len(temp.rstrip('0'))
        #strip off the python added zeroes and add back in the ones the user added
        final[0] = final[0].rstrip('0') + ''.join(['0' for num in range(leng)])
    else:
        #the user had no trailing zeroes so just strip them all
        final[0] = final[0].rstrip('0')
    #pass it back to the beginning to be parsed
    return find_sigfigs('e'.join(final))
