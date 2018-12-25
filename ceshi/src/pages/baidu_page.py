from selenium.webdriver.common.by import By

from  src.common.base_page import BasePage


class BaiduPage(BasePage):
    # 定位器
    keywords_loc = (By.ID, 'kw')
    submit_loc = (By.ID, 'su')
    hao123_loc = (By.LINK_TEXT, 'hao123')
    more_loc = (By.LINK_TEXT, '更多产品')
    zhidao_loc = (By.LINK_TEXT,'知道')

    #   打开页面
    def open(self):
        self._open(self.url, self.title)

    #   输入关键词
    def input_keywords(self, keywords):
        self.find_element(*self.keywords_loc).send_keys(keywords)

    #   点击搜索按钮
    def click_submit(self):
        self.find_element(*self.submit_loc).click()