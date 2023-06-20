import os


def gen_pylength(userdir:str='.'):
    files_list = list()
    for fname in os.listdir(userdir):
        if fname[-3::] == '.py':
            stringcount = 0
            with open(fname, 'r') as pfile:
                for pstring in pfile:
                    if pstring != '\n' and pstring[0] != '#':
                        stringcount += 1
            yield stringcount

for i in gen_pylength():
    print(i)