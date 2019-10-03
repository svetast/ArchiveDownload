import unittest

from selenium import webdriver



class HelperTestBase(unittest.TestCase):
    def setUp(self):



        self.driver = webdriver.Chrome("C:\Windows\chromedriver.exe")
        self.base_url = 'https://premier.ua/oldarchive.aspx'

        self.driver.implicitly_wait(200)
        #self.driver.set_window_size(320 , 568)
        self.driver.maximize_window()



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
