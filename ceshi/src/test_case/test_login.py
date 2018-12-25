from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from src.pages.login import Login_Page
import pytest
import unittest

class Test_Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.yunlinye.com/login.html'
        self.login = Login_Page(self.driver,'登录',self.url)

    def test_01(self):
        try:
            self.login.open()
            self.login.log_in('map','gzshili@map1')
            sleep(2)
            # self.error_loc = self.driver.find_element_by_id('error')
            self.assertIn('用户名或密码错误',self.login.error_msg())
        except:
            print('出错了 看看在哪')

    def tearDown(self):
        self.driver.quit()