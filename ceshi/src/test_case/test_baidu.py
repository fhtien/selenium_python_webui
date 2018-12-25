import unittest
from selenium import webdriver
from src.pages.baidu_page import BaiduPage
from time import sleep
'''
project:百度页面测试
'''
class TestBaiduSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = 'https://www.baidu.com/'
        self.keyword = 'python'
        self.baidu_page = BaiduPage(self.driver, self.url, '百度')

    def test_baidu_search(self):
        '''百度搜索'''
        try:
            self.baidu_page.open()
            self.baidu_page.input_keywords(self.keyword)
            self.baidu_page.click_submit()
            sleep(2)
            self.assertIn(self.keyword, self.driver.title)
        except Exception as e:

            raise e
    def tearDown(self):
        self.driver.quit()