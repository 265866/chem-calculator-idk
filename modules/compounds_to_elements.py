"""This function converts element compounds to a list of elements."""
def compounds_to_elements(compound):
    """
    returns a dict with list of elements in compounds and their count
    e.g. H2O -> {'H': 2, 'O': 1}
    e.g. (NH4)2SO4 -> {'N': 2, 'H': 8, 'S': 1, 'O': 4}
    """
    from collections import Counter
    #need to make work with more than one digit number
    #need to check if any keys are a non letter

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
    keys = list(result.keys())
    blck = []
    for i in keys:
        if i.islower():
            for p in keys:
                if i in p:
                    result[p]+=result[i]
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
        del result[t]

    if '(' in compound:
        first_bracket = compound.index('(')
        last_bracket = compound.rfind(')')
        bracketed_part = compound[first_bracket + 1:last_bracket]
        bracketed_part_count = int(compound[last_bracket + 1])
        compound = compound.replace(compound[first_bracket:last_bracket + 2], '')
        compound += bracketed_part * bracketed_part_count
    elements = []
    for index, char in enumerate(compound):
        if char.isupper():
            try:
                if compound[index + 1].isupper():
                    elements.append(char)
                else:
                    elements.append(char + compound[index + 1])
            except IndexError:
                elements.append(char)
    elements_dict = {}
    for element in elements:
        if element[-1].isdigit():
            only_element = element[:-1]
            only_number = int(element[-1])
        else:
            only_element = element
            only_number = 1
        if only_element in elements_dict:
            elements_dict[only_element] += only_number
        else:
            elements_dict[only_element] = only_number

    result_2 = elements_dict
    if len(list(result_2.keys())) > len(list(result.keys())):
        return result_2
    return result
