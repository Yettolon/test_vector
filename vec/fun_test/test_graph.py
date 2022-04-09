import os
import time
from selenium import webdriver
from django.test import LiveServerTestCase

class FristTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def load_file(self):
        file = self.browser.find_element_by_id('file')
        current_dir = os.path.abspath(os.path.dirname(__file__)) 
        file_path = os.path.join(current_dir, 'test_input_file.xlsx')
        file.send_keys(file_path)
        
    def test_see_graph(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Vec', self.browser.title) 
        x = self.browser.find_element_by_class_name('dropdown-toggle')
        x.click()

        self.load_file()
        self.browser.find_element_by_id('wordvec').click()
        time.sleep(3)
        self.assertIn('Vec', self.browser.title) 
        self.load_file()
        self.browser.find_element_by_id('tfidfvectorizer').click()
        time.sleep(3)
        self.load_file()
        self.browser.find_element_by_id('countvectorizer').click()
        time.sleep(3)