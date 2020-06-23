import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait



class HelperTestBase(unittest.TestCase):


    def setUp(self, OS='Linux', browser='Chrome'):

        self.base_url = 'https://premier.ua/oldarchive.aspx'

        if browser == 'Proxy':

            PROXY = "192.168.0.103:8080"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % PROXY)
            self.driver = webdriver.Chrome(chrome_options=chrome_options)

        ### Tests can run Chrome Incognito mode:
        if browser == 'Incognito':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            self.driver = webdriver.Chrome(chrome_options=chrome_options)

        ### Tests can run without UI using Headless Browser:

        if browser == 'Chrome_Headless': ### Tests can run without UI using Chrome Headless Browser
            chrome_options = Options()
            chrome_options.add_argument("headless")
            self.driver = webdriver.Chrome(chrome_options=chrome_options)

        if browser == 'Firefox_headless': ### Tests can run without UI using Firefox Headless Browser
            options = FirefoxOptions()
            options.add_argument("--headless")
            self.driver = webdriver.Firefox(options=options)



        if browser == 'Chrome':
            if OS == 'Linux':
                self.driver = webdriver.Chrome('chromedriver')
            if OS == 'Windows':
                self.driver = webdriver.Chrome("C:\Windows\chromedriver.exe")

        if browser == 'Firefox':
            if OS == 'Linux':
                self.driver = webdriver.Firefox(executable_path='/home/sveta/workspase/fishfacts-test')
            if OS == 'Windows':
                    self.driver = webdriver.Firefox(executable_path="C:\Windows\geckodriver.exe")

        if browser == 'Edge':
            self.driver = webdriver.Edge(executable_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            # if OS == 'Windows':
            #   self.driver = webdriver.Ie(executable_path="C:\Windows\IEDriverServer_Win32_3.14.0\IEDriverServer.exe")


        if browser == 'IE':
            if OS == 'Windows':
              self.driver = webdriver.Ie(executable_path="C:\Windows\IEDriverServer_Win32_3.14.0\IEDriverServer.exe")

        # if env == 'demo':
        #     self.base_url = 'https://demo.fishfacts.fo/#/'
        #
        # if env == 'test':
        #     self.base_url = 'https://test.fishfacts.fo/#/'
        #
        # if env == "prod":
        #     #self.base_url = 'https://www.fishfacts.fo/#/'
        #     self.base_url = 'https://www.fishfacts.com/#/'

        self.driver.implicitly_wait(200)
        self.driver.set_window_size(1366,768)
        #self.driver.set_window_size(320,568)
        #self.driver.maximize_window()







    def tearDown(self):
        self.driver.quit()







if __name__ == "__main__":
    unittest.main()



    ############# Don't REMOVE !!!!!!!!!!!!!!!!!    #####################





    # Set the mobile device:



    #######

    # mobile_emulation = {
    #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 7.0; PRA-LA1 Build/HUAWEIPRA-LA1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"}
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # self.driver = webdriver.Chrome(chrome_options=chrome_options)






    # # Select which device you want to emulate by uncommenting it:
    # mobile_emulation = {"deviceName": "Nexus 5"}
    #
    # # Define a variable to hold all the configurations we want:
    # chrome_options = webdriver.ChromeOptions()
    #
    # # Add the mobile emulation to the chrome options variable:
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # # Create driver, pass it the path to the chromedriver file and the special configurations you want to run:
    # self.driver = webdriver.Chrome(
    #     executable_path='chromedriver', chrome_options=chrome_options)


    ##### or set device:


    # mobile_emulation = {
    #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 7.0; PRA-LA1 Build/HUAWEIPRA-LA1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"}
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # self.driver = webdriver.Chrome(chrome_options=chrome_options)





    ##### the universal metod  using on web pages: ##########
