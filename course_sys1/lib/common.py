import hashlib


def encrypt(password):
    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    salt = "我真帅"
    md5.update(salt.encode("utf-8"))
    res = md5.hexdigest()
    return res


def admin_identify(func):
    def wrapper(*args, **kwargs):
        from core import admin
        if admin.online_user:
            res = func(*args, **kwargs)
            return res
        else:
            print("请先登录")

    return wrapper


def student_identify(func):
    def wrapper(*args, **kwargs):
        from core import student
        if student.online_user:
            res = func(*args, **kwargs)
            return res
        else:
            print("请先登录")

    return wrapper


def teacher_identify(func):
    def wrapper(*args, **kwargs):
        from core import teacher
        if teacher.online_user:
            res = func(*args, **kwargs)
            return res
        else:
            print("请先登录")

    return wrapper
