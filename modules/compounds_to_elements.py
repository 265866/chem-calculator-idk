from collections import Counter
import re

"""This function converts element compounds to a list of elements."""
def compounds_to_elements_v2(compound):
    if '(' in compound:
        #find the first bracket
        first_bracket = compound.index('(')
        #find the last bracket
        last_bracket = compound.rfind(')')
        #extract the bracketed part
        bracketed_part = compound[first_bracket + 1:last_bracket]
        #extract the number of times the bracketed part is repeated
        bracketed_part_count = int(compound[last_bracket + 1])
        #remove the bracketed part from the compound
        compound = compound.replace(compound[first_bracket:last_bracket + 2], '')
        #add the bracketed part to the compound
        compound += bracketed_part * bracketed_part_count




    #seperate two letter elements
    #e.g. SO4NH4NH4 -> S O4 N H4 N H4
    #e.g. NaCl -> Na Cl
    #e.g. MgSO4 -> Mg S O4

    #List of elements
    elements = []

    #loop through the compound
    for index, char in enumerate(compound):
        #if the character is a capital letter
        if char.isupper():
            #if the next character is a capital letter
            try:
                if compound[index + 1].isupper():
                    #add the character to the list
                    elements.append(char)
                #if the next character is a lower case letter
                else:
                    #add the two characters to the list
                    elements.append(char + compound[index + 1])
            #if the character is the last character
            except IndexError:
                #add the character to the list
                elements.append(char)


    #dict to store the elements and their count
    elements_dict = {}
    for element in elements:
        #checks if the element has a number after it
        if element[-1].isdigit():
            only_element = element[:-1]
            only_number = int(element[-1])
        #if it doesnt, it sets the number to 1
        else:
            only_element = element
            only_number = 1

        #if its in the dict, it adds the number to the existing number
        if only_element in elements_dict:
            elements_dict[only_element] += only_number
        #if the element is not in the dict yet, it adds it to the dict with the number
        else:
            elements_dict[only_element] = only_number

    return elements_dict

def clean(dct):
    keys = list(dct.keys())
    blck = []
    for i in keys:
        if i.islower():
            for p in keys:
                if i in p:
                    dct[p]+=dct[i]
                    blck.append(i)
                    break

    for g in keys:
        if len(g)==1 and g.isupper():
            flg = 0
            for y in keys:
                if g in y and g!=y:
                    flg = 1
                    break
            if flg==1:
                blck.append(g)
    for t in blck:
        del dct[t]
    return(dct)

def compounds_to_elements_v3(compound):
    l = re.findall(r'[A-Z][a-z]*|\d+', re.sub('[A-Z][a-z]*(?![\da-z])', r'\g<0>1', compound))
    dct = {}
    for j in range(0,len(l)-1,2):
        dct[l[j]] = l[j+1]
    return(dct)

def compare(dct_1,dct_2):
    try:
        for key in dct_1:
            if int(dct_1[key])<int(dct_2[key]):
                #print(dct_1[key],dct_2[key],'returning True')
                return True
    except:
        return False

def compounds_to_elements(compound):
    """
    returns a dict with list of elements in compounds and their count
    e.g. H2O -> {'H': 2, 'O': 1}
    e.g. (NH4)2SO4 -> {'N': 2, 'H': 8, 'S': 1, 'O': 4}
    """
    init_sub_list = [[]]
    for iter_ in compound:
        if iter_.istitle():
            if iter_.isalpha():
                last = [iter_]
                upper = iter_
                init_sub_list[-1]+=[iter_]

        elif iter_.isalpha():
            last = upper + iter_
            init_sub_list[-1] = [last]

        elif iter_.isdigit():
            init_sub_list[-1].extend(last*(int(iter_)-1))
        elif iter_ == '(' or iter_ == '[':
            init_sub_list.append([])
        elif iter_ == ')' or iter_ == ']':
            last = init_sub_list.pop()
            init_sub_list[-1].extend(last)

    result = dict(Counter(init_sub_list[-1]))
    result = clean(result)
    result_2 = compounds_to_elements_v2(compound)
    result_3 = compounds_to_elements_v3(compound)
    try:
        for key in result_3:
            result_3[key] = int(result_3[key])
    except:
        pass
    flag = 0

    if len(list(result_2.keys()))>len(list(result.keys())):
        if compare(result_2,result_3):
            return result_3
        else:
            return result_2
    if compare(result,result_3):
        return result_3
    else:
        return result
        