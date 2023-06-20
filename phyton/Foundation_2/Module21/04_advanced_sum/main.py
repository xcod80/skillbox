def super_sum(*args):
    sum = 0
    for arg in args:
        if isinstance(arg,(tuple, dict, list)):
            for item in arg:
                if isinstance(item, (int, float)):
                    sum += item
                elif isinstance(item,(tuple, dict, list)):
                    sum += super_sum(item)
        elif isinstance(arg, (int, float)):
            sum += arg
    return sum
