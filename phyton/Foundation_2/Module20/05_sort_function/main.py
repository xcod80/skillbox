def tpl_sort(data):
    tpl_data = sorted(number for number in data if isinstance(number, int))
    if len(data) != len(tpl_data):
        return data
    else:
        return tuple(tpl_data)