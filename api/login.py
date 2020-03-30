import requests
import pytest
#获取token
class Login:

#获取token
    token =None


    @classmethod
    def login(self):
        if self.token ==None:
            #获取验证码
            sms_url = "https://radio-api-demo.zlzgy.org.cn/api/live/app/sendVerifyCode"
            requests.post(sms_url, json={"phone": "18682115996", "smsMode": "test"}, verify=False)
            #登录
            url="https://radio-api-demo.zlzgy.org.cn/api/live/app/login"
            r=requests.post(url,json={"tel": "18682115996","telCode": "888888","type": 3},verify=False)
  
            if r.json()["status"] == 200:
                self.token=(r.json()["body"]["userToken"])

        return self.token

