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
        self.homepage = HomePage(self.driver)

        # Asserting the website
        conf_title = self.homepage.confirmHomePage()
        self.logger.info("Asserting the Website")

        # Asserting the website
        if conf_title == "Inference One":
            assert True
            self.logger.info("Website Assertion Passed")
            self.driver.close()
        else:
            self.logger.error("Website Assertion Failed")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//homepage_fail.png")
            self.logger.info("Homepage Failed Screenshot Saved")
            self.driver.close()
            assert False

