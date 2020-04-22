#coding=utf-8

import pytest
import allure
from api.user import userApi
from Common import Log

class TestUser:

    log = Log.MyLog()
    expected_msg = "success"

    @pytest.mark.parametrize("payload", [{"mobile": "18682115996"}])
    def test_sendVerifyCode(self,payload):
        '''
        测试发送验证码接口
        :param payload:
        :return:
        '''
        a=userApi(payload).sendVerifyCode()["msg"]
        assert a == self.expected_msg

    @pytest.mark.parametrize("payload", [{"device": "android","mobile": "15166831990","verifyCode": "1234"},{"device": "android","mobile": "15166831990","verifyCode": "2334"}])
    def test_sendVerifyCode(self, payload):
        '''
        测试登录接口
        :param payload:
        :return:
        '''
        a = userApi(payload).appLogin()["msg"]
        if a == self.expected_msg:
            assert a == self.expected_msg
        else:
            assert a != self.expected_msg
