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

        # She notices the page title and header mention aialytics
        self.assertIn('aialytics', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('aialytics',header_text)

        # At the top left of the page is the aialytics logo
        image = self.browser.find_element_by_tag_name('img')
        self.assertEqual(image.get_attribute('src'), 
            '//www.aialytics.com/media/aialytics.jpg')
        # At the top right of the page there are icons to LinkedIn, Twitter,
        # Facebook and rss (compare mindtools)

        # Below that we find a menu that will direct us to home, analytics,
        # ai tools, decision analysis and our partners

        # The home page shows us: ...
        # - A column for Analytics, AI tools and Decision Analysis
        # - Get insight from your data using advanced data analytics and ai
        #   techniques
        # - Development of algorithms and data analytics solutions that can be
        #   integrated into your ai solutions (incl. apps)
        # - Support your decisions with advanced bayesian decision analysis

        # The about us page shows us: ...
        # - A description of who we are, what we do and how to contact us
        # - The industries that we are able to support

        # The blog page shows us: ...
        # - an example of an industry application

        # The ai tools page shows us: ...
        # - Links to various ai tools in the market to support analytics
        #   (e.g. datarobot)

        # The our partners page shows us: ...
        # - A list of technology companies we work with in implementing
        #   solutions for our clients

        # At the bottom left of the page it mentions 'aialytics 2017.
        # All rights reserved.'


if __name__ == '__main__':
    unittest.main(warnings='ignore')