#coding: utf-8

import requests
from Conf.Config import Config
from api import login
from api.BaseApi import BaseApi
import time


class missionApi(BaseApi):

    conf = Config()
    host = conf.host_debug
    createAgenda_url = host + 'createMeeting?t=' + str(int(time.time()))
    createMeeting_url = host+'createMeeting?t='+str(int(time.time()))
    createTheme_url = host + 'createTheme?t=' + str(int(time.time()))
    editMeeting_url = host + 'editMeeting?t=' + str(int(time.time()))
    editTheme_url = host + 'editTheme?t=' + str(int(time.time()))
    userAddMission_url=host + 'userAddMission?t=' + str(int(time.time()))
    userExitMission_url = host + 'userExitMission?t=' + str(int(time.time()))
    missionThemeList_url = host + 'missionThemeList?t=' + str(int(time.time()))
    getMyMeetingList_url = host + 'getMyMeetingList?t=' + str(int(time.time()))
    getMeetingDetail_url = host + 'getMeetingDetail/666387367187186323?t=' + str(int(time.time()))
    getMeetingList_url = host + 'getMeetingList?t=' + str(int(time.time()))
    queryThemeInfo_url = host + 'queryThemeInfo/667150233641157277?t=' + str(int(time.time()))
    updateAgenda_url = host + 'updateAgenda?t=' + str(int(time.time()))
    delAgendaById_url = host + 'delAgendaById/667277411649323515?t=' + str(int(time.time()))
    delMeetingById_url = host + 'delMeetingById/667278911532433915?t=' + str(int(time.time()))
    delThemeById_url = host + 'delThemeById/667344913905484039?t=' + str(int(time.time()))
    headers = {"authorization": login.Login.login(), "content - type": "application/json;charset=utf-8"}




    #添加议程
    @classmethod
    def createAgenda(self,payload):
        self.json_data = requests.post(self.createAgenda_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #用户创建学习会
    @classmethod
    def createMeeting(self,payload):
        self.json_data = requests.post(self.createMeeting_url, headers=self.headers,json=payload, verify=False).json()
        return self.json_data


    #添加主题
    @classmethod
    def createTheme(self,payload):
        '''

        :param payload: 方法参数
        :return: 返回json
        '''
        self.json_data = requests.post(self.createTheme_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #删除议程
    @classmethod
    def delAgendaById(self,payload):
        '''

        :param payload: 方法参数
        :return: 返回json
        '''
        self.json_data = requests.delete(self.delAgendaById_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #删除我的学习会
    @classmethod
    def delMeetingById(self,payload):
        '''

        :param payload: 方法参数
        :return: 返回json
        '''
        self.json_data = requests.delete(self.delMeetingById_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #删除主题会
    @classmethod
    def delThemeById(self,payload):
        '''

        :param payload: 方法参数
        :return: 返回json
        '''
        self.json_data = requests.delete(self.delThemeById_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #编辑我的学习会
    @classmethod
    def editMeeting(self,payload):
        self.json_data = requests.post(self.editMeeting_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #编辑主题内容
    @classmethod
    def editTheme(self,payload):
        self.json_data = requests.post(self.editTheme_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #学习会详情
    @classmethod
    def getMeetingDetail(self,payload):
        self.json_data = requests.get(self.getMeetingDetail_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #用户查询所有学习会列表
    @classmethod
    def getMeetingList(self,payload):
        self.json_data = requests.post(self.getMeetingList_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #用户查看我的会议列表
    @classmethod
    def getMyMeetingList(self,payload):
        self.json_data = requests.get(self.getMyMeetingList_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #任务主题列表查询(首页列表)
    @classmethod
    def missionThemeList(self,payload):
        self.json_data = requests.post(self.missionThemeList_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #主题详情查询(包含议程)
    @classmethod
    def queryThemeInfo(self,payload):
        self.json_data = requests.get(self.queryThemeInfo_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #修改议程
    @classmethod
    def updateAgenda(self,payload):
        self.json_data = requests.post(self.updateAgenda_url, headers=self.headers, json=payload, verify=False).json()
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





