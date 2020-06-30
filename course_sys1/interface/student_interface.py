from db import modules
from lib import common


# 注册接口
# 5. 创建学员时，选择学校，关联班级
def register_interface(user_name, password, school_name):
    user_obj = modules.Student.select(user_name)
    if user_obj:
        return False, "用户名已存在,请重新输入"
    password = common.encrypt(password)
    modules.Student(user_name, password, school_name)
    user_obj = modules.Student.select(user_name)
    if user_obj:
        return True, "[{}]注册成功".format(user_name)
    else:
        return False, "输入的学校名不存在,无法注册,请重新输入"
    # logger.info('{}注册'.format(user_name))


# 登录接口
def login_interface(user, password):
    user_obj = modules.Student.select(user)
    if not user_obj:
        return False, "用户名不存在,请重新输入"
    password = common.encrypt(password)
    if user_obj.password == password:
        # logger.info('{}登录'.format(user))
        return True, "登陆成功"
    else:
        return False, "密码错误,请重新输入"


def charge_interface(user, money):
    user_obj = modules.Student.select(user)
    money = float(money)
    user_obj.balance += money
    user_obj.save()
    return "充值成功,现有金额:[{}]".format(user_obj.balance)


def choose_class_interface(user, class_name):
    class_obj = modules.Class.select(class_name)
    if not class_obj:
        return False, "输入的班级不存在,请重新输入"
    user_obj = modules.Student.select(user)
    result = user_obj.relate_class(class_obj)
    if result is None:
        return False, "当前输入的班级已选择,请重新输入"
    return True, "[{}]选择[{}]班级成功".format(user, class_name)
