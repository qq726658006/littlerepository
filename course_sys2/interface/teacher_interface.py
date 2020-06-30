
from db import models

def check_class_interface(user):
    teacher_obj = models.Teacher.select(user)
    return teacher_obj.show_course()


def add_class_interface(online_user,class_name):
    teacher_obj = models.Teacher.select(online_user)
    course_list = teacher_obj.show_course()
    if class_name in course_list:
        return False,"该课程已添加"
    teacher_obj.add_course(class_name)
    return True,f"课程[{class_name}]添加成功"


def check_class_member_interface(class_name):
    class_obj = models.Course.select(class_name)
    student_list = class_obj.show_student
    return student_list


def modify_score_interface(online_user,class_name,student_name,score):
    tea_obj = models.Teacher.select(online_user)
    tea_obj.motify_score(class_name,student_name,score)
    return "修改成绩成功"


