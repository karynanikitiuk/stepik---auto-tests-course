from selenium import webdriver
import time
import math
    

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 

    link = "http://suninjuly.github.io/execute_script.html"

    browser = webdriver.Chrome()
    browser.get(link)



    x_element = browser.find_element_by_css_selector("#input_value")
    print('*****************', x_element)
    x = x_element.text
    y = calc(x)
    
       


    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option1 = browser.find_element_by_css_selector("#robotsRule")
    option1.click()

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()