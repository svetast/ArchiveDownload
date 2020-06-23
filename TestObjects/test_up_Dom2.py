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


class Test_up_Dom2(HelperTestBase):
    # @pytest.mark.skip()

    def test_up_Dom2(self, username="alf_an", password="melya43"):
        driver = self.driver
        driver.get("http://www.dom.kharkov.ua/users/login.php")

        wait = WebDriverWait(self.driver, 30)
        elem = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='login']")))
        ActionChains(self.driver).move_to_element(elem).click().send_keys(username).perform()

        wait = WebDriverWait(self.driver, 30)
        elem = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        ActionChains(self.driver).move_to_element(elem).click().send_keys(password).perform()

        wait = WebDriverWait(self.driver, 30)
        elem = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@value='OK']")))
        ActionChains(self.driver).move_to_element(elem).click().perform()
        time.sleep(3)





        # i = 0
        # while i < 10:

        time.sleep(1)
        elem = self.driver.find_elements_by_xpath("//a[@title='Поднять в начало списка в выдаче. Операцию можно повторять каждых 12 часов']")
        elem[0].click()
        elem[1].click()
        elem[2].click()
        elem[3].click()
        elem[4].click()

        #elem[i].click()
        #i += 1



