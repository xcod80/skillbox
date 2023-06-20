nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def line_list(in_list):
    temp_list = []
    for item in in_list:
        if isinstance(item, list):
            temp_list.extend(line_list(item))
        else:
            temp_list.append(item)
    return temp_list

print(line_list(nice_list))
