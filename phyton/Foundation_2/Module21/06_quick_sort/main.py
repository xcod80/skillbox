def hoar_sort(in_list):
    min_list = [item for item in in_list if item < in_list[len(in_list)-1]]
    equ_list = [item for item in in_list if item == in_list[len(in_list)-1]]
    max_list = [item for item in in_list if item > in_list[len(in_list)-1]]
    if len(min_list) == 0 and len(max_list) != 0:
        return equ_list + hoar_sort(max_list)
    elif len(min_list) != 0 and len(max_list) == 0:
        return hoar_sort(min_list) + equ_list
    elif len(min_list) == 0 and len(max_list) == 0:
        return equ_list
    return hoar_sort(min_list)+equ_list+hoar_sort(max_list)
