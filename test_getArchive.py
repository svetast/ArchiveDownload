import time

import pytest
from HelperTestBase import HelperTestBase


class TestVessels(HelperTestBase):
    @pytest.mark.acceptance
    # @pytest.mark.skip()

    def test_getArchive(self):
        driver = self.driver
        driver.get('https://premier.ua/freerass.aspx')

        self.driver.find_element_by_xpath("//a[@href='javascript:void(0);']").click()
        time.sleep(3)

        i = 1
        while i < 31:
            elem = self.driver.find_elements_by_xpath('//a[text()="Скачать"]')
            elem[i].click()
            i += 1
