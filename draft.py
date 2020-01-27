import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1"])
class TestFeedback(object):
    def test_first(self, links):
        browser = webdriver.Chrome()

        link = f"{links}"
        browser.get(link)
        browser.implicitly_wait(10)


        answer = math.log(int(time.time()))
        print(answer)

        input1 = browser.find_element_by_css_selector("#ember67")
        input1.send_keys(str(answer))

        button = browser.find_element_by_css_selector(".submit-submission")
        button.click()
        
        browser.implicitly_wait(10)

        message = browser.find_element_by_css_selector(".smart-hints__hint")

        assert "Correct!" in message.text
        print(message.text)

#    def test_second(self, browser, links):
#        # этот тест тоже запустится дважды
#        link = f'{links}
#        browser.get(link)
#        browser.find_element_by_css_selector("#login_link")