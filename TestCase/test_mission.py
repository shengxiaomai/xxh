import pytest
import allure
from api.mission import missionApi
from Common import Log

class TestMission:

    def test_createAgenda(self): # 添加议程（创建学习会）
        self.log = Log.MyLog()
        #self.log.error('get cookies error, please checkout!!!')
        expected_msg = "success"
        a = missionApi.createAgenda()
        msg =a["msg"]
        assert msg == expected_msg
