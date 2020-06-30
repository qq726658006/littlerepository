# import logging.config
from db import modules
from lib import common


# from conf import settings


# logging.config.dictConfig(settings.LOGGING_DIC)
# logger = logging.getLogger('user')

# 注册接口
def register_interface(user_name, password):
    user_obj = modules.Admin.select(user_name)
    if user_obj:
        return False, "用户名已存在,请重新输入"
    else:
        password = common.encrypt(password)
        modules.Admin(user_name, password)
        return True, "注册成功"
    # logger.info('{}注册'.format(user_name))


# 登录接口
def login_interface(user, password):
    user_obj = modules.Admin.select(user)
    if not user_obj:
        return False, "用户名不存在,请重新输入"
    password = common.encrypt(password)
    if user_obj.password == password:
        # logger.info('{}登录'.format(user))
        return True, "登陆成功"
    else:
        return False, "密码错误,请重新输入"


def check_school(school_name):
    school_obj = modules.School.select(school_name)
    if school_obj:
        return True, ""
    return False, "学校不存在,请重新输入"


def create_school_interface(name):
    school_obj = modules.School.select(name)
    if school_obj:
        return False, "该学校已存在,请重新输入"
    else:
        modules.School(name)
        return True, "注册学校:[{}]成功".format(name)


def create_teacher_interface(name, age, gender, salary, level):
    user_obj = modules.Admin.select(name)
    if user_obj:
        return False, "用户名已存在,请重新输入"
    else:
        modules.Teacher(name, age, gender, salary, level)
        return True, "注册成功"


def create_class_interface(class_name, school_name):
    # 通过学校创建班级， 班级关联课程、讲师
    class_obj = modules.Class.select(class_name)
    if class_obj:
        return False, "用户名已存在,请重新输入"
    else:
        school_obj = modules.School.select(school_name)
        school_obj.create_class(class_name)
        return True, "注册班级[{}]成功".format(class_name)


def create_course_interface(school_name, course_name, period, price):
    course_obj = modules.Course.select(course_name)
    if course_obj:
        return False, "该课程已存在,请重新输入"
    else:
        school_obj = modules.School.select(school_name)
        school_obj.create_course(course_name, period, price)
        return True, "注册课程:[{}]成功".format(course_name)
