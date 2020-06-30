from interface import teacher_interface
from lib import common

# 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级，
# 查看班级学员列表 ， 修改所管理的学员的成绩
online_user = None


def login():
    while 1:
        print("登录功能执行中")
        user_name = input("请输入姓名:[温馨提示:输入q退出]")
        if user_name.lower() == "q":
            break
        password = input("请输入密码:")
        flag, msg = teacher_interface.login_interface(user_name, password)
        if flag is False:
            print(msg)
            continue
        if flag is True:
            print(msg)
            global online_user
            online_user = user_name
            break
        pass


@common.teacher_identify
def class_manage():
    pass


@common.teacher_identify
def choose_to_class():
    pass


@common.teacher_identify
def check_class_member():
    pass


@common.teacher_identify
def modify_score():
    pass


func_dic = {
    # "0":["注册",],
    "1": ["登录", login],
    "2": ["管理班级", class_manage],
    "3": ["选择上课班级", choose_to_class],
    "4": ["查看班级成员", check_class_member()],
    "5": ["修改学员成绩", modify_score()],
}


def teacher_view():
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
