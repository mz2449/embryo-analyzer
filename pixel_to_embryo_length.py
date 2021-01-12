def pixel_to_embryo_length(lst):
    ret_list = list()
    last_line = lst[-1]  # this should also be line with the largest first element
    for line in lst:
        if line[0].isnumeric():  # filters out lines that are not numbers
            first_element = float(line[0])
            max_first_element = float(last_line[0])
            first_element = float(format(100 * (max_first_element - first_element) / max_first_element, '.1f'))
            """
            IMPORTANT: IMAGEJ PLOTS X CORD START AT ZERO
            Divide difference between maximum number and original number by maximum number, then
            multiply by 100 to obtain a percentage with 100% at the beginning (equivalent to the original 0)
            (in Drosophila, 100 indicates the anterior)
            """
            ret_line = [first_element, float(line[-1])]
            ret_list.append(ret_line)
    return ret_list
