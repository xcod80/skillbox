import os

text_file = open('zen.txt', 'r')
text = text_file.read().split('\n')
text.reverse()
print('\n'.join(text))
text_file.close()