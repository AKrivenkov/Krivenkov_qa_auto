from selenium import webdriver
import time, math
browser = webdriver.Chrome()
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)

    x_element = browser.find_element(by='id', value='input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(by='id', value='answer')
    input1.send_keys(y)

    option1 = browser.find_element(by='id', value='robotCheckbox')
    option1.click()
    option2 = browser.find_element(by='id', value='robotsRule')
    option2.click()
    button = browser.find_element(by='css selector', value='button.btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()