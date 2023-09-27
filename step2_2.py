from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el = browser.find_element(By.XPATH, "//img[@id='treasure']")
    # print(el.get_attribute("valuex"), type(el.get_attribute("valuex")))
    
    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(calc(int(el.get_attribute("valuex"))))

    ch_box1 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    ch_box1.click()

    r_btn1 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    r_btn1.click()

    bnt_submit = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    bnt_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
