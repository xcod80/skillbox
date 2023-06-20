original_text = input('Введите текст: ')
original_dict = {sym:original_text.count(sym) for sym in original_text}
print('Оригинальный словарь частот:\n')
for sym in sorted(original_dict):
    print('{} : {}'.format(sym, original_dict[sym]))
revert_dict = {sym:[char for char in original_dict if sym == original_dict[char]] for sym in original_dict.values()}
print('\nИнвертированный словарь частот:')
for sym in revert_dict:
    print('{} : {}'.format(sym, revert_dict[sym]))
