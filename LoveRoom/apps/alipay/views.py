from django.contrib.auth.mixins import LoginRequiredMixin
from apps.house.models import HouseInfo, Order, Order_date
from apps.Uc.models import User
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.views.generic import View
from LoveRoom.settings import ALIPAY
import datetime
import time
from libs.pay import AliPay


class Booking(LoginRequiredMixin,View):
    def get(self,request,id):
        house = HouseInfo.objects.filter(id=id)[0]
        st = datetime.datetime.strptime(request.GET.get('st'), '%m/%d/%Y')
        et = datetime.datetime.strptime(request.GET.get('et'), '%m/%d/%Y')
        order_list = Order_date.objects.filter(date__range=(st, et),house=id)
        if order_list:
            return render(request,'show/404.html',status=404)
        st = request.GET.get('st')
        et = request.GET.get('et')
        kwag = {
            'house': house,
            'st': st,
            'et': et,
        }
        return render(request,'show/booking.html',kwag)

    def post(self, request, id):
        values = request.POST
        moneny = values.get('moneny')
        order_num = 'gs' + str(id) + datetime.datetime.now().strftime('%Y%m%d')
        date = values.get('order_date')
        date_list = date.split('-')
        end_date = datetime.datetime.strptime(date_list[1].split(' ')[1],'%m/%d/%Y')
        start_date = datetime.datetime.strptime(date_list[0].split(' ')[0],'%m/%d/%Y')
        date_cut = (end_date - start_date).days
        i = 0
        while i < date_cut:
            Order_date.objects.create(house_id=id,date=(start_date + datetime.timedelta(days=i)))
            i += 1
        subject = "归宿短租房间预订"
        alipay = ali()
        Order.objects.create(order_num=order_num,house_id=id,customer_id=request.user.id,price=moneny,
                             start_date=start_date,end_date=end_date,customer_num=values.get('customer_num'),liuyan=values.get('liuyan'))

        # 生成支付的url
        query_params = alipay.direct_pay(
            subject=subject,  # 商品简单描述
            out_trade_no=order_num,  # 商户订单号
            total_amount=moneny,  # 交易金额(单位: 元 保留俩位小数)
        )
        # 支付宝网关,带上订单参数才有意义
        pay_url = "{}{}".format(ALIPAY["gateway"],query_params)
        # POST请求重定向到支付宝提供的网关，跳转到支付宝支付界面
        return redirect(pay_url)


def ali():
    # POST请求，用于最后的检测(检测是否支付成功，生成订单)
    notify_url = ALIPAY["server_url"]+reverse("pay")
    # GET请求，用于页面的跳转展示（获取订单状态，显示给用户）
    return_url = ALIPAY["server_url"]+reverse("pay_result")

    alipay = AliPay(
        appid=ALIPAY["app_id"],
        app_notify_url=notify_url,
        return_url=return_url,
        app_private_key_path=ALIPAY["app_private_key"],
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
        alipay_public_key_path=ALIPAY["alipay_public_key"],
        debug=True,  # 默认False,
    )
    return alipay

class PayView(View):
    def get(self, request):
        return render(request, 'alipay/pay.html')

    def post(self, request):
        money = float(request.POST.get('money'))
        subject = "Django课程"
        alipay = ali()
        # 生成支付的url
        query_params = alipay.direct_pay(
            subject=subject,  # 商品简单描述
            out_trade_no="x2" + str(time.time()),  # 商户订单号
            total_amount=money,  # 交易金额(单位: 元 保留俩位小数)
        )
        # 支付宝网关,带上订单参数才有意义
        pay_url = "{}{}".format(ALIPAY["gateway"],query_params)
        # POST请求重定向到支付宝提供的网关，跳转到支付宝支付界面
        return redirect(pay_url)

class PayResultView(View):
    def get(self, request):
        alipay = ali()
        params = request.GET.dict()
        sign = params.pop('sign', None)
        status = alipay.verify(params, sign)
        if status:
            # 获取订单状态，显示给用户
            return HttpResponse('支付成功')

    def post(self, request):
        alipay = ali()
        # 检测是否支付成功
        # 去请求体中获取所有返回的数据：状态/订单号
        from urllib.parse import parse_qs
        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)

        params = {}
        for k, v in post_data.items():
            params[k] = v[0]
        sign = params.pop('sign', None)
        status = alipay.verify(params, sign)
        print(1111)

        if status:
            # 修改订单状态
            out_trade_no = params.get('out_trade_no', None)  # 商户订单号
            trade_no = params.get('trade_no', None)  # 支付宝交易号
            buyer_id = params.get('buyer_id', None)  # 买家支付宝用户号
            trade_status = params.get('trade_status', None)  # 交易状态
            total_amount = params.get('total_amount', None)  # 订单金额
            receipt_amount = params.get('receipt_amount', None)  # 实收金额
            subject = params.get('subject', None)  # 订单标题
            gmt_payment = params.get('gmt_payment', None)  # 交易付款时间
        return HttpResponse('支付宝的POST回调')