import os
import pytest

from pageObjects.homePage import HomePage
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig


class TestHomePage:
    logger = LogGen.loggen()
    baseURL = ReadConfig.getApplicationURL()

    @pytest.mark.sanity
    def test_homepage(self, setup):
        self.driver = setup
        self.logger.info("Opening Website")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("Opened Website")

        self.homepage= HomePage(self.driver)

        #Confirm Homepage
        result= self.homepage.confirmHomePage()

        #Assert
        if result==True:
            assert True
            self.logger.info("Test Passed")
            self.driver.close()
        else:
            self.logger.info("Test Failed")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//homepage_fail.png")
            assert False

            self.driver.close()

