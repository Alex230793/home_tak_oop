class Student:

    def __init__(self, name, surname, gender):
        self.name = name  # имя
        self.surname = surname  # фамилия
        self.gender = gender  # пол
        self.finished_courses = []  # законченные курсы
        self.courses_in_progress = []  # курс который изучается
        self.grades = {}  # оценки за курс

    def rate_hw_stud(self, lecturer, course, lecturer_score): # оценки которые ставят студенты лекторам
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecturer_scores:
                lecturer.lecturer_scores[course] += [lecturer_score]
            else:
                lecturer.lecturer_scores[course] = [lecturer_score]
        else:
            return 'Ошибка'


    def sum_grad_student(grade): # подсчет средней оценки студента
        for key, value in grade.items():
            sum_grad_stud = sum(value) / len(value)
            return sum_grad_stud


    def __lt__(self, best_stud): # функция сравнения студентов по среднему баллу
        if not isinstance(best_stud, Student):
            print('Не получается сравнить')
            return
        return Student.sum_grad_student(self.grades) <= Student.sum_grad_student(best_stud.grades)



    def __str__(self): # принт для студентов
        mid_grad_st = Student.sum_grad_student(self.grades)
        stud_print = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {mid_grad_st}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return stud_print

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # курс который проводит учитель


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # self.courses_attached = []
        self.lecturer_scores = {}  # оценки студенов за лекции преподавателям


    def sum_grad_lecturer(scores): # подсчет средней оценки лектора за проведение лекций
        for key, value in scores.items():
            sum_grad_lect = sum(value) / len(value)
            return sum_grad_lect

    def __lt__(self, best_lect): # функция сравненния лекторов по среднему баллу
        if not isinstance(best_lect, Lecturer):
            print('Не получается сравнить')
            return
        return Lecturer.sum_grad_lecturer(self.lecturer_scores) <= Lecturer.sum_grad_lecturer(best_lect.lecturer_scores)

    def __str__(self): # принт для лекторов
        mid_grad_lect = Lecturer.sum_grad_lecturer(self.lecturer_scores)
        lect_print = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {mid_grad_lect}'
        return lect_print

class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw_rev(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



    def __str__(self): # принт для проверяющих
        rev_print = f'Имя: {self.name}\nФамилия: {self.surname}'
        return rev_print

# добавление и посчет средней оценки студентов
dikt_grades_student = []
# я подумал, зачем пребирать все элементы из списка относящегося к студенту, ели нам нужны только оценки
# проще срузу добавлять их в одельный список и считать
def dikt_append_stud_grad(student):
    for key, value in student.items():
        for grad in value:
            dikt_grades_student.append(grad)

def mid_grade_stud(dikt):
    mid_grade = sum(dikt_grades_student) / len(dikt_grades_student)
    return f'Средний бал всех студентов - {mid_grade}'

# тоже самое для преподавателей
dikt_lecturer_scores = []

def dikt_append_lect_grad(lecturer):
    for key, value in lecturer.items():
        for scores in value:
            dikt_lecturer_scores.append(scores)

def mid_scores_lect(dikt):
    mid_scores = sum(dikt_lecturer_scores) / len(dikt_lecturer_scores)
    return f'Средний бал преподавателей читающих лекции - {mid_scores}'





# Студенты
student_1 = Student('Alex', 'Netov', 'man')
student_1.courses_in_progress += ['Python']
student_2 = Student('Maks', 'Chester', 'man')
student_2.courses_in_progress += ['Python']

# Лекторы
lecturer_1 = Lecturer('Vlad', 'Morozov')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Ivan', 'Bragin')
lecturer_2.courses_attached += ['Python']

# Проверяющие
reviewer_1 = Reviewer('Petr', 'Pervui')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Petr', 'Vtoroi')
reviewer_2.courses_attached += ['Python']

# Оценки студентам
reviewer_2.rate_hw_rev(student_1, 'Python', 10)
reviewer_1.rate_hw_rev(student_1, 'Python', 9)
reviewer_2.rate_hw_rev(student_1, 'Python', 8)
reviewer_1.rate_hw_rev(student_1, 'Python', 10)

reviewer_2.rate_hw_rev(student_2, 'Python', 9)
reviewer_1.rate_hw_rev(student_2, 'Python', 9)
reviewer_2.rate_hw_rev(student_2, 'Python', 7)
reviewer_1.rate_hw_rev(student_2, 'Python', 10)


# оценки лекторам
student_1.rate_hw_stud(lecturer_1, 'Python', 10)
student_1.rate_hw_stud(lecturer_2, 'Python', 7)
student_1.rate_hw_stud(lecturer_1, 'Python', 9)
student_1.rate_hw_stud(lecturer_2, 'Python', 10)

student_2.rate_hw_stud(lecturer_1, 'Python', 9)
student_2.rate_hw_stud(lecturer_2, 'Python', 8)
student_2.rate_hw_stud(lecturer_1, 'Python', 10)
student_2.rate_hw_stud(lecturer_2, 'Python', 7)


dikt_append_stud_grad(student_1.grades)
dikt_append_stud_grad(student_2.grades)

dikt_append_lect_grad(lecturer_1.lecturer_scores)
dikt_append_lect_grad(lecturer_2.lecturer_scores)



print(student_1)
print()
print(student_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(reviewer_1)
print()
print(reviewer_2)
print()
print(mid_grade_stud(dikt_grades_student))
print(mid_scores_lect(dikt_lecturer_scores))

