from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    money = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "$100")
    )
    money = browser.find_element(By.XPATH, "//h5[@id='price']").text
    print(money)
    browser.find_element(By.XPATH, "//button[@id='book']").click()

    res = calc(browser.find_element(By.XPATH, "//span[@id='input_value']").text)
    print(browser.find_element(By.XPATH, "//span[@id='input_value']").text, res)
    
    txt_area = browser.find_element(By.XPATH, "//input[@id='answer']")
    txt_area.send_keys(res)
    
    browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    