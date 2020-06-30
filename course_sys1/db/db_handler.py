import os
import pickle
from conf import settings


def save(obj):
    dir_path = os.path.join(settings.DB_PATH, obj.__class__.__name__)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    data_path = os.path.join(dir_path, obj.name)
    with open(data_path, "wb") as f:
        pickle.dump(obj, f)


def select(cls, user_name):
    user_path = os.path.join(settings.DB_PATH, cls.__name__, user_name)
    if os.path.exists(user_path):
        with open(user_path, "rb") as f:
            obj = pickle.load(f)
            return obj

