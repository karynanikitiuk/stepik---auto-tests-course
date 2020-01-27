import pytest
from selenium import webdriver
import time
import math


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    yield browser
    browser.quit()

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class TestFeedback(object):
    def test_first(self, links, browser):
        link = f"{links}"
        browser.get(link)

        answer = math.log(int(time.time()))

        input1 = browser.find_element_by_css_selector("#ember67")
        input1.send_keys(str(answer))

        button = browser.find_element_by_css_selector(".submit-submission")
        button.click()

        message = browser.find_element_by_css_selector(".smart-hints__hint")
        assert "Correct!" in message.text
