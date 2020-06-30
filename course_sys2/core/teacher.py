from interface import teacher_interface
from interface import common_interface
from lib import common

# 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级，
# 查看班级学员列表 ， 修改所管理的学员的成绩
online_user = {}


def login():
    while 1:
        print("登录1功能执行中")
        user_name = input("请输入姓名:[温馨提示:输入q退出]")
        if user_name.lower() == "q":
            break
        password = input("请输入密码:")
        flag, msg = common_interface.login_interface("teacher", user_name, password)
        if flag is False:
            print(msg)
            continue
        if flag is True:
            print(msg)
            global online_user
            online_user["name"] = user_name
            break


# 查看教授课程
@common.identify("teacher")
def check_class():
    class_list = teacher_interface.check_class_interface(online_user["name"])
    if not class_list:
        print("无教授课程")
        return
    print(class_list)


# 选择教授课程
@common.identify("teacher")
def choose_class():
    while 1:
        class_list = common_interface.show_all_class()
        if not class_list:
            print("无课程,请联系管理员添加课程")
        for index, course in enumerate(class_list):
            print(f"编号:[{index}]    课程:[{course}]")
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
        flag, msg = teacher_interface.add_class_interface(online_user["name"], class_name)
        print(msg)
        if flag is True:
            break


# 查看课程下学生
@common.identify("teacher")
def check_class_member():
    while 1:
        class_list = teacher_interface.check_class_interface(online_user["name"])
        if not class_list:
            print("无课程,请联系管理员添加课程")
        for index, course in enumerate(class_list):
            print(f"编号:[{index}]    课程:[{course}]")
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

        student_list = teacher_interface.check_class_member_interface(class_name)
        if not student_list:
            print("没有学生选择该课程")
            return
        print(student_list)
        break


# 修改学生分数
@common.identify("teacher")
def modify_score():
    while 1:
        class_list = teacher_interface.check_class_interface(online_user["name"])
        if not class_list:
            print("无课程,请联系管理员添加课程")
        for index, course in enumerate(class_list):
            print(f"编号:[{index}]    课程:[{course}]")
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
        student_list = teacher_interface.check_class_member_interface(class_name)
        for index,student in enumerate(student_list):
            print(f"编号:[{index}]     姓名:[{student}]")
        student_index = input("请选择学生:")
        if not student_index.isdigit():
            print("请输入数字!")
            continue
        student_index = int(student_index)
        if student_index not in range(len(student_list)):
            print("编号不存在!")
            continue
        student_name = student_list[student_index]
        score = input("请输入成绩:")
        msg = teacher_interface.modify_score_interface(online_user["name"],class_name,student_name,score)
        print(msg)
        return


func_dic = {
    # "0":["注册",],
    "1": ["登录", login],
    "2": ["查看教授班级", check_class],
    "3": ["选择上课班级", choose_class],
    "4": ["查看班级成员", check_class_member],
    "5": ["修改学员成绩", modify_score],
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
    global online_user
    online_user = {}
