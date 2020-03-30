import json

import jsonpath as jsonpath


class Utils:
    @classmethod
    def format(self, json_object):
        return json.dumps(json_object,indent=2)


    @classmethod
    def jsonpath(self,json_object,expr):
        return jsonpath(json_object,expr)