import unittest
from Baidu.Page.SearchPage import SearchPage
from time import sleep
from Baidu.tools.ReadConfig import ReadConfig


class TestSearch(unittest.TestCase):
    def setUp(self) -> None:
        # self.url = 'http://www.baidu.com'
        self.content = '12306'
        self.search_case = SearchPage()
        print('测试开始')

    def tearDown(self) -> None:
        print('测试结束')
        self.search_case.quit()

    def test_search(self):
        # self.search_case.open_url(self.url)
        self.search_case.open_url(ReadConfig('../tools/test.ini').get_config('url', 'baidu'))
        self.search_case.search_content(self.content)
        self.search_case.click_button()
        sleep(5)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestSearch('test_search'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)
