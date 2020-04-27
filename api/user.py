#coding=utf-8

import requests
from Conf.Config import Config
from api import login
from api.BaseApi import BaseApi
import time

class userApi(BaseApi):

    def __init__(self,payload):
        self.payload = payload
        self.session = requests.session()
        self.sendVerifyCode_url = Config().user_host_debug+'sendVerifyCode'
        self.appLogin_url = Config().user_host_debug + 'appLogin'
        self.editUserInfo_url = Config().user_host_debug + 'editUserInfo'
        self.getUserInfo_url = Config().user_host_debug + 'getUserInfo'
        self.getUserInfoByMobile_url = Config().user_host_debug + 'getUserInfoByMobile'
        self.editCallRemind_url = Config().user_host_debug + 'editCallRemind'
        self.headers = {"authorization": login.Login.login(), "content - type": "application/json;charset=utf-8"}



    def sendVerifyCode(self):
        self.json_data = self.session.post(self.sendVerifyCode_url,json=self.payload).json()
        self.verbose(self.json_data)
        return self.json_data


    def appLogin(self):
        self.json_data = self.session.post(self.appLogin_url, json=self.payload).json()
        self.verbose(self.json_data)
        return self.json_data


    #编辑用户信息

    def editUserInfo(self):
        self.json_data = requests.post(self.editUserInfo_url, headers=self.headers, json=self.payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data

    #获取用户信息

    def getUserInfo(self):
        self.json_data = requests.get(self.getUserInfo_url, headers=self.headers, json=self.payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #根据手机号查询用户信息

    def getUserInfoByMobile(self):
        self.json_data = requests.post(self.getUserInfoByMobile_url, headers=self.headers, json=self.payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #修改语音视频通话提示

    def editCallRemind(self):
        self.json_data = requests.post(self.editCallRemind_url, headers=self.headers, json=self.payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data





