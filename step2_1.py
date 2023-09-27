from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el_txt = browser.find_element(By.XPATH, "//span[@id='input_value']")
    num = int(el_txt.text)
    print(num)
    res = calc(num)

    time.sleep(1)

    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(res)

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
    