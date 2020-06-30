import os
from conf import settings
from db import models

# 登陆接口
# 登录接口
def login_interface(role,user_name, password):
    if role == "admin":
        user_obj = models.Admin.select(user_name)
    # 存在用户则重新输入
    elif role == "student":
        user_obj = models.Student.select(user_name)
    elif role == "teacher":
        user_obj = models.Teacher.select(user_name)
    else:
        return False, "当前身份无法登陆"
    if not user_obj:
        return False, "用户名不存在，请重新输入"
    if user_obj.password == password:
        return True, "登录成功"
    return False, "密码错误，请重新输入"





def show_all_school():
    school_path = os.path.join(settings.DB_PATH, "School")
    school_list = os.listdir(school_path)
    return school_list

def show_classes(school_name):
    school_obj = models.School.select(school_name)
    return school_obj.course_list

def show_all_class():
    class_path = os.path.join(settings.DB_PATH, "Course")
    class_list = os.listdir(class_path)
    return class_list