from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select



#def calc(x):
#    return str(math.log(abs(12*math.sin(int(x)))))

try: 

    link = "http://suninjuly.github.io/selects2.html"

    browser = webdriver.Chrome()
    browser.get(link)



    x_element = browser.find_element_by_css_selector("#num1")
    x = x_element.text
    print('*****************', x)

    y_element = browser.find_element_by_css_selector("#num2")
    y = y_element.text
    print('*****************', y)
 
    z = str(int(x) + int(y))
    print('*****************', z)    

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text('%s' % z) 

#    input1 = browser.find_element_by_id("answer")
#    input1.send_keys(y)
#    option1 = browser.find_element_by_css_selector("#robotCheckbox")
#    option1.click()
#    option1 = browser.find_element_by_css_selector("#robotsRule")
#    option1.click()

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()