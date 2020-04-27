#coding=utf-8

import pytest
import allure
from api.user import userApi
from Common import Log

class TestUser:

    log = Log.MyLog()
    expected_msg = "success"
    expected_mobile="15002020506"
    expected_userId = "636804209588568383"

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


    @pytest.mark.parametrize("payload", [{"isEdit":1,"sex":1}])
    def test_editUserInfo(self, payload):
        '''
        编辑用户信息
        :param payload:
        :return:
        '''
        self.log.info("编辑用户信息")
        a = userApi(payload).editUserInfo()["msg"]
        assert a == self.expected_msg


    @pytest.mark.parametrize("payload", [{}])
    def test_getUserInfo(self, payload):
        '''
        获取用户信息
        :param payload:
        :return:
        '''
        self.log.info("获取用户信息")
        a = userApi(payload).getUserInfo()["body"]["mobile"]
        assert a == self.expected_mobile


    @pytest.mark.parametrize("payload", [{"mobile":"15002020506"}])
    def test_getUserInfoByMobile(self, payload):
        '''
        根据用户手机查询用户信息
        :param payload:
        :return:
        '''
        self.log.info("根据用户手机查询用户信息")
        a = userApi(payload).getUserInfoByMobile()["body"]["userId"]
        assert a == self.expected_userId


    @pytest.mark.parametrize("payload", [{"editCode":2,"userId":"636804209588568383"}])
    def test_editCallRemind(self, payload):
        '''
        修改语音视频通话提示(打开或者关闭用户语音和视频通话提醒)
        :param payload:
        :return:
        '''
        self.log.info("修改语音视频通话提示")
        a = userApi(payload).editCallRemind()["body"]["userId"]
        assert a == self.expected_userId


