import os

def gen_files_path(userdir:str='.'):
    files_list = list()
    for item in os.walk(userdir):
        for fname in item[2]:
            files_list.append(os.path.join(item[0], fname))
    return files_list


print(gen_files_path('c:\\source'))

#Правильное решение:

def root_path() -> str:
    return os.path.abspath(os.sep)


def gen_files_path(folder: str, path=os.path.abspath(os.sep)):
    for root, dirs, files in os.walk(path):
        print(root, dirs, files)
        for file in files:
            yield os.path.join(root, file)
        if folder in dirs:
            print(f'Искомая директория {folder} найдена {os.path.join(root, folder)}')
            return True


def main():
    """
    Проход по каталогу с решениями
    И поиск текущей директории

    :return:
    """

    current_folder = os.path.basename(os.path.abspath('./'))

    for file_path in gen_files_path(current_folder):
        print(file_path)


main()