import pytest
# import time, os, re, shutil, sys
import time, os
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from unittest import TestCase


class DriverTestCase(TestCase):

    # def test(self):
    #     driver = webdriver.Chrome()
    #     # driver = webdriver.Firefox()
    #     driver.get("https://rozetka.com.ua/ua/")
    #     driver.maximize_window()
    #     time.sleep(2)
    #     driver.find_element(By.XPATH, "//a[@class='menu-categories__link' and contains(.,'Смартфони')]").click()
    #     time.sleep(2)
    #     driver.find_element(By.XPATH, "//a[contains(@class,'tile-cats__heading') and contains(.,'Мобільні')]").click()
    #     time.sleep(2)
    #     driver.find_element(By.XPATH, "(//button[contains(@class,'buy-button')])[1]").click()
    #     time.sleep(2)
    #     driver.find_element(By.XPATH,
    #                         "//li[contains(@class,'cart')]/*/button[contains(@class,'header__button')]").click()
    #     time.sleep(2)
    #     # counter = driver.find_element(By.XPATH, "//input[@data-testid='cart-counter-input']").text
    #     # print(counter)
    #     # print("hvchjvjvjvh")
    #     # //a[@data-testid='title']
    #     # ------------------------------------------------------------
    #     chosen_goods = []
    #     length = 0
    #     chosen_filtersText = driver.find_elements(By.XPATH, "//a[@data-testid='title']")
    #     for i in chosen_filtersText:
    #         chosen_goods.append(str(i.text))
    #     length = chosen_goods.__len__()
    #     print("\nGods in basket: ", length)
    #     # ------------------------------------------------------------
    #     # assert "Python" in driver.title
    #     # elem = driver.find_element(By.NAME, "q")
    #     # elem.clear()
    #     # elem.send_keys("pycon")
    #     # elem.send_keys(Keys.RETURN)
    #     # assert "No results found." not in driver.page_source
    #     assert length == 1
    #     assert True
    #     driver.close()

    def test_rozetka(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument("--log-level=1")
        options.add_argument("--start-maximized")
        # options.binary_location = "/opt/headless-chromium"
        # chromedriver_path = "/opt/chromedriver"
        driver = webdriver.Chrome(options=options)
        # driver.get("https://www.youtube.com/")
        driver.get("https://rozetka.com.ua/ua/")
        assert True
