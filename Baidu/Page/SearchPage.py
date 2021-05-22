from Baidu.Base.BasePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class SearchPage(BasePage):
    search_loc = (By.ID, 'kw')
    btn_loc = (By.ID, 'su')

    def search_content(self, content):
        search_element = self.find_element(*self.search_loc)
        search_element.send_keys(content)

    def click_button(self):
        button = self.find_element(*self.btn_loc)
        button.click()


# if __name__ == '__main__':
#     BaiduSearch = SearchPage()
#     BaiduSearch.open_url('http://www.baidu.com')
#     BaiduSearch.search_content('12306')
#     BaiduSearch.click_button()
#     sleep(5)
#     BaiduSearch.quit()
