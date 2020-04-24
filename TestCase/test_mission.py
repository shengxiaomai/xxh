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
    @pytest.mark.parametrize("payload",
                             [
                                 {"name": "自由讨论",
                                  "desc": "sdfgdsfgfdsg",
                                  "ext": "{\"tagId\":\"626549294551269829\",\"meetingType\":1,\"timeUse\":\"5分钟\"}",
                                  "tagId": "626549294551269829"},
                                 {"name": "主题演讲",
                                  "desc": "<!DOCTYPE html>\n      <html lang=\"en\">\n      <head>\n        <meta charset=\"UTF-8\">\n        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n        <title>Document</title>\n        <style>\n          * {\n            padding: 0;\n            margin: 0;\n          }\n        </style>\n      </head>\n      <body>\n        <div style='font-size: 17px;color: #7f7f7f;'>461616</div>\n      </body>\n      </html>",
                                  "ext": "{\"tagId\":\"626544899323331013\",\"meetingType\":0,\"speaker\":\"15166841990 Qiucw\",\"speakerId\":\"636786270315479359\",\"timeUse\":\"9分钟\",\"teachStyle\":\"直播演讲\",\"audio\":{\"result\":\"\",\"name\":\"\"},\"video\":{\"result\":\"\",\"name\":\"\"},\"content\":\"<!DOCTYPE html>\\n      <html lang=\\\"en\\\">\\n      <head>\\n        <meta charset=\\\"UTF-8\\\">\\n        <meta name=\\\"viewport\\\" content=\\\"width=device-width, initial-scale=1.0\\\">\\n        <title>Document</title>\\n        <style>\\n          * {\\n            padding: 0;\\n            margin: 0;\\n          }\\n        </style>\\n      </head>\\n      <body>\\n        <div style='font-size: 17px;color: #7f7f7f;'>461616</div>\\n      </body>\\n      </html>\"}",
                                  "tagId": "626544899323331013"}
                             ])
    def test_createAgenda(self, payload):
        '''
        添加议程
        版本v1.0.0
        :param payload:
        :return:
        '''
        self.log.info("开始测试添加议程")
        a = missionApi.createMeeting(payload)
        assert a["msg"] == self.expected_msg


    @pytest.mark.parametrize("payload", [{
            "desc": "学习会议的文稿",
            "name": "新建的学习会",
            "content":"学习会议的文稿"
    }])
    def test_createMeeting(self,payload):
        '''
        用户创建学习会
        版本v1.0.0
        :param payload: 参数
        :return:
        '''
        self.log.info("开始测试创建学习会")
        a = missionApi.createMeeting(payload)
        assert a["msg"] == self.expected_msg


    @pytest.mark.parametrize("payload", [{"agendaIds":["666910263752000147"],
                                          "content":"反反复复个广告发个广告广告方法个 v 尺寸",
                                          "desc": "反反复复个广告发个广告广告方法个 v 尺寸",
                                          "ext": "{\"video\":{\"result\":\"\",\"name\":\"\"},\"audio\":{\"result\":\"\",\"name\":\"\"},\"content\":{\"contentHtml\":\"\",\"contentText\":\"\"}}",
                                          "name": "测试",
                                          "pid":"666892345685312147",
                                          "startTime":datetime.datetime.strftime(datetime.datetime.now()+datetime.timedelta(minutes=5),'%Y-%m-%d %H:%M:%S')}])
    def test_createTheme(self,payload):
        '''
        添加主题
        版本v1.0.0
        :param payload:
        :return:
        '''
        self.log.info("开始测试添加主题")
        a = missionApi.createTheme(payload)
        assert a["msg"] == self.expected_msg


    @pytest.mark.parametrize("payload", [{}])
    def test_delAgendaById(self, payload):
        '''
        删除议程
        版本v1.0.0
        :param payload: 参数
        :return:
        '''
        self.log.info("删除议程")
        a = missionApi.delAgendaById(payload)
        assert a["msg"] == self.expected_msg


    @pytest.mark.parametrize("payload", [{}])
    def test_delMeetingById(self, payload):
        '''
        删除我的学习会
        版本v1.1.0
        :param payload: 参数
        :return:
        '''
        self.log.info("删除我的学习会")
        a = missionApi.delMeetingById(payload)
        assert a["msg"] == self.expected_msg


    @pytest.mark.parametrize("payload", [{}])
    def test_delThemeById(self, payload):
        '''
        删除主题会
        版本v1.1.0
        :param payload: 参数
        :return:
        '''
        self.log.info("删除主题会")
        a = missionApi.delThemeById(payload)
        assert a["msg"] == self.expected_msg


    @pytest.mark.parametrize("payload", [{"desc": "再次编辑",
    "name": "测试编辑学习会",
    "content":"再次编辑",
    "id":"667115786527048181"}])
    def test_editMeeting(self,payload):
        '''
        编辑我的学习会
        版本v1.1.0
        :param payload: 参数
        :return:
        '''
        self.log.info("编辑我的学习会")
        a = missionApi.editMeeting(payload)
        assert a["msg"] == self.expected_msg


    @pytest.mark.parametrize("payload", [{"agendaIds":["667150077277504157"],
                                          "content":"再次修改主题会议内容",
                                          "desc": "再次修改主题会议内容",
                                          "ext": "{\"video\":{\"result\":\"\",\"name\":\"\"},\"audio\":{\"result\":\"\",\"name\":\"\"},\"content\":{\"contentHtml\":\"\",\"contentText\":\"\"}}",
                                          "id": "667150233641157277",
                                          "name": "测试编辑主题会",
                                          "pid":"666387367187186323",
                                          "startTime":"2020-04-25 23:00:00"}])
    def test_editTheme(self,payload):
        '''
        编辑主题内容
        版本v1.1.0
        :param payload:
        :return:
        '''
        self.log.info("开始编辑主题内容")
        a = missionApi.editTheme(payload)
        assert a["msg"] == self.expected_msg


    @pytest.mark.parametrize("payload", [{
        "idx": 0,
        "size": 20
    }])
    def test_getMeetingDetail(self, payload):
        '''
        学习会详情
        版本v1.1.0
        :param payload: 参数
        :return:
        '''
        self.log.info("学习会详情")
        a = missionApi.getMeetingDetail(payload)
        assert a["msg"] == self.expected_msg


    @pytest.mark.parametrize("payload", [{}])
    def test_getMeetingList(self, payload):
        '''
        用户查询所有学习会列表
        版本v1.1.0
        :param payload: 参数
        :return:
        '''
        self.log.info("用户查询所有学习会列表")
        a = missionApi.getMeetingList(payload)
        assert a["msg"] == self.expected_msg


    @pytest.mark.parametrize("payload", [{
        "idx": 0,
        "size": 20
    }])
    def test_getMyMeetingList(self, payload):
        '''
        用户查看我的会议列表
        版本v1.1.0
        :param payload: 参数
        :return:
        '''
        self.log.info("用户查看我的会议列表")
        a = missionApi.getMyMeetingList(payload)
        assert a["msg"] == self.expected_msg


    @pytest.mark.parametrize("payload", [{
        "idx": 0,
        "size": 20,
        "userId": "636804209588568383"
    }])
    def test_missionThemeList(self, payload):
        '''
        任务主题列表查询(首页列表)
        版本v1.0.0
        :param payload: 参数
        :return:
        '''
        self.log.info("任务主题列表查询(首页列表)")
        a = missionApi.missionThemeList(payload)
        assert a["msg"] == self.expected_msg


    @pytest.mark.parametrize("payload", [{}])
    def test_queryThemeInfo(self, payload):
        '''
        主题详情查询
        版本v1.0.0
        :param payload: 参数
        :return:
        '''
        self.log.info("主题详情查询")
        a = missionApi.queryThemeInfo(payload)
        assert a["msg"] == self.expected_msg


    @pytest.mark.parametrize("payload", [{
        "ext": "{\"tagId\":\"626549294551269829\",\"meetingType\":1,\"timeUse\":\"4分钟\"}",
        "id": "667150077277504157",
        "name": "自由讨论",
        "tagId": "626549294551269829"
    }])
    def test_updateAgenda(self, payload):
        '''
        修改议程
        版本v1.0.0
        :param payload: 参数
        :return:
        '''
        self.log.info("修改议程")
        a = missionApi.updateAgenda(payload)
        assert a["msg"] == self.expected_msg


    @pytest.mark.parametrize("payload", [{
        "missionId": "666387367187186323",
        "userId": "636804209588568383"
    }])
    def test_userAddMission(self, payload):
        '''
        用户加入学习会
        版本v1.0.0
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
        版本v1.1.0
        :param payload: 参数
        :return:
        '''
        self.log.info("用户退出学习会")
        a = missionApi.userExitMission(payload)
        assert a["msg"] == self.expected_msg