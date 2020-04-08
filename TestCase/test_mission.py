import pytest
import allure
from api.mission import missionApi
from Common import Log

class TestMission:

    def test_createMeeting(self): # 创建学习会
        self.log = Log.MyLog()
        #self.log.error('get cookies error, please checkout!!!')
        expected_msg = "success"
        a = missionApi.createMeeting()
        msg =a["msg"]
        assert msg == expected_msg


    def test_createAgenda(self): # 创建学习会
        self.log = Log.MyLog()
        expected_msg = "success"
        a = missionApi.createMeeting()
        msg =a["msg"]
        assert msg == expected_msg