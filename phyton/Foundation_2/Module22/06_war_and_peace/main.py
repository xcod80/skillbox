import zipfile
import os

#вариант заумный и нерабочий
'''main_file = zipfile.ZipFile('voyna-i-mir.zip', 'r')
main_file.extractall()
main_file.close()
main_file = open('voyna-i-mir.txt', 'r')
text = [sym for sym in main_file.read() if sym.isalpha()]
freq_list = sorted(sorted([[key, value] for key, value in dict([(sym, round(text.count(sym)/len(text), 3)) for sym in text]).items()]),
                   key=lambda x: x[1], reverse=True)
ans_file = open('analysis.txt', 'w')
print('rec')
ans_file.writelines(['{} {}\n'.format(item[0], item[1]) for item in freq_list])
os.remove('voyna-i-mir.txt')
main_file.close()
ans_file.close()
'''
#Другой вариант
freq_list = dict()
main_file = zipfile.ZipFile('voyna-i-mir.zip', 'r')
main_file.extractall()
main_file.close()
main_file = open('voyna-i-mir.txt', 'r')
#загрузить буквы
text = str([sym for sym in main_file.read() if sym.isalpha()])
#удалить знаки препинания пробелы и прочее
text = text.replace(' ','')
text = text.replace('\'','')
text = text.replace(',','')
#Считаем символы
text_len = len(text)
while len(text)>0:
    sym = text[0]
    freq_list[sym] = text.count(sym)/text_len
    text = text.replace(sym, '') #Улалить лишнее
freq_list = sorted(sorted([[key, value] for key, value in freq_list.items()]), key=lambda x: x[1], reverse=True)
ans_file = open('analysis.txt', 'w')
ans_file.writelines(['{} {}\n'.format(item[0], item[1]) for item in freq_list])
ans_file.close()
main_file.close()
os.remove('voyna-i-mir.txt')