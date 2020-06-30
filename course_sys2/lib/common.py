'''
装饰器
'''

def identify(role):
    def deco(func):
        def wrapper(*args, **kwargs):
            from core import admin, student, teacher
            if role == "admin":
                if not admin.online_user:
                    print("请先登录")
                    admin.login()
                    return
            elif role == "student":
                if not student.online_user:
                    print("请先登录")
                    student.login()
                    return
            elif role == "teacher":
                if not teacher.online_user:
                    print("请先登录")
                    teacher.login()
                    return
            res = func(*args, **kwargs)
            return res

        return wrapper

    return deco



