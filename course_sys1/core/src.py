from core import admin
from core import student
from core import teacher

id_dic = {
    "1": ["管理员", admin.admin_view],
    "2": ["学员", student.student_view],
    "3": ["教师", teacher.teacher_view],
}


def run():
    while True:
        for num, func_list in id_dic.items():
            print(f"[{num}]     [{func_list[0]}]")
        choice = input('请输入您的身份对应的编号: ').strip()
        if choice.lower() == "q":
            break
        if choice not in id_dic:
            print("编号不存在,请输入正确的编号")
            continue
        id_dic[choice][1]()
