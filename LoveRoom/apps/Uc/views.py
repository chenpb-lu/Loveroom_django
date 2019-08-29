from django.shortcuts import render,redirect, reverse
from django.views.generic import View
import logging
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from .models import User
from .forms import RegisterForm,PhoneLoginForm,PwLoginForm
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
logger = logging.getLogger('account')

# Create your views here.
class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "house/index.html")

    # Ajax提交表单
    def post(self, request):
        from django.core.cache import cache
        ret = {"status": 400, "msg": "调用方式错误"}
        if request.is_ajax():
            print(request.POST)
            form = RegisterForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data["password"]
                password1 = form.cleaned_data["password1"]
                print(f"{password}--{password1}")
                mobile = form.cleaned_data["mobile"]
                username = "手机用户" + mobile
                mobile_captcha = form.cleaned_data["mobile_captcha"]
                print(mobile_captcha)
                # print(username)
                mobile_captcha_reids = '123456'
                # mobile_captcha_reids = cache.get(mobile)
                if mobile_captcha == mobile_captcha_reids:
                    print("通过验证")
                    user = User.objects.create(username=username,mobile=mobile, password=make_password(password))
                    user.save()
                    ret['status'] = 200
                    ret['msg'] = "注册成功"
                    logger.debug(f"新用户{user.username}注册成功！")

                    user = auth.authenticate(username=username, password=password)
                    if user is not None and user.is_active:
                        auth.login(request, user)
                        logger.debug(f"新用户{user.username}登录成功")
                    else:
                        logger.error(f"新用户{username}登录失败")
                else:
                    # 验证码错误
                    ret['status'] = 401
                    ret['msg'] = "验证码错误或过期"
            else:
                ret['status'] = 402
                ret['msg'] = "该手机号已注册"
        logger.debug(f"用户注册结果：{ret}")
        return JsonResponse(ret)

class PhoneLogin(View):
    def get(self, request):
        # 如果已登录，则直接跳转到index页面
        # request.user 表示的是当前登录的用户对象,没有登录 `匿名用户`
        phone_login_form = PhoneLoginForm()
        if request.user.is_authenticated:
            return redirect(reverse('house:index'))
        # 设置下一跳转地址
        request.session["next"] =  request.GET.get('next',reverse('house:index'))
        return render(request, "house/index.html")

        # Form表单直接提交
    def post(self, request):
        # 表单数据绑定
        ret = {"status": 400, "msg": "调用方式错误"}
        phone_login_form = PhoneLoginForm(request.POST)
        if phone_login_form.is_valid():
            mobile = phone_login_form.cleaned_data["mobile_login"]
            mobile_captcha = phone_login_form.cleaned_data["mobile_captcha_login"]
            mobile_captcha_reids = '123456'
            # mobile_captcha_reids = cache.get(mobile)
            logger.debug(f"登录提交验证码:{mobile_captcha}-{mobile_captcha_reids}")
            # 验证码一致
            if mobile_captcha == mobile_captcha_reids:
                user = User.objects.get(mobile=mobile)
                # user = auth.authenticate(username=username, password=password)
                if user is not None and user.is_active :
                    auth.login(request, user)
                    ret['status'] = 200
                    ret['msg'] = "登录成功"
                    logger.info(f"{user.username}登录成功")
                else:
                    ret['status'] = 401
                    ret['msg'] = "该手机号未注册"
                    logger.error(f"{mobile}登录失败, 手机号未注册")
            else:
                ret['status'] = 402
                ret['msg'] = "验证码错误"
                logger.error(f"验证码错误")
        else:
            msg = "表单数据不完整"
            logger.error(phone_login_form.errors)
            logger.error(msg)
        return JsonResponse(ret)

class PwLogin(View):
    def get(self, request):
        # 如果已登录，则直接跳转到index页面
        # request.user 表示的是当前登录的用户对象,没有登录 `匿名用户`
        phone_login_form = PwLoginForm()
        if request.user.is_authenticated:
            return redirect(reverse('house:index'))
        # 设置下一跳转地址
        request.session["next"] =  request.GET.get('next',reverse('house:index'))
        return render(request, "house/index.html")

        # Form表单直接提交
    def post(self, request):
        # 表单数据绑定
        ret = {"status": 400, "msg": "调用方式错误"}
        pw_login_form = PwLoginForm(request.POST)
        if pw_login_form.is_valid():
            mobile = pw_login_form.cleaned_data["mobile_pwlogin"]
            password = pw_login_form.cleaned_data['password_login']
            password1 = pw_login_form.cleaned_data['password1_login']

            logger.debug(f"登录提交密码:{password}-{password1}")
            user, flag = pw_login_form.check_password()
            print(user.username)
            if user is not None and user.is_active and flag:
                if user is not None and user.is_active :
                    auth.login(request, user)
                    ret['status'] = 200
                    ret['msg'] = "登录成功"
                    logger.info(f"{user.username}登录成功")
            else:
                ret['status'] = 401
                ret['msg'] = "手机号或密码错误"
                logger.error(f"手机号或密码错误")
        else:
            msg = "表单数据不完整"
            logger.error(pw_login_form.errors)
            logger.error(msg)
        return JsonResponse(ret)


def logout(request):
    logger.info(f"{request.user.username}注销成功")
    auth.logout(request)
    return redirect(reverse("house:index"))

@login_required()
def change_passwd(request):
    return render(request,'uc/uc_change_passwd.html')

class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request, "uc/uc_profile.html")

    def post(self, request):
        ret_info = {"code": 200, "msg": "修改成功"}
        try:
            if request.POST.get("email"):
                request.user.email = request.POST.get("email")
            if request.POST.get("mobile"):
                print('change mobile')
                request.user.mobile = request.POST.get("mobile")
            if request.POST.get("qq"):
                request.user.qq = request.POST.get("qq")
            if request.POST.get("realname"):
                request.user.realname = request.POST.get("realname")
            request.user.save()
        except Exception as ex:
            ret_info = {"code": 200, "msg": "修改失败"}
        return render(request, "uc/uc_profile.html", {"ret_info": ret_info})


class Collect(LoginRequiredMixin,View):
    def get(self,request):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT house_houseinfo.id,house_houseinfo.type,house_houseinfo.info,house_houseinfo.location,house_houseinfo.photo,house_houseinfo.price,house_houseinfo.title  FROM show_housecollection,Uc_user,house_houseinfo WHERE Uc_user.id=8 and show_housecollection.status=1 and house_houseinfo.id=show_housecollection.house_id")
        rows = cursor.fetchall()

        # rows = cursor.fetchmany(2)  返回2条数据(3,4,5,6,7,...)
        kwag = {
            "houselist": rows,
        }

        return render(request,"uc/uc_collection.html",kwag)
