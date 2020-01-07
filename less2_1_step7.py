from selenium import webdriver
#from selenium.webdriver.common.by import By

import time
import math
    

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 

    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)




    x_el = browser.find_element_by_id("treasure")

    x_element = x_el.get_attribute("valuex")
    y = calc(x_element)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
