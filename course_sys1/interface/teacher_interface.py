from db import modules
from lib import common

online_user = None


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
