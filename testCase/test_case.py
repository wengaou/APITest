# -*- coding: utf-8 -*-
# @ProjectName：APITest
# @Author: dudu.zhang
# @File: test_case.py
# @Time: 2019-08-19 15:00
import json
import time

import get_url_params
import readExcel
import unittest
import urllib.parse
import paramunittest

from common.request import HttpClient

url = get_url_params.geturlParams().get_create_project_url()
# login_xls = readExcel.readExcel().get_xls('userCase.xlsx','createProject')
login_xls = readExcel.readExcel().get_xls('userCase.xlsx','selectProject')
# login_xls = readExcel.readExcel().get_xls('userCase.xlsx','login')
from utils.get_md5 import getAppKeyMD5

@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):

    def setParameters(self,case_name,path,query,method):
        """
        设置参数
        :param case_name:
        :param path:
        :param query:
        :param method:
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.menthod = str(method)


    def description(self):
        """
        测试报告描述
        :return:
        """
        self.case_name


    def setUp(self):
        """
        :return:
        """
        # print(self.case_name+'测试开始前准备')
        print("用例名称："+self.case_name)
        print("测试路径："+self.path)
        print("测试参数："+self.query)
        print("测试方法："+self.menthod)




    def test01case(self):
        self.checkResult()


    def tearDown(self):
        """
        :return:
        """
        print('测试结束，输出log完结\n\n')



    # def checkResult(self):
    #     """
    #     断言测试结果
    #     :return:
    #     """
    #     print(self.case_name,self.path,self.query,self.menthod)
    #     url = "http://127.0.0.1/login?"
    #     new_url = url + self.query
    #     print('new_url：',new_url)
    #     #将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
    #     # data = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
    #     data = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
    #     print('data：',data)
    #     #根据Excel中的method调用run_main来进行requests请求，并拿到响应
    #     response = HttpClient().request(self.menthod,url,data)
    #     result = json.loads(response)
    #     print('response：',result)
    #     # if self.case_name == 'login':
    #     #     self.assertEqual(result['code'],200)
    #     # if self.case_name == 'login_err':
    #     #     self.assertEqual(result['code'],-1)
    #     # if self.case_name == 'login_null':
    #     #     self.assertEqual(result['code'],10001)










    def checkResult(self):

        """
        断言测试结果
        :return:
        """
        timestamp = int(time.time() * 1000)

        new_url = url + self.query + '&'+ 'timestamp='+str(timestamp)
        print('new_url：', new_url)


        #将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        data = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))

        #根据Excel中的method调用run_main来进行requests请求，并拿到响应
        response = HttpClient().request(self.menthod,url,getAppKeyMD5(data))

        print("response:",response)


        res = json.loads(response)
        rr = res['data']['projects'][-1]['appId']
        print('最后一个appId:',rr)





        # print(json.loads(response)['data'])
        #
        # if self.case_name == 'case001':
        #     self.assertEqual(json.loads(response)['code'],9003)
        # if self.case_name == 'login_err':
        #     self.assertEqual(result['code'],-1)
        # if self.case_name == 'login_null':
        #     self.assertEqual(result['code'],10001)






