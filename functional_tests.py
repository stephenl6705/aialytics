from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_open_home_page(self):
        # Company A has heard about a cool new company called aialytics. She goes to
        # check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention aialytics
        self.assertIn('aialytics', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')