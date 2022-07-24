# avr = {'1':[2,3]}
# ass = sum(avr.values())/len.values()(avr)
# print(ass)
# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
#
#     def rate_lectures(self, lecturer, course, grade):
#         if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
#             if course in lecturer.lecture_grades:
#                 lecturer.lecture_grades[course] += [grade]
#             else:
#                 lecturer.lecture_grades[course] = [grade]
#         else:
#             return 'Ошибка'
#
#     def __str__(self):
#         print('Имя: ', self.name)
#         return ('Фамилия: ', self.surname)
#         # print('Средняя оценка за домашние задания: ', self.surname)
# student = Student('Bill', 'Shiphr', 'unknown')
#
# print(__str__(student))
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
grades = {'python': [9, 5, 10],
'git': [10, 10],}

def averege_score_course(student_list, course):
    # find_course = False
    score = 0
    for student in student_list
        for courses, grade in self.grades.items():
            if course in courses:
                score += sum(grade) / len(grade)
                # find_course = True
    return f'средняя оценка за домашнее задание на курсе {course} - {round(score / len(self.grades)}')

find_doc = False
    document_number = input('Введите номер документа ')
    for shelf, document in directories.items():
            if document_number in document:
                document.remove(document_number)
                find_doc = True



#
# def averege():
#     score = 0
#     for subject, grade in grades.items():
#         score += sum(grade)/len(grade)
#     return score/len(grades)
#
#
# # ass = sum(avr.values())/len.values()(avr)
# print(averege())