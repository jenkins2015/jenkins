#coding:utf-8

from selenium import webdriver
import unittest

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "http://www.baidu.com"
        self.title = u"百度一下，你就知道"

    def testTitle(self):
        self.driver.get(self.url)

        self.assertEqual(self.driver.title,self.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

