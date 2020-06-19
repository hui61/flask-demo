from functools import wraps

from flask import session, redirect


def login_validate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("user_id"):
            result = func(*args, **kwargs)
            return result
        else:
            return redirect("/")

    return wrapper


def admin_validate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_role') == 1:
            result = func(*args, **kwargs)
            return result
        else:
            return

    return wrapper
