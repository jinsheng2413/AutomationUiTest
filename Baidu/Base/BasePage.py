import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self):
        # 尝试打开safari浏览器
        try:
            self.driver = webdriver.Safari()
        except Exception:
            print('初始化浏览器出错')

    def open_url(self, url):
        # 打开url
        if url == '':
            print('请输入正确的url')
        else:
            self.driver.get(url)
            # 浏览器最大化
            self.driver.maximize_window()

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(loc))
            element = self.driver.find_element(*loc)
            return element
        except selenium.common.exceptions.NoSuchElementException:
            print('未找到此元素')

    def send_keys(self, loc, content, clear_first=True, click_first=True):
        try:
            loc = getattr(self, f"{loc}")
            if click_first:
                self.driver.find_element(*loc).click()
            if clear_first:
                self.driver.find_element(*loc).clear()
                self.driver.find_element(*loc).send_keys(content)
        except AttributeError:
            print('未能找到元素')

    def script(self, script):
        self.driver.execute_script(script)

    def quit(self):
        self.driver.quit()
