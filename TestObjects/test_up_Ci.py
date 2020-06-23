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


class Test_up_Ci(HelperTestBase):

    # @pytest.mark.skip()

    def test_up_Ci(self, username="alf_an", password="1997alf2025"):
        driver = self.driver
        driver.get('https://ci.ua/accounts/login')

        wait = WebDriverWait(self.driver, 30)
        elem = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        ActionChains(self.driver).move_to_element(elem).click().send_keys(username).perform()

        wait = WebDriverWait(self.driver, 30)
        elem = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        ActionChains(self.driver).move_to_element(elem).click().send_keys(password).perform()

        wait = WebDriverWait(self.driver, 30)
        elem = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
        ActionChains(self.driver).move_to_element(elem).click().perform()

        time.sleep(3)
        driver.get("https://ci.ua/accounts/profile")

        # wait = WebDriverWait(self.driver, 30)
        # elem = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[text()='Обновить']")))
        # ActionChains(self.driver).move_to_element(elem).click().perform()
        # time.sleep(2)
        #
        # wait = WebDriverWait(self.driver, 30)
        # elem = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[text()='Обновить']")))
        # ActionChains(self.driver).move_to_element(elem).click().perform()
        # time.sleep(2)
        #
        # try:
        #     alert = self.driver.switch_to_alert()
        #     alert.accept()
        #
        # except:
        #     print
        #     "no alert"

        i = 0
        while i < 20:
            #driver.get("https://ci.ua/accounts/profile")
            time.sleep(2)
            elem = self.driver.find_elements_by_xpath("//button[text()='Обновить']")
            elem[i].click()
            elem[i].click()
            i += 1




            ''' DOM
            
            wait = WebDriverWait(self.driver, 30)
        elem = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='login']")))
        ActionChains(self.driver).move_to_element(elem).click().send_keys(username).perform()

        wait = WebDriverWait(self.driver, 30)
        elem = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        ActionChains(self.driver).move_to_element(elem).click().send_keys(password).perform()

        wait = WebDriverWait(self.driver, 30)
        elem = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@value='Войти']")))
        ActionChains(self.driver).move_to_element(elem).click().perform()'''






















            '''@Test
    public void upDom1() throws InterruptedException {
        driver.get("http://dom.kharkov.ua/login/php");
        driver.findElement(By.name("login")).sendKeys("hryack@ukr.net");
        Thread.sleep((long) (Math.random() * 1000));
        driver.findElement(By.name("password")).sendKeys("20alf25");
        Thread.sleep((long) (Math.random() * 1000));
        driver.findElement(By.xpath(Buttonlocator)).click();

        for (int n = 0; n < 10; n++) {
            driver.findElement(By.xpath("//img[@title='Продлить']")).click();
            Thread.sleep((long) (Math.random() * 1000));
            driver.navigate().back();


        }
    }
'''
