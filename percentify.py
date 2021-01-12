def percentify(list_file):
    by_second_element = lambda second_element: float(second_element[1])
    min_value = min(list_file, key=by_second_element)[1]
    max_value = max(list_file, key=by_second_element)[1] - min_value
    for line in list_file:
        ret_num = ((line[-1] - min_value) / max_value) * 100
        line[1] = ret_num

