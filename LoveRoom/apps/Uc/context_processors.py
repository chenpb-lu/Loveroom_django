"""
file：context_processors.py
author：陈先生
date：2019/8/512:57
blog:https://chenpb-lu.github.io
"""
from .forms import RegisterForm,PhoneLoginForm,PwLoginForm
def regform(request):
    form = RegisterForm()
    return {"form": form}
def phform(request):
    phone_login_form = PhoneLoginForm()
    return {"phone_login_form":phone_login_form}

def pwform(request):
    pw_login_form = PwLoginForm()
    return {"pw_login_form":pw_login_form}