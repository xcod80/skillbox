alphabet = [chr(sym) for sym in range(ord('a'),ord('z')+1)]
main_file = open('text.txt', 'r')
text = [sym for sym in main_file.read().lower() if sym in alphabet]
freq_list = sorted(sorted([[key, value] for key, value in dict([(sym, round(text.count(sym)/len(text), 3)) for sym in text]).items()]),
                   key=lambda x: x[1], reverse=True)
ans_file = open('analysis.txt', 'w')
ans_file.writelines(['{} {}\n'.format(item[0], item[1]) for item in freq_list])
main_file.close()
ans_file.close()