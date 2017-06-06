from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_open_home_page(self):
        # Company A has heard about a cool new company called aialytics. She
        # goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title mentions aialytics
        self.assertIn('aialytics', self.browser.title)
        # header_text = self.browser.find_element_by_tag_name('h1').text
        # self.assertIn('aialytics',header_text)

        # At the top left of the page is the aialytics logo
        image = self.browser.find_element_by_tag_name('img')
        self.assertEqual(image.get_attribute('src'),
            'http://localhost:8000/static/aialytics.jpg')
        # At the top right of the page there are icons to LinkedIn, Twitter,
        # Facebook and rss (compare mindtools)

        # Below that we find a menu that will direct us to home, analytics,
        # ai tools, decision analysis and about us
        menu = self.browser.find_element_by_id('id_menu')
        rows = menu.find_elements_by_tag_name('li')
        self.assertTrue(
            any(row.text == 'Home' for row in rows)
        )
        self.assertTrue(
            any(row.text == 'Analytics' for row in rows)
        )
        self.assertTrue(
            any(row.text == 'AI Tools' for row in rows)
        )
        self.assertTrue(
            any(row.text == 'Decision Analysis' for row in rows)
        )
        self.assertTrue(
            any(row.text == 'About Us' for row in rows)
        )

        # The home page shows us: ...
        # - A row for Analytics, AI tools and Decision Analysis
        page = self.browser.find_element_by_id('id_page')
        rows = page.find_elements_by_tag_name('a')
        self.assertTrue(
            any(row.text == 'Analytics' for row in rows)
        )
        self.assertTrue(
            any(row.text == 'AI Tools' for row in rows)
        )
        self.assertTrue(
            any(row.text == 'Decision Analysis' for row in rows)
        )

        # The 'about us' section shows us: ...
        # - A description of who we are, what we do and how to contact us
        # - The industries that we are able to support
        # - A list of technology companies we work with in implementing
        #   solutions for our clients

        # The analytics page shows us: ...
        # - an example of an industry application

        # The ai tools page shows us: ...
        # - Links to various ai tools in the market to support analytics
        #   (e.g. datarobot)

        # The decision analysis page shows us: ...
        # - How are decisions made and how can we support this with bayesian
        #   decision analysis techniques
        
        # At the bottom left of the page it mentions 'aialytics 2017.
        # All rights reserved.'


if __name__ == '__main__':
    unittest.main(warnings='ignore')