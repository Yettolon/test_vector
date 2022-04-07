from selenium import webdriver
from django.test import LiveServerTestCase
import time
class FristTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_first_button(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Vec', self.browser.title) 
        x = self.browser.find_element_by_class_name('dropdown-toggle')
        x.click()
        time.sleep(10)
