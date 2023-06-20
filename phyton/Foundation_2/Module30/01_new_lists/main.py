from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

new_floats = list(map(lambda elem: round(elem ** 3, 3), floats))
new_names = list(filter(lambda elem: len(elem) > 4, names))

# def mul():
#     m=1
#     for elem in numbers:
#         m *= elem
#     return m


new_numbers = reduce(lambda elem_last, elem: elem_last * elem, numbers)

print(new_floats)
print(new_names)
print(new_numbers)