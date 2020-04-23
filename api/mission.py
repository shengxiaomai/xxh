#coding: utf-8

import requests
from Conf.Config import Config
from api import login
from api.BaseApi import BaseApi
import time


class missionApi(BaseApi):

    conf = Config()
    host = conf.host_debug
    createMeeting_url = host+'createMeeting?t='+str(int(time.time()))
    createAgenda_url = host + 'createMeeting?t=' + str(int(time.time()))
    createTheme_url = host + 'createTheme?t=' + str(int(time.time()))
    userAddMission_url=host + 'userAddMission?t=' + str(int(time.time()))
    userExitMission_url = host + 'userExitMission?t=' + str(int(time.time()))
    headers = {"authorization": login.Login.login(), "content - type": "application/json;charset=utf-8"}

    #创建学习会
    @classmethod
    def createMeeting(self,payload):
        self.json_data = requests.post(self.createMeeting_url, headers=self.headers,json=payload, verify=False).json()
        return self.json_data
    #添加议程
    @classmethod
    def createAgenda(self,payload):
        self.json_data = requests.post(self.createAgenda_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data
    #创建主题会
    @classmethod
    def createTheme(self,payload):
        '''

        :param payload: 方法参数
        :return: 返回json
        '''
        self.json_data = requests.post(self.createTheme_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data
    #用户加入学习会
    @classmethod
    def userAddMission(self,payload):
        self.json_data = requests.post(self.userAddMission_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data
    #用户退出学习会
    @classmethod
    def userExitMission(self,payload):
        self.json_data = requests.post(self.userExitMission_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data