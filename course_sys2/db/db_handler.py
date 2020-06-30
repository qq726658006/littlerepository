import os
import pickle
from conf import settings


def select(cls, user_name):
    user_dir = os.path.join(settings.DB_PATH, cls.__name__)
    if not os.path.exists(user_dir):
        os.mkdir(user_dir)
    user_file = os.path.join(user_dir, user_name)
    if os.path.exists(user_file):
        with open(user_file, "rb") as f:
            user_obj = pickle.load(f)
            return user_obj


def save(obj):
    user_dir = os.path.join(settings.DB_PATH, obj.__class__.__name__)
    if not os.path.exists(user_dir):
        os.mkdir(user_dir)
    user_file = os.path.join(user_dir, obj.name)
    with open(user_file, "wb") as f:
        pickle.dump(obj, f)
