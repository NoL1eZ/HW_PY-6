class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # the function allows students to rate lecturers
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print('Имя: ', self.name)
        print('Фамилия: ', self.surname)
        print(f'Средняя оценка за домашние задания: {averege(self)}')
        print('Курсы в процессе изучения: ', self.courses_in_progress)
        return 'Завершенные курсы: Введение в программирование'

    # возможность сравнивать между собой студентов по средней оценке за домашние задания.
    def best_students(self, student):
        if not isinstance(student, Student):
            return 'Error[not student]'
        if averege(student) > averege(self):
            return f'{student.name} {student.surname} делает домашнюю работу лучше чем {self.name} {self.surname}'
        else:
            return f'{self.name} {self.surname} делает домашнюю работу лучше чем {self.name} {self.surname}'




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}
    # def lecture_grades(self):
    #     self.grades = {}

# возможность сравнивать между собой лекторов по средней оценке за лекции.
    def best_lecturer(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            return 'Error[not lecturer]'
        if averege(lecturer) > averege(self):
            return f'{lecturer.name} {lecturer.surname} ведет занятия лучше чем {self.name} {self.surname}'
        else:
            return f'{self.name} {self.surname} ведет занятия лучше чем {lecturer.name} {lecturer.surname}'

    def __str__(self):
        print('Имя: ', self.name)
        print('Фамилия: ', self.surname)
        return f'Средняя оценка за лекции: {averege(self)}'


#the function of mentors to evaluate students home work
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print('Имя: ', self.name)
        return 'Фамилия: ', self.surname


#function for calculating the average score
def averege(self):
    score = 0
    for subject, grade in self.grades.items():
        score += sum(grade) / len(grade)
    return round(score / len(self.grades))

def averege_score_homework(student_list, course):
    # find_course = False
    score = 0
    for student in student_list:
        for courses, grade in student.grades.items():
            if course == courses:
                score += sum(grade) / (len(grade) * len(student_list))
                # find_course = True
    return (f'Cредняя оценка за домашнее задание на курсе {course} - {round(score / len(student.grades))}')

def averege_score_courses(lecturer_list, course):
    # find_course = False
    score = 0
    for lecturer in lecturer_list:
        for courses, grade in lecturer.grades.items():
            if course == courses:
                score += sum(grade) / (len(grade) * len(lecturer_list))
                # find_course = True
    return (f'Cредняя оценка за лекцию на курсе {course} - {round(score / len(lecturer.grades))}')

# # def get_avg_student_grade(student_list, course):
# #     total_sum = 0
# #     for student in student_list:
# #         for c, grades_list in student.grades.items():
# #             if c == course:
# #                 total_sum += sum(grades_list) / len(grades_list)
# #     return round(total_sum / len(student_list), 2)
#
# print(get_avg_student_grade(student_lsit, 'Python'))


first_student = Student('Ruoy', 'Eman')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Portal construction']


second_student = Student('Stanford', 'Pines')
second_student.courses_in_progress += ['Portal construction']
second_student.courses_in_progress += ['Python']


first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Portal construction']

first_lecturer = Lecturer('Some', 'Buddy')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Portal construction']

second_lecturer = Lecturer('Bill', 'Cipher')
second_lecturer.courses_attached += ['Portal construction']
second_lecturer.courses_attached += ['Python']

second_reviewer = Reviewer('Bill', 'Cipher')
second_reviewer.courses_attached += ['Portal construction']
second_reviewer.courses_attached += ['Python']

print(second_reviewer.__str__())
print(first_reviewer.__str__())

first_student.rate_lecture(first_lecturer, 'Python', 1)
first_student.rate_lecture(first_lecturer, 'Portal construction', 2)

first_student.rate_lecture(second_lecturer, 'Python', 3)
first_student.rate_lecture(second_lecturer, 'Portal construction', 4)

second_student.rate_lecture(first_lecturer, 'Python', 5)
second_student.rate_lecture(first_lecturer, 'Portal construction', 6)

second_student.rate_lecture(second_lecturer, 'Python', 10)
second_student.rate_lecture(second_lecturer, 'Portal construction', 10)

first_student.rate_lecture(first_lecturer, 'Python', 9)
first_student.rate_lecture(first_lecturer, 'Portal construction', 10)

first_student.rate_lecture(second_lecturer, 'Python', 9)
first_student.rate_lecture(second_lecturer, 'Portal construction', 8)

second_student.rate_lecture(first_lecturer, 'Python', 7)
second_student.rate_lecture(first_lecturer, 'Portal construction', 6)

second_student.rate_lecture(second_lecturer, 'Python', 10)
second_student.rate_lecture(second_lecturer, 'Portal construction', 10)

print(first_lecturer.__str__())
print(second_lecturer.__str__())

first_reviewer.rate_hw(first_student, 'Python', 1)
first_reviewer.rate_hw(first_student, 'Portal construction', 2)

first_reviewer.rate_hw(second_student, 'Python', 3)
first_reviewer.rate_hw(second_student, 'Portal construction', 4)

second_reviewer.rate_hw(first_student, 'Python', 5)
second_reviewer.rate_hw(first_student, 'Portal construction', 6)

second_reviewer.rate_hw(second_student, 'Python', 10)
second_reviewer.rate_hw(second_student, 'Portal construction', 10)

first_reviewer.rate_hw(first_student, 'Python', 5)
first_reviewer.rate_hw(first_student, 'Portal construction',6)

first_reviewer.rate_hw(second_student, 'Python', 7)
first_reviewer.rate_hw(second_student, 'Portal construction', 9)

second_reviewer.rate_hw(first_student, 'Python', 5)
second_reviewer.rate_hw(first_student, 'Portal construction', 9)

second_reviewer.rate_hw(second_student, 'Python', 10)
second_reviewer.rate_hw(second_student, 'Portal construction', 10)

print(first_student.__str__())
print(second_student.__str__())

print(averege_score_homework([first_student, second_student], 'Portal construction'))
print(averege_score_homework([first_student, second_student], 'Python'))
print(averege_score_courses([first_lecturer, second_lecturer], 'Portal construction'))
print(averege_score_courses([first_lecturer, second_lecturer], 'Python'))
print(first_student.best_students(second_student))
print(first_lecturer.best_lecturer(second_lecturer))