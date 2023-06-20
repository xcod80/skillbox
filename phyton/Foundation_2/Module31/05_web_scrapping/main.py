import requests
import re

# # В данном случае запрос request.get заменен на загрзку сайта из файла html
# with open('examples.html', 'r') as f:
#     text = f.read()
# # По итогу вы так же получаете код сайта в виде одной строки
#

text = requests.get(input('Введите адрес сайта: ')).text #https://habr.com/ru/articles/349860/
head_list = [re.sub(r'</{,1}[hH]3>','', head) for head in re.findall(r'<[hH]3>.+</[hH]3>', text)]
print(head_list)