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
            return f'{student} делает домашнюю работу лучше чем {self}'
        else:
            return f'{self} делает домашнюю работу лучше чем {student}'




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
            return f'{lecturer} ведет занятия лучше чем {self}'
        else:
            return f'{self} ведет занятия лучше чем {lecturer}'

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
        print('Фамилия: ', self.surname)


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
            if course in courses:
                score += sum(grade) / (len(grade) * len(student_list))
                # find_course = True
    return (f'средняя оценка за домашнее задание на курсе {course} - {round(score / len(student.grades))}')

def averege_score_courses(lecturer_list, course):
    # find_course = False
    score = 0
    for lecturer in lecturer_list:
        for courses, grade in lecturer.grades.items():
            if course in courses:
                score += sum(grade) / (len(grade) * len(lecturer_list))
                # find_course = True
    return (f'средняя оценка за домашнее задание на курсе {course} - {round(score / len(lecturer.grades))}')


first_student = Student('Ruoy', 'Eman')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Portal construction']


second_student = Student('Stanford', 'Pines')
second_student.courses_in_progress += ['Portal construction']
second_student.courses_in_progress += ['Python']


first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python']

first_lecturer = Lecturer('Some', 'Buddy')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Bill', 'Cipher')
second_lecturer.courses_attached += ['Portal construction']

second_reviewer = Reviewer('Bill', 'Cipher')
second_reviewer.courses_attached += ['Portal construction']

