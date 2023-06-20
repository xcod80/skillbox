students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def interest_and_surnamelen(dictionary):
    lst = [student for id in dictionary for student in dictionary[id]['interests']]
    cnt = sum([len(dictionary[id]['surname']) for id in dictionary])
    return lst, cnt

print('Список пар "ID студента — возраст":', [(id, students[id]['age']) for id in students])
intersts_lst, surname_len = interest_and_surnamelen(students)
print('Полный список интересов всех студентов:', intersts_lst)
print('Общая длина всех фамилий студентов:', surname_len)
