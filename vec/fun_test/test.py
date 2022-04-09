import os
from selenium import webdriver
from django.test import LiveServerTestCase

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

    
    def test_load_file_xlsx(self):
        self.browser.get(self.live_server_url)
        file = self.browser.find_element_by_id('file')
        current_dir = os.path.abspath(os.path.dirname(__file__)) 
        file_path = os.path.join(current_dir, 'test_input_file.xlsx')
        file.send_keys(file_path)
    
    def test_load_csv(self):
        self.browser.get(self.live_server_url)
        file = self.browser.find_element_by_id('file')
        current_dir = os.path.abspath(os.path.dirname(__file__)) 
        file_path = os.path.join(current_dir, 'test_input_file.csv')
        file.send_keys(file_path)
    


