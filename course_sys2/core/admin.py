from interface import admin_interface
from interface import common_interface
from lib import common

online_user = {}


# 6.3 管理视图，创建讲师， 创建班级，创建课程
# 登录

def login():
    while 1:
        print("==========登录功能执行中")
        user_name = input("请输入用户名:[温馨提示:输入q退出]")
        if user_name.lower() == "q":
            break
        password = input("请输入密码:")
        flag, msg = common_interface.login_interface("admin",user_name, password)
        print(msg)
        if flag is True:
            online_user["name"] = user_name
            break


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
        flag, msg = admin_interface.register_interface(user_name, password2)
        print(msg)
        if flag is True:
            break


@common.identify("admin")
def create_school():
    while 1:
        name = input("请输入要创建的学校名:[温馨提示:输入q退出]")
        if name.lower() == "q":
            break
        adr = input("请输入要创建的学校地址")
        flag, msg = admin_interface.create_school_interface(online_user["name"], name, adr)
        print(msg)
        if flag is True:
            break


@common.identify("admin")
def create_course():
    while 1:
        school_list = common_interface.show_all_school()
        for index,school_name in enumerate(school_list):
            print(f"编号:[{index}]        学校名:[{school_name}]")
        school_index = input("请输入选择的学校的编号:[温馨提示:输入q退出]")
        if school_index.lower() == "q":
            break
        if not school_index.isdigit():
            print("请输入数字!")
            continue
        school_index = int(school_index)
        if school_index not in range(len(school_list)):
            print("编号不存在!")
            continue
        school_name = school_list[school_index]
        name = input("请输入要创建的课程名:")
        period = input("请输入课程周期:")
        price = input("请输入课程价格:")
        if not price.isdigit():
            print("课程价格请输入数字")
            continue
        flag, msg = admin_interface.create_course_interface(online_user["name"], school_name, name, period, price)
        print(msg)
        if flag is True:
            break


@common.identify("admin")
def create_teacher():
    while 1:
        school_list = common_interface.show_all_school()
        for index, school in enumerate(school_list):
            print(f'编号: {index}    学校名: {school}')
        school_index = input("请输入班级所属学校的编号:[温馨提示:输入q退出]")
        if school_index.lower() == "q":
            break
        if not school_index.isdigit():
            print("请输入数字")
            continue
        school_index = int(school_index)
        if school_index not in range(len(school_list)):
            print("请输入正确的编号")
            continue
        name = input("请输入新增教师的姓名:")
        age = input("请输入教师年龄:")
        if not age.isdigit():
            print("年龄请输入数字")
            continue
        gender = input("请输入教师性别:")
        salary = input("请输入教师薪资:")
        if not salary.isdigit():
            print("年龄请输入数字")
            continue
        level = input("请输入教师等级:")
        if not level.isdigit():
            print("年龄请输入数字")
            continue
        flag, msg = admin_interface.create_teacher_interface(online_user["name"], school_list[school_index], name, age,
                                                             gender, salary, level)
        print(msg)
        if flag is True:
            break


func_dic = {
    "0": ["注册", register],
    "1": ["登录", login],
    "2": ["创建学校", create_school],
    "3": ["创建课程", create_course],
    "4": ["创建讲师", create_teacher],
}


def admin_view():
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
    global online_user
    online_user = {}
