import pickle
import uuid
from db import db_handler


class Base:
    def save(self):
        db_handler.save(self)

    @classmethod
    def select(cls, user_name):
        obj = db_handler.select(cls, user_name)
        return obj


class Admin(Base):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.save()


# 学校
# 	- 数据
# 		- 学校名
# 	- 功能
# 		- 创建课程
# 		- 创建班级
class School(Base):
    def __init__(self, name):
        self.name = name
        self.uuid = uuid.uuid4()
        self.classes = []
        self.courses = []
        self.save()

    def create_course(self, name, period, price):
        course_obj = Course(name, period, price)
        self.courses.append(course_obj)
        self.save()

    def create_class(self, name):
        class_obj = Class(name)
        self.classes.append(class_obj)
        self.save()

    pass


# 课程
# 	- 数据
# 	- 功能
class Course(Base):
    # 课程包含，周期，价格，通过学校创建课程
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price
        self.uuid = uuid.uuid4()
        self.save()


# 班级
# 	- 数据
# 	- 功能
# 		- 关联课程
# 		- 关联讲师
class Class(Base):
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.teachers = []
        self.uuid = uuid.uuid4()
        self.save()

    def relate_course(self, course_obj):
        self.courses.append(course_obj)
        self.save()

    def relate_teacher(self, teacher_obj):
        self.teachers.append(teacher_obj)
        self.save()


# 学员
# 	- 数据
# 	- 功能
# 		- 选择学校
# 		- 关联班级
class Student(Base):
    def __init__(self, name, password, school_name):
        self.school = None
        self.choose_school(school_name)
        self.name = name
        self.password = password
        self.classes = []
        self.balance = 0
        if self.school is None:
            return
        self.save()

    def choose_school(self, school_name):
        school_obj = db_handler.select(School, school_name)
        if school_obj:
            self.school = school_obj

    def relate_class(self, class_obj):
        if class_obj in self.classes:
            return
        self.classes.append(class_obj)
        self.save()
        return True


# 讲师
# 	- 数据
# 	- 功能
# 		- 关联学校
class Teacher(Base):
    # 创建讲师角色时要关联学校，
    def __init__(self, name, age, gender, salary, level,school_name):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        self.level = level
        self.password = 123
        self.classes = []
        school_obj = db_handler.select(School, school_name)
        self.school = school_obj
        if self.school is None:
            return
        self.save()



