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

    def sendVerifyCode(self):
        self.json_data = self.session.post(self.sendVerifyCode_url,json=self.payload).json()
        self.verbose(self.json_data)
        return self.json_data

    def appLogin(self):
        self.json_data = self.session.post(self.appLogin_url, json=self.payload).json()
        self.verbose(self.json_data)
        return self.json_data

