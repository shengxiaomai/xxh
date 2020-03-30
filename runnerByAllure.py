import pytest
import subprocess

if __name__== '__main__':

    #pytest.main(['--alluredir','/Users/xiaomai/PycharmProjects/shy/report/xml','/Users/xiaomai/PycharmProjects/shy/TestCase'])
    pytest.main(['--alluredir', '/Users/xiaomai/PycharmProjects/shyApi/report/xml', '--allure-severities=blocker','/Users/xiaomai/PycharmProjects/shyApi/TestCase'])
    print(subprocess.getstatusoutput('allure generate   --clean /Users/xiaomai/PycharmProjects/shyApi/report/xml --output /Users/xiaomai/PycharmProjects/shyApi/report/html'))