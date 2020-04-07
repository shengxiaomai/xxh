#coding: utf-8

import requests
from Conf.Config import Config
from api import login
from api.BaseApi import BaseApi
import time


class missionApi(BaseApi):

    conf = Config()
    host = conf.host_debug
    createAgenda_url = host+'createMeeting?t='+str(int(time.time()))
    headers = {"authorization": login.Login.login(), "content - type": "application/json;charset=utf-8"}
    @classmethod
    def createAgenda(self):
        payload = {
            "desc": "<!DOCTYPE html>\n      <html lang=\"en\">\n      <head>\n        <meta charset=\"UTF-8\">\n        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n        <title>Document</title>\n      </head>\n      <body>\n        <div style='font-size: 17px;color: #7f7f7f;'>我的学习会</div>\n      </body>\n      </html>",
            "name": "我的学习会3"}
        self.json_data = requests.post(self.createAgenda_url, headers=self.headers,json=payload, verify=False).json()
        self.verbose(self.json_data)
        return self.json_data
