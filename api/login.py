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
            sms_url = "http://xxh.maipingba.com/user/app/sendVerifyCode"
            requests.post(sms_url, json={"mobile":"18682115996"}, verify=False)
            #登录
            url="http://xxh.maipingba.com/user/app/appLogin"
            r=requests.post(url,json={"device": "android","mobile": "15002020506","verifyCode": "1234"},verify=False)
  
            if r.json()["status"] == 200:
                self.token=(r.json()["body"]["userToken"])

        return self.token

