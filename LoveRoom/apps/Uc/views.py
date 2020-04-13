from django.shortcuts import render,redirect, reverse
from django.views.generic import View
import logging
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from .models import User
from apps.house.models import Order
from .forms import RegisterForm,PhoneLoginForm,PwLoginForm
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
logger = logging.getLogger('account')
from django.contrib.auth.hashers import check_password as auth_check_password

class LoginRequiredMixin(object):
    """
    登陆限定，并指定登陆url
    """
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/')

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


class ChangePasswd(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'uc/uc_change_passwd.html')
    def post(self,request):
        ret = {"status": 400, "msg": "调用方式错误"}
        oldpassword = request.POST.get("oldpassword")
        newpasswd1 = request.POST.get("newpassword1")
        if auth_check_password(oldpassword, request.user.password):
            request.user.password=make_password(newpasswd1)
            logger.info(f"{request.user.username}注销成功")
            logger.info(f"{request.user.username}修改密码成功")
            request.user.save()
            return render(request,'house/index.html',{"msg":"修改密码成功，请重新登录"})

        else:
            ret ={"status": 300, "msg": "旧密码错误"}
            return render(request,"uc/uc_change_passwd.html",{"msg":"旧密码错误"})




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
        sql = "SELECT house_houseinfo.id,house_houseinfo.type,house_houseinfo.info,house_houseinfo." \
              "location,house_houseinfo.photo,house_houseinfo.price,house_houseinfo.title FROM show_housecollection,Uc_user,house_houseinfo WHERE show_housecollection.user_id= %d and show_housecollection.status=1 and house_houseinfo.id=show_housecollection.house_id GROUP BY house_houseinfo.id" % request.user.id

        cursor.execute(sql)
        rows = cursor.fetchall()
        paginator = Paginator(rows, 12)
        page = request.GET.get('page')
        numlist = []
        if paginator.num_pages > 5:
            numlist = ['1', '2', '3', '4', '5']
        else:
            for i in range(1, paginator.num_pages + 1):
                numlist.append(str(i))
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
            page = 1
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
            page = paginator.num_pages

        # rows = cursor.fetchmany(2)  返回2条数据(3,4,5,6,7,...)
        kwag = {
            "houselist": contacts,
            "page" : page,
            'fivenum': numlist,
            'pagenum': paginator.num_pages,
        }

        return render(request,"uc/uc_collection.html",kwag)


class Order(LoginRequiredMixin,View):
    def get(self,request):
        from django.db import connection
        cursor = connection.cursor()
        sql = "SELECT house_houseinfo.id,house_houseinfo.type,house_houseinfo.info,house_houseinfo.location," \
              "house_houseinfo.photo,house_order.price,house_houseinfo.title,house_order.id,house_order.start_date,house_order.end_date FROM house_order,Uc_user,house_houseinfo WHERE house_order.customer_id= %d and house_houseinfo.id=house_order.house_id GROUP BY house_order.id" % request.user.id
        cursor.execute(sql)
        rows = cursor.fetchall()
        paginator = Paginator(rows, 12)
        page = request.GET.get('page')
        numlist = []
        if paginator.num_pages > 5:
            numlist = ['1', '2', '3', '4', '5']
        else:
            for i in range(1, paginator.num_pages + 1):
                numlist.append(str(i))
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
            page = 1
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
            page = paginator.num_pages

        # rows = cursor.fetchmany(2)  返回2条数据(3,4,5,6,7,...)
        kwag = {
            "orderlist": contacts,
            "page" : page,
            'fivenum': numlist,
            'pagenum': paginator.num_pages,
        }
        return render(request,"uc/uc_order.html",kwag)
