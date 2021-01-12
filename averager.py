def denest_list(lst):  # brings all nested lists to the outside
    ret_list = list()
    for outer_list in lst:
        for nested_list in outer_list:
            ret_list.append(nested_list)
    return ret_list


def sort_by_first_element(lst):  # sort by the first element
    ret_list = sorted(lst, key=lambda element: float(element[0]), reverse=True)
    return ret_list


def bring_to_zero(lst):
    lightest_value = max(lst, key=lambda second_element: second_element[1])[1]
    for element in lst:
        element[1] = abs(lightest_value - element[1])


def averager(lst):  # put like first elements together, and average them out
    ret_list = list()
    helper_dict = dict()  # helper dictionary makes every key the first element, and the value a list of all the
    # second elements that correspond to that first element
    lst = denest_list(lst)
    for element in lst:
        if element[0] in helper_dict.keys():
            helper_dict[element[0]] += [element[-1]]
        else:
            helper_dict[element[0]] = [element[-1]]

    for key, value in helper_dict.items():
        ret_list.append([key, (sum(value) / len(value))])

    bring_to_zero(ret_list)

    return sort_by_first_element(ret_list)  # sort this list by the first element of the lists inside
