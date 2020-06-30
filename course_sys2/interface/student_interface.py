from db import models


def register_interface(user_name, password):
    stu_obj = models.Student.select(user_name)
    if stu_obj:
        return False, "用户名已存在,请重新输入"
    models.Student(user_name, password)
    return True, "注册成功"


def choose_school_interface(name, school_name):
    stu_obj = models.Student.select(name)
    if stu_obj.school:
        return False, "用户名已选择学校"
    stu_obj.choose_school(school_name)
    return True, f"选择[{school_name}]成功"


def show_class(name):
    stu_obj = models.Student.select(name)
    if stu_obj.school:
        school_obj = models.School.select(stu_obj.school)
        return school_obj.course_list


def choose_class_interface(name, class_name):
    stu_obj = models.Student.select(name)
    if class_name in stu_obj.courses:
        return False, "已选择过该课程"
    class_obj = models.Course.select(class_name)
    class_obj.add_student(name)
    stu_obj.add_course(class_name)
    return True, f"选择[{class_name}]课程成功"


def show_score(name):
    stu_obj = models.Student.select(name)
    if not stu_obj.score_dict:
        return "还没选课"
    return stu_obj.score_dict
