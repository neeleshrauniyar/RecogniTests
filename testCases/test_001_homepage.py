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

