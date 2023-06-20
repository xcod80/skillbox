# TODO здесь писать код
file_name = input("Название файла: ")
if file_name.startswith(('@','№','$','%','^','&','\\','*','(',')')):
    print("Ошибка: название начинается на один из специальных символов.")
elif not file_name.endswith(".txt") and not file_name.endswith(".docx"):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
else:
    print("Файл назван верно.")