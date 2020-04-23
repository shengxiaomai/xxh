#coding=utf-8

import pytest
import allure
from api.mission import missionApi
from Common import Log
import datetime

class TestMission:
    """
    主题议程模块测试
    """

    log = Log.MyLog()
    expected_msg = "success"


    @allure.severity('normal')
    @allure.story('Collections')
    @pytest.mark.parametrize("payload", [{
            "desc": "学习会议的文稿",
            "name": "新建的学习会",
            "content":"学习会议的文稿"
    }])
    def test_createMeeting(self,payload):
        '''
        测试创建学习会
        :param payload: 参数
        :return:
        '''
        self.log.info("开始测试创建学习会")
        a = missionApi.createMeeting(payload)
        assert a["msg"] == self.expected_msg



    @pytest.mark.parametrize("payload",
                    [
                        {"name": "自由讨论", "desc": "sdfgdsfgfdsg",
                   "ext": "{\"tagId\":\"626549294551269829\",\"meetingType\":1,\"timeUse\":\"5分钟\"}",
                   "tagId": "626549294551269829"},
                     {"name":"主题演讲", "desc":"<!DOCTYPE html>\n      <html lang=\"en\">\n      <head>\n        <meta charset=\"UTF-8\">\n        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n        <title>Document</title>\n        <style>\n          * {\n            padding: 0;\n            margin: 0;\n          }\n        </style>\n      </head>\n      <body>\n        <div style='font-size: 17px;color: #7f7f7f;'>461616</div>\n      </body>\n      </html>","ext":"{\"tagId\":\"626544899323331013\",\"meetingType\":0,\"speaker\":\"15166841990 Qiucw\",\"speakerId\":\"636786270315479359\",\"timeUse\":\"9分钟\",\"teachStyle\":\"直播演讲\",\"audio\":{\"result\":\"\",\"name\":\"\"},\"video\":{\"result\":\"\",\"name\":\"\"},\"content\":\"<!DOCTYPE html>\\n      <html lang=\\\"en\\\">\\n      <head>\\n        <meta charset=\\\"UTF-8\\\">\\n        <meta name=\\\"viewport\\\" content=\\\"width=device-width, initial-scale=1.0\\\">\\n        <title>Document</title>\\n        <style>\\n          * {\\n            padding: 0;\\n            margin: 0;\\n          }\\n        </style>\\n      </head>\\n      <body>\\n        <div style='font-size: 17px;color: #7f7f7f;'>461616</div>\\n      </body>\\n      </html>\"}",
                                                   "tagId":"626544899323331013"}
                    ])
    def test_createAgenda(self,payload):
        '''
        测试添加议程
        :param payload:
        :return:
        '''
        self.log.info("开始测试添加议程")
        a = missionApi.createMeeting(payload)
        assert a["msg"] == self.expected_msg

    @pytest.mark.parametrize("payload", [{"agendaIds":["656964581662392753"],"name":"你好","pid":"656789803471208874","startTime":datetime.datetime.strftime(datetime.datetime.now()+datetime.timedelta(minutes=5),'%Y-%m-%d %H:%M:%S')}])
    def test_createTheme(self,payload):
        '''
        测试添加主题
        :param payload:
        :return:
        '''
        self.log.info("开始测试添加主题")
        a = missionApi.createTheme(payload)
        assert a["msg"] == self.expected_msg

    @pytest.mark.parametrize("payload", [{
        "missionId": "666387367187186323",
        "userId": "636804209588568383"
    }])
    def test_userAddMission(self, payload):
        '''
        用户加入学习会
        :param payload: 参数
        :return:
        '''
        self.log.info("用户加入学习会")
        a = missionApi.userAddMission(payload)
        assert a["msg"] == self.expected_msg

    @pytest.mark.parametrize("payload", [{
        "missionId": "666387367187186323",
        "userId": "636804209588568383"
    }])
    def test_userExitMission(self, payload):
        '''
        用户退出学习会
        :param payload: 参数
        :return:
        '''
        self.log.info("用户退出学习会")
        a = missionApi.userExitMission(payload)
        assert a["msg"] == self.expected_msg