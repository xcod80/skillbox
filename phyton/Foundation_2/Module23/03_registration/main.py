def check_line(in_line):
    check_value = in_line.split()
    if len(check_value) < 3:
        raise IndexError
    elif not check_value[0].isalpha():
        raise NameError
    elif check_value[1].find('@') == -1 or check_value[1].find('.') == -1:
        raise SyntaxError
    elif not int(check_value[2]) in range(10, 100):
        raise ValueError
    return

reg_file = open('registrations.txt', 'r')
good_log = open('registrations_good.log', 'w')
bad_log = open('registrations_bad.log', 'w')
for line in reg_file:
    try:
        check_line(line)
    except IndexError:
        line = line.replace('\n', '')
        bad_log.write(f'{line}\t\t Не достаточно данных для ввода\n')
    except ValueError:
        line = line.replace('\n', '')
        bad_log.write(f'{line}\t\t Поле «Возраст» НЕ является числом от 10 до 99\n')
    except SyntaxError:
        line = line.replace('\n', '')
        bad_log.write(f'{line}\t\t Поле «Имейл» НЕ содержит @ и . (точку)\n')
    except NameError:
        line = line.replace('\n', '')
        bad_log.write(f'{line}\t\t Поле «Имя» содержит НЕ только буквы\n')
    else:
        good_log.write(line)
reg_file.close()
good_log.close()
bad_log.close()