from selenium.webdriver.support.wait import WebDriverWait
# from bases.config import Image_Path



class BaseAction(object):

    def __init__(self, driver,title,base_url):
        self.driver = driver
        self.title = title
        self.url = base_url



    def _open_browser(self,url,title):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            assert title in self.driver.title,'打开页面：'%url
        except:
            print('---')



    def getElement(self, *selector):
        """
        to locate element by selector
        :arg
        selector should be passed by an example with "(By.方式, '值')"
        (By.ID, 'username')
        :returns
        DOM element
        """
        try:
            WebDriverWait(self.driver,20).until(lambda driver:driver.find_element(*selector).is_displayed())
            return self.driver.find_element(*selector)
        except Exception as e:
            print('没找该元素：'+str(selector))
            raise e



    def click_el(self, *selector):
        """
        Operation click box.

        Usage:
        driver.click_ele(*(By.ID, 'username'))
        """
        self.getElement(*selector).click()



    def type(self, text,clear =True,*selector):
        """
        Operation input box.

        Usage:
        driver.type("i,el","selenium")
        """
        try:
            if clear:
                self.getElement(*selector).clear()
                self.getElement(*selector).send_keys(text)
        except:
            print('输入失败咯：'+str(selector))


    def select_date(self, id, date):
        ele = self.getElement(id)
        js = 'document.getElementById("'+id+'").removeAttribute("readonly")'
        self.driver.execute_script(js)
        ele.type(date)
        js1 = 'document.getElementById("'+id+'").click()'
        self.driver.execute_script(js1)

    # def img_screenshot(self,img_name):
    #     try:
    #         self.driver.get_screenshot_as_file(Image_Path+img_name+'.png')
    #     except Exception as e:
    #         print('截图失败：' + img_name)
    #         raise e

