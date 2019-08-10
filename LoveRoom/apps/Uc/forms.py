"""
file：forms.py
author：陈先生
date：2019/8/417:54
blog:https://chenpb-lu.github.io
"""
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.hashers import check_password as auth_check_password

class RegisterForm(forms.ModelForm):
    mobile_captcha = forms.CharField(label="验证码", widget=widgets.TextInput(
        attrs={'type':"text", 'class':"kapkey" ,'maxlength':"6" ,'placeholder':"验证码",'style':{'backgroud':'white !important'} }))
    password1 = forms.CharField(widget=widgets.TextInput(attrs={'type':"text", 'class':"password1", 'maxlength':"16", 'autocomplete':"off", 'placeholder':"密码"}))
    class Meta:
        model = User
        fields = ['mobile', 'password']
        widgets = {
            'mobile': widgets.TextInput(attrs={'type':"text", 'class':"phone", 'maxlength':"11", 'placeholder':"手机号码" ,'style':{'backgroud':'white !important'}}),
            'password': widgets.PasswordInput(attrs={'type':"password", 'class':"password", 'maxlength':"16", 'autocomplete':"off", 'placeholder':"密码"}),
        }

    def clean_mobile(self):
        ret = User.objects.filter(mobile=self.cleaned_data.get("mobile"))
        if not ret:
            return self.cleaned_data.get("mobile")
        else:
            raise ValidationError("手机号已绑定")

    def clean_password(self):
        data = self.cleaned_data.get("password")
        if not data.isdigit():
            return self.cleaned_data.get("password")
        else:
            raise ValidationError("密码不能全是数字")


class PhoneLoginForm(forms.Form):
    # 因为是登录功能，所以不适合ModelForm。
    # ModelForm对于unique字段会检查是否已经存在，如果存在，is_valid结果会为False


    mobile_captcha_login = forms.CharField(label="验证码", widget=widgets.TextInput(
        attrs={'type':"text", 'class':"kapkey_login" ,'maxlength':"6" ,'placeholder':"验证码",'style': {'backgroud': 'white !important'}
               }))
    mobile_login = forms.CharField(label="手机",widget=widgets.TextInput(
        attrs={"type": "text", "class": "phone_login", "maxlength":"11", "placeholder":"手机号码",
                       'style': {'backgroud': 'white !important'}}
    ))


    def clean_phone(self):

        ret = User.objects.filter(mobile=self.cleaned_data.get("mobile_login"))
        print(ret)
        if ret:
            return self.cleaned_data.get("mobile_login")
        else:
            raise ValidationError("用户名或密码不正确")


class PwLoginForm(forms.Form):
    # 因为是登录功能，所以不适合ModelForm。
    # ModelForm对于unique字段会检查是否已经存在，如果存在，is_valid结果会为False

    password1_login = forms.CharField(widget=widgets.TextInput(
        attrs={'type': "text", 'class': "password1N", 'maxlength': "16", 'autocomplete': "off", 'placeholder': "密码"}))

    password_login = forms.CharField(widget=widgets.TextInput(
        attrs={'type': "password", 'class': "passwordN", 'maxlength': "16", 'autocomplete': "off", 'placeholder': "密码"}))

    mobile_pwlogin = forms.CharField(label="手机",widget=widgets.TextInput(
        attrs={"type": "text", "class": "username", "maxlength":"11", "placeholder":"手机号码",
                       'style': {'backgroud': 'white !important'}}
    ))


    def check_password(self):
        print('check password')
        mobile = self.cleaned_data['mobile_pwlogin']
        password = self.cleaned_data['password_login']
        try:
            user = User.objects.get(mobile=mobile)
            print(user.username)
            return user, auth_check_password(password, user.password)
        except:
            return None, False


