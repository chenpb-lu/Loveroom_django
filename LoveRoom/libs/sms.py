"""
file：sms.py
author：陈先生
date：2019/8/422:58
blog:https://chenpb-lu.github.io
"""
import urllib.request
import urllib
import json
import logging
logger = logging.getLogger('apis')


def send_sms(mobile,captcha):
    flag = True
    url = "https://open.ucpaas.com/ol/sms/sendsms"
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    values = {

            "sid": "7c1f1eb1dca8bbcc41fd830ae0bc78c7",
            "token": "208e1550969ac468c8c267ef391bd364",
            "appid": "e0e36a084f9f4384b2d41e5fd840b316",
            "templateid": "489482",
            "param": str(captcha),
            "mobile": mobile
    }

    try:
        data = json.dumps(values).encode('utf-8')
        logger.info(f"即将发送短信: {data}")
        request = urllib.request.Request(url, data, headers)
        html = urllib.request.urlopen(request).read().decode('utf-8')
        # html = '{"code":"000000","count":"1","create_date":"2018-07-23 13:34:06","mobile":"15811564298","msg":"OK","smsid":"852579cbb829c08c917f162b267efce6","uid":""}'
        code = json.loads(html)["code"]
        # print(html)
        if code == "000000":
            logger.info(f"短信发送成功：{html}")
            flag = True
        else:
            logger.info(f"短信发送失败：{html}")
            flag = False
    except Exception as ex:
        logger.info(f"出错了,错误原因：{ex}")
        flag = False
    return flag

# if __name__ == "__main__":
#     # 测试短信接口是否是管用
#     send_sms("18390800805", "123456")