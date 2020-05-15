#coding=utf-8

import pytest
import allure
from api.groupim import groupimApi
from Common import Log
import datetime

class TestGroupim:
    log = Log.MyLog()
    expected_msg = "success"
    expected_yxRoomId="52082273159127"
    expected_cid=52082330175442
    expected_userid="636804209588568383"
    expected_msgContent="gogogo"


    @pytest.mark.parametrize("payload", [{"roomId":691610799449309455,"yxRoomId":52083065489361}])
    def test_closeRoom(self, payload):
        '''
        关闭房间
        :param payload:
        :return:
        '''
        a = groupimApi.closeRoom(payload)["msg"]
        assert a == self.expected_msg


    @pytest.mark.parametrize("payload", [{"missionId":691622459614429871,"type": 2}])
    def test_createVideoAudioRoom(self, payload):
        '''
        创建音视频聊天室
        :param payload:
        :return:
        '''
        a = groupimApi.createVideoAudioRoom(payload)["msg"]
        assert a == self.expected_msg


    @pytest.mark.parametrize("payload", [{"roomId": "691286261654094095","yxRoomId":"52082273159127"}])
    def test_exitRoom(self, payload):
        '''
        退出聊天或者拒绝接听
        :param payload:
        :return:
        '''
        a = groupimApi.exitRoom(payload)["msg"]
        assert a == self.expected_msg


    @pytest.mark.parametrize("payload", [{}])
    def test_getVideoAudioRoomInfo(self, payload):
        '''
        查询音视频聊天室内信息
        :param payload:
        :return:
        '''
        a = groupimApi.getVideoAudioRoomInfo(payload)["body"]["cid"]
        assert a == self.expected_cid


    @pytest.mark.parametrize("payload", [{}])
    def test_getYxRoomStatus(self, payload):
        '''
        查询云信音视频房间状态
        :param payload:
        :return:
        '''
        a = groupimApi.getYxRoomStatus(payload)["body"]["yxRoomId"]
        assert a == self.expected_yxRoomId


    @pytest.mark.parametrize("payload", [{"roomId": "691286261654094095"}])
    def test_intoRoom(self, payload):
        '''
        用户加入房间
        :param payload:
        :return:
        '''
        a = groupimApi.intoRoom(payload)["msg"]
        assert a == self.expected_msg


    @pytest.mark.parametrize("payload", [{"accId": "636804209588568383","audioUrl":"https://xxh-test-1254038939.cos.ap-guangzhou.myqcloud.com/xxh/user/sbc/audio/691146c9d9c6b79c1432e136d24b545b_origin.mp3"
                                             ,"chatRoomId":"176001193","roomId":"691500472745328911","themeId":"691500472745328911","themeName":"哦啦啦"}])
    def test_audioToText(self, payload):
        '''
        聊天室语音转文字
        :param payload:
        :return:
        '''
        a = groupimApi.audioToText(payload)["msg"]
        assert a == self.expected_msg


    @pytest.mark.parametrize("payload", [{"businessId": 691443947620270767,"idx":0,"queryType":1,"size":10}])
    def test_queryTipsYxCommonMsg(self, payload):
        '''
        获取云信聊天室历史精选分享消息
        :param payload:
        :return:
        '''
        a = groupimApi.queryTipsYxCommonMsg(payload)["body"]["msgInfo"][0]["userId"]
        assert a == self.expected_userid


    @pytest.mark.parametrize("payload", [{"businessId": 691697645969736367,"idx":0,"queryType":1,"size":10}])
    def test_queryYxCommonMsg(self, payload):
        '''
        获取云信聊天室历史消息
        :param payload:
        :return:
        '''
        a = groupimApi.queryYxCommonMsg(payload)["body"]["msgInfo"][0]["msgContent"]
        assert a == self.expected_msgContent


    @pytest.mark.parametrize("payload", [{"meetingId":"691539090406900399","themeId":"691539461518918319"}])
    def test_sendRoomMsg(self, payload):
        '''
        给聊天室发送主题演讲稿
        :param payload:
        :return:
        '''
        a = groupimApi.sendRoomMsg(payload)["msg"]
        assert a == self.expected_msg