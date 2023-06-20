from random import randint
class Student:
    def __init__(self, FN, GroupNumber, grade):
        self.FN = FN
        self.GroupNumber = GroupNumber
        self.grade = grade
    def average_grade(self):
        return sum(self.grade)/len(self.grade)
    def print_dossier(self):
        print(f'ФИ: {self.FN}\n№Группы: {self.GroupNumber}\nСредний балл: {self.average_grade()}')

student_list = list()
for _ in range(10):
    student_list.append(Student(input('Введите Фимилию Имя студента:'),
                                randint(1,3),
                                [randint(1,5) for _ in range(5)]))
student_list = sorted(student_list, key=lambda sl:sl.average_grade())
for student in student_list:
    student.print_dossier()