from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el_txt = browser.find_element(By.XPATH, "//h2")    
    nums = re.findall(r'\d+', el_txt.text)
    res = sum(map(int, nums))
    print(f"{el_txt.text}, {nums}, {res}")
    
    # sel1 = browser.find_element(By.XPATH, "//select[@id='dropdown']")
    xp = f"//option[@value='{res}']"
    print(xp)    
    # sel1.click()
    time.sleep(2)        
    sel2 = browser.find_element(By.XPATH, xp)
    sel2.click()
    time.sleep(1)

    btn_submit = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")    
    btn_submit.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
