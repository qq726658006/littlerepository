from interface import student_interface
from lib import common
online_user = None
# 6.1 学员视图， 可以注册， 交学费， 选择班级，
# 登录
def login():
    while 1:
        print("登录功能执行中")
        user_name = input("请输入姓名:[温馨提示:输入q退出]")
        if user_name.lower() == "q":
            break
        password = input("请输入密码:")
        flag, msg = student_interface.login_interface(user_name, password)
        if flag is False:
            print(msg)
            continue
        if flag is True:
            print(msg)
            global online_user
            online_user = user_name
            break
        pass


# 注册
def register():
    while 1:
        print("===============注册功能执行中")
        user_name = input("请输入用户名:[温馨提示:输入q退出]")
        if user_name.lower() == "q":
            break
        password1 = input("请输入密码:")
        password2 = input("请确认密码:")
        if password1 != password2:
            print("两次密码不一致")
            continue
        school_name = input("请输入选择的学校:")
        flag, msg = student_interface.register_interface(user_name, password1,school_name)
        print(msg)
        if flag is True:
            break



@common.student_identify
def charge():
    while 1:
        money = input("请输入缴费金额").strip()
        if money.lower() == "q":
            break
        if not money.isdigit():
            print("只能输入数字")
            continue
        msg = student_interface.charge_interface(online_user,money)
        print(msg)
        break

@common.student_identify
def choose_class():
    while 1:
        class_name = input("请输入选择的班级").strip()
        if class_name.lower() == "q":
            break
        flag,msg = student_interface.choose_class_interface(online_user,class_name)
        print(msg)
        if flag is True:
            break


func_dic = {
    "0": ["注册", register],
    "1": ["登录", login],
    "2": ["交学费", charge],
    "3": ["选择班级", choose_class],
    # "4":["",],
    # "5":["",],
}


def student_view():
    while True:
        for num, func_list in func_dic.items():
            print(f"[{num}]     [{func_list[0]}]")
        choice = input('请选择功能编号: ').strip()
        if choice.lower() == "q":
            break
        if choice not in func_dic:
            print("编号不存在,请输入正确的编号")
            continue
        func_dic[choice][1]()
