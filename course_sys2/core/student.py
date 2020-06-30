from interface import student_interface
from interface import common_interface
from lib import common
online_user = {}
# 6.1 学员视图， 可以注册，选择校区， 选择班级，
# 登录
def login():
    while 1:
        print("登录功能执行中")
        user_name = input("请输入姓名:[温馨提示:输入q退出]")
        if user_name.lower() == "q":
            break
        password = input("请输入密码:")
        flag, msg = common_interface.login_interface("student",user_name, password)
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
        flag, msg = student_interface.register_interface(user_name,password1)
        print(msg)
        if flag is True:
            break





# 选择校区
@common.identify("student")
def choose_school():
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
        flag,msg = student_interface.choose_school_interface(online_user["name"],school_name)
        print(msg)
        if flag is True:
            break


# 选择班级
@common.identify("student")
def choose_class():
    while 1:
        class_list = student_interface.show_class(online_user["name"])
        if class_list is None:
            print("请先选择学校")
            return
        if not class_list:
            print("当前学校无课程,请联系管理员创建")
            return
        for index, class_name in enumerate(class_list):
            print(f"编号:[{index}]        课程名:[{class_name}]")
        class_index = input("请输入选择的班级").strip()
        if class_index.lower() == "q":
            break
        if not class_index.isdigit():
            print("请输入数字!")
            continue
        class_index = int(class_index)
        if class_index not in range(len(class_list)):
            print("编号不存在!")
            continue
        class_name = class_list[class_index]
        flag,msg = student_interface.choose_class_interface(online_user["name"],class_name)
        print(msg)
        if flag is True:
            break
# 查看成绩
@common.identify("student")
def show_score():
    score_dic = student_interface.show_score(online_user["name"])
    print(score_dic)


func_dic = {
    "0": ["注册", register],
    "1": ["登录", login],
    "2": ["选择校区", choose_school],
    "3": ["选择班级", choose_class],
    "4":["查看成绩",show_score],
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
    global online_user
    online_user = {}