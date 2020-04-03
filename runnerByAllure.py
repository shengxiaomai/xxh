import pytest
import subprocess

if __name__== '__main__':

    #pytest.main(['--alluredir','/Users/xiaomai/PycharmProjects/shy/Report/xml','/Users/xiaomai/PycharmProjects/shy/TestCase'])
    pytest.main(['--alluredir', '/Users/xiaomai/PycharmProjects/shyApi/Report/xml', '--allure-severities=blocker','/Users/xiaomai/PycharmProjects/shyApi/TestCase'])
    print(subprocess.getstatusoutput('allure generate   --clean /Users/xiaomai/PycharmProjects/shyApi/Report/xml --output /Users/xiaomai/PycharmProjects/shyApi/Report/html'))