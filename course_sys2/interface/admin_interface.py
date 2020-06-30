from db import models


# 注册接口
def register_interface(user, password):
    user_obj = models.Admin.select(user)
    # 存在用户则重新输入
    if user_obj:
        return False, "用户名已存在，请重新输入"
    # 不存在该用户则创建admin
    models.Admin(user, password)
    return True, f"[{user}] 注册成功"





# 创建学校接口
def create_school_interface(admin_name, school_name, school_adr):
    school_obj = models.School.select(school_name)
    if school_obj:
        return False, "该学校已存在，请重新输入"
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(school_name, school_adr)
    return True, f"[{school_name}]学校注册成功！"


def create_course_interface(online_user, school_name, name, period, price):
    school_obj = models.School.select(school_name)
    if not school_obj:
        return False, "学校不存在，请重新输入"
    course_obj = models.Course.select(name)
    if course_obj:
        return False, "课程已存在，请重新输入"
    admin_obj = models.Admin.select(online_user)
    admin_obj.create_course(name, period, price)
    school_obj.add_course(name)
    return True, f"注册[{name}]课程成功，所属学校为[{school_name}]"


def create_teacher_interface(online_user, school_name, name, age, gender, salary, level):
    school_obj = models.School.select(school_name)
    teacher_obj = models.Teacher.select(name)
    if teacher_obj:
        return False, "该老师已存在，请重新输入"
    admin_obj = models.Admin.select(online_user)
    admin_obj.create_teacher(name, age, gender, salary, level)
    school_obj.add_teacher(name)
    return True, f"[{name}]老师登记成功，所属学校为[{school_name}]"
