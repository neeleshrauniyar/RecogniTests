import time

import pytest

from pageObjects.homePage import HomePage
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig, ReadLLMParameters


class TestCopyFunctionality:
    logger = LogGen.loggen()
    baseUrl = ReadConfig.getApplicationURL()

    @pytest.mark.regression
    def test_copy_functionality(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.logger.info("Testing Copy Functionality")

        # Opening Homepage
        self.homepage = HomePage(self.driver)

        # Selecting fields
        self.logger.info("Selecting the fields")
        self.homepage.selectModel(ReadLLMParameters.get_model())
        self.homepage.selectPrompt(ReadLLMParameters.get_prompt())
        self.homepage.selectBatchSize(ReadLLMParameters.get_batch_size())
        self.homepage.selectTensorParallelism(ReadLLMParameters.get_tensor_parallelism())

        # Running the simulation
        self.logger.info("Running the simulation")
        self.homepage.clickRunSimulation()
        time.sleep(10)  # waiting for the simulation to be completed

        # Copying the text in the outputbox
        self.logger.info("Copying the text from recogni and competitor outputbox")
        recogni_text = self.homepage.click_copy_recogni()
        competitor_text = self.homepage.click_copy_competitor()

        # Match the text
        self.logger.info("Matching the copied text")
        if recogni_text == self.homepage.get_recogni_output_text() and competitor_text == self.homepage.get_competitor_output_text():
            assert True
            self.logger.info("Copied Text Matched: Copy Functionality Passed")
            self.driver.close()
        else:
            self.logger.error("Copied Text did not Match: Copy Functionality Failed")
            self.driver.close()
            assert False
