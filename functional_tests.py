from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_app(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('Quiz', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
   unittest.main(warnings='ignore')