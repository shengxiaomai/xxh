# -*- coding: utf-8 -*-
# @Time    : 2020/4/5
# @Author  : sheng
# @File    : Log.py

"""
封装log方法

"""

from configparser import ConfigParser
import os

class Config:
    # titles:
    TITLE_DEBUG = "private_debug"


    # values:
    # [debug\release]
    VALUE_TESTER = "tester"
    VALUE_ENVIRONMENT = "environment"
    VALUE_VERSION_CODE = "versionCode"
    VALUE_HOST = "host"
    VALUE_LOGIN_HOST = "loginHost"
    VALUE_LOGIN_INFO = "loginInfo"
    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):

        self.config = ConfigParser()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir + '/Report/xml'
        self.html_report_path = Config.path_dir + '/Report/html'


        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")
        self.config.read(self.conf_path, encoding='utf-8')

        self.tester_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
        self.environment_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_ENVIRONMENT)
        self.versionCode_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_VERSION_CODE)
        self.host_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_HOST)
        self.loginHost_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_HOST)
        self.loginInfo_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_INFO)

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)