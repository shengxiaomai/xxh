#coding: utf-8

import requests
from Conf.Config import Config
from api import login
from api.BaseApi import BaseApi
import time

class groupimApi(BaseApi):

    conf = Config()
    host = conf.groupim_debug
    exitRoom_url = host + 'chat/exitRoom?t=' + str(int(time.time()))
    intoRoom_url = host + 'chat/intoRoom?t=' + str(int(time.time()))
    getYxRoomStatus_url = host + 'chat/getYxRoomStatus?yxRoomId=52082273159127'
    getVideoAudioRoomInfo_url = host + 'chat/getVideoAudioRoomInfo?roomId=691309615136112911&yxRoomId=52082330175442'
    queryTipsYxCommonMsg_url = host + 'yxcommon/queryTipsYxCommonMsg?t=' + str(int(time.time()))
    audioToText_url = host + 'yxcommon/audioToText?t=' + str(int(time.time()))
    sendRoomMsg_url = host + 'yxcommon/sendRoomMsg?t=' + str(int(time.time()))
    closeRoom_url = host + 'chat/closeRoom?t=' + str(int(time.time()))
    createVideoAudioRoom_url = host + 'chat/createVideoAudioRoom?t=' + str(int(time.time()))
    queryYxCommonMsg_url = host +'yxcommon/queryYxCommonMsg?t=' + str(int(time.time()))
    headers = {"authorization": login.Login.login(), "content - type": "application/json;charset=utf-8"}


    #关闭房间
    @classmethod
    def closeRoom(self,payload):
        self.json_data = requests.post(self.closeRoom_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #创建音视频聊天室
    @classmethod
    def createVideoAudioRoom(self,payload):
        self.json_data = requests.post(self.createVideoAudioRoom_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    #退出聊天或者拒绝接听
    @classmethod
    def exitRoom(self,payload):
        self.json_data = requests.post(self.exitRoom_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    # 查询音视频聊天室内信息
    @classmethod
    def getVideoAudioRoomInfo(self, payload):
        self.json_data = requests.get(self.getVideoAudioRoomInfo_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    # 查询云信音视频房间状态
    @classmethod
    def audioToText(self, payload):
        self.json_data = requests.get(self.getYxRoomStatus_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    # 用户加入房间
    @classmethod
    def intoRoom(self, payload):
        self.json_data = requests.post(self.intoRoom_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    # 聊天室语音转文字
    @classmethod
    def audioToText(self, payload):
        self.json_data = requests.post(self.audioToText_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    # 获取云信聊天室历史精选分享消息
    @classmethod
    def queryTipsYxCommonMsg(self, payload):
        self.json_data = requests.post(self.queryTipsYxCommonMsg_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data


    # 获取云信聊天室历史消息
    @classmethod
    def queryYxCommonMsg(self, payload):
        self.json_data = requests.post(self.queryYxCommonMsg_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data

    # 给聊天室发送主题演讲文稿
    @classmethod
    def sendRoomMsg(self, payload):
        self.json_data = requests.post(self.sendRoomMsg_url, headers=self.headers, json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data

