from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, selenium_driver, base_url, page_title):
        self.driver = selenium_driver
        self.url = base_url
        self.title = page_title


    #   打开页面,并校验链接是否加载正确
    def _open(self, url, page_title):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
#           通过断言输入的title是否在当前title中
            assert page_title in self.driver.title, '打开页面失败：%s' % url
        except:
            print('失败')

    #   重写find_element方法，增加定位元素的健壮性
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element(*loc).is_displayed())
            #WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print('找不到元素:'+str(loc))

    #   重写send_keys方法
    def send_keys(self, value, clear=True, *loc):
        try:
            if clear:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print('输入失败,loc='+str(loc)+u';value='+value)