import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import pytest
from HelperTestBase.HelperTestBase import HelperTestBase


class Test_up_Dom(HelperTestBase):
    # @pytest.mark.skip()

    def test_up_Dom(self, username="an_alf@ukr.net", password="20alf25"):
        driver = self.driver
        driver.get("http://dom.kharkov.ua/login/php")

        wait = WebDriverWait(self.driver, 30)
        elem = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='login']")))
        ActionChains(self.driver).move_to_element(elem).click().send_keys(username).perform()

        wait = WebDriverWait(self.driver, 30)
        elem = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        ActionChains(self.driver).move_to_element(elem).click().send_keys(password).perform()

        wait = WebDriverWait(self.driver, 30)
        elem = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@value='Войти']")))
        ActionChains(self.driver).move_to_element(elem).click().perform()
        time.sleep(3)

        driver.get("http://www.dom.kharkov.ua/panel.php?status=all&object=all&srv=ob&view=objects&op=list")

        i = 0
        while i < 20:

            time.sleep(2)
            elem = self.driver.find_elements_by_xpath("//img[@title='Продлить']")
            elem[i].click()
            driver.back()
            i += 1



