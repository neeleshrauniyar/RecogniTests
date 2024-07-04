import os
import pytest

from pageObjects.homePage import HomePage
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig, ReadModels


class TestSelectModels:
    logger = LogGen.loggen()
    baseURL = ReadConfig.getApplicationURL()

    @pytest.mark.regression
    def test_select_model(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("Testing Select Model")

        # Opening Homepage
        self.homepage = HomePage(self.driver)

        # Click on Toggle Button
        self.logger.info("Click on Select Model")
        select_model_text = self.homepage.selectModelType(ReadModels.get_diffusion_model())

        # Confirming the toggle functionality
        self.logger.info("Confirming the Select Model functionality")
        if select_model_text == "Diffusion Model" or select_model_text == 'Large Language Model':
            assert True
            self.logger.info("Select Model functionality passed")
            self.driver.close()
        else:
            self.logger.error("Select Model functionality failed")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//toggle_fail.png")
            self.driver.close()
            assert False
