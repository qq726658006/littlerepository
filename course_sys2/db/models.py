from db import db_handler


class Base:
    @classmethod
    def select(cls, user_name):
        obj = db_handler.select(cls, user_name)
        return obj

    def save(self):
        db_handler.save(self)


class Admin(Base):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.save()

    def create_school(self, school_name, school_adr):
        School(school_name, school_adr)

    def create_course(self, name, period, price):
        Course(name, period, price)

    def create_teacher(self, name, age, gender, salary, level):
        Teacher(name, age, gender, salary, level)


class School(Base):
    def __init__(self, name, adr):
        self.name = name
        self.adr = adr
        self.course_list = []
        self.teacher_list = []
        self.save()

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.save()

    def add_teacher(self, teacher_name):
        self.teacher_list.append(teacher_name)
        self.save()


class Student(Base):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.courses = []
        self.school = None
        self.score_dict = {}
        self.save()

    def choose_school(self, school_name):
        self.school = school_name
        self.save()

    def add_course(self, class_name):
        self.courses.append(class_name)
        self.score_dict[class_name] = 0
        self.save()

    pass


class Course(Base):
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price
        self.student_list = []
        self.save()

    def add_student(self, stu_name):
        self.student_list.append(stu_name)
        self.save()
    def show_student(self):
        return self.student_list



class Teacher(Base):
    def __init__(self, name, age, gender, salary, level):
        self.name = name
        self.password = "123"
        self.age = age
        self.gender = gender
        self.salary = salary
        self.level = level
        self.course_list = []
        self.save()

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.save()

    def motify_score(self, class_name, student_name, score):
        stu_obj = Student.select(student_name)
        stu_obj.score_dict[class_name] = score
        stu_obj.save()

    def show_course(self):
        return self.course_list
