import os

def scan_dir(my_path):
    my_files, my_bytes, my_dirs  = 0, 0, 0
    for elem in os.listdir(my_path):
        tmp_name = os.path.join(my_path, elem)
        if os.path.isfile(tmp_name):
            my_files +=1
            my_bytes += os.path.getsize(tmp_name)
        elif os.path.isdir(tmp_name):
            tm_dirs, tm_files, tm_bytes = scan_dir(tmp_name)
            my_dirs += tm_dirs + 1
            my_files += tm_files
            my_bytes += tm_bytes
    return my_dirs, my_files, my_bytes
path = input('Введите путь до каталога: ')

if os.path.exists(path):
    total_dirs, total_files, total_bytes = scan_dir(path)
else:
    print('Каталог не существует!')
    exit()
print(path)
print('Размер каталога (в Кб):',total_bytes / 1024)
print('Количество подкаталогов:', total_dirs)
print('Количество файлов:', total_files)
