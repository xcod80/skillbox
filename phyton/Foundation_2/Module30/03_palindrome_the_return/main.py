import collections

def can_be_poly(string:str = '') -> bool:
    counters = collections.Counter(string)
    if len(list(filter(lambda count: count % 2 != 0, counters.values()))) > 1:
        return False
    else:
        return True
print(can_be_poly('abcba'))
print(can_be_poly('abbbd'))
