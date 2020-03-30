#完成所有功能类的初始化
from utils.Utils import Utils
import configparser



class BaseApi:

    json_data=None
    config = configparser.ConfigParser()
    config.read("Config.ini", encoding="utf-8")
    url = config.get("Url", "url")

    @classmethod
    def verbose(self,json_object):
        print(Utils.format(json_object))

    @classmethod
    def jsonpath(self,expr):
        return Utils.jsonpath(self.json_data,expr)
