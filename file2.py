from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
<<<<<<< HEAD
    browser.get(link)   
=======
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
>>>>>>> de0118c79a135f058c928618efd704b5b3561ec7
    input1 = browser.find_element_by_css_selector("div.first_block>div.form-group.first_class>input.form-control.first")
    input1.send_keys("Petr")
    input2 = browser.find_element_by_css_selector("div.first_block>div.form-group.second_class>input.form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.first_block>div.form-group.third_class>input.form-control.third")
<<<<<<< HEAD
    input3.send_keys("pp@mail.tu")  
    button = browser.find_element_by_css_selector("button.btn")
    button.click()  
    time.sleep(1)   
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text    
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
=======
    input3.send_keys("pp@mail.tu")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
>>>>>>> de0118c79a135f058c928618efd704b5b3561ec7
    browser.quit()
