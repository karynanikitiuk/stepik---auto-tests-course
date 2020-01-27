from selenium import webdriver


import unittest

class TestAbs(unittest.TestCase):

    def test_abs1(self):

        self.link = "http://suninjuly.github.io/registration1.html"
#        link = "http://suninjuly.github.io/registration2.html"
    
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
    
        self.input1 = self.browser.find_element_by_css_selector(".first_block > .form-group.first_class > .form-control.first")
        self.input1.send_keys("Ivan")
        self.input2 = self.browser.find_element_by_css_selector(".first_block > .form-group.second_class > .form-control.second")
        self.input2.send_keys("Petrov")
        self.input3 = self.browser.find_element_by_css_selector(".first_block > .form-group.third_class > .form-control.third")
        self.input3.send_keys("Email")
    
        self.button = self.browser.find_element_by_css_selector("button.btn")
        self.button.click()
    
    
    
        self.browser.implicitly_wait(5)
    
        self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
    
        self.welcome_text = self.welcome_text_elt.text
    
        self.assertEqual("Congratulations! You have successfully registered!" , self.welcome_text)

    def test_abs2(self):
        self.link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
    
        self.input1 = self.browser.find_element_by_css_selector(".first_block > .form-group.first_class > .form-control.first")
        self.input1.send_keys("Ivan")
        self.input2 = self.browser.find_element_by_css_selector(".first_block > .form-group.second_class > .form-control.second")
        self.input2.send_keys("Petrov")
        self.input3 = self.browser.find_element_by_css_selector(".first_block > .form-group.third_class > .form-control.third")
        self.input3.send_keys("Email")
    
        self.button = self.browser.find_element_by_css_selector("button.btn")
        self.button.click()
    
    
        self.browser.implicitly_wait(5)
    
        
    
        self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
    
        self.welcome_text = self.welcome_text_elt.text
    
        self.assertEqual("Congratulations! You have successfully registered!" , self.welcome_text)

        
if __name__ == "__main__":
    unittest.main()