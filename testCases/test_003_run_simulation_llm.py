import os
import pytest
import time

from pageObjects.homePage import HomePage
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig, ReadLLMParameters, ReadKPIs


class TestRunSimulationLLM:
    logger = LogGen.loggen()
    baseURL = ReadConfig.getApplicationURL()
    read_llm_parameters = ReadLLMParameters()

    @pytest.mark.regression
    def test_runSimulation(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Opening Hompage
        self.homepage = HomePage(self.driver)

        # Selecting fields
        self.logger.info("LLM Simulation Begins")
        self.logger.info("Selecting the models, prompts, batchsize, and tensorflow")
        self.homepage.selectModel(self.read_llm_parameters.get_model())
        self.homepage.selectPrompt(self.read_llm_parameters.get_prompt())
        self.homepage.selectBatchSize(self.read_llm_parameters.get_batch_size())
        self.homepage.selectTensorParallelism(self.read_llm_parameters.get_tensor_parallelism())

        # Running the simulation
        self.logger.info("Running the LLM simulation")
        self.homepage.clickRunSimulation()
        time.sleep(45)

        # Confirming the simulation run with KPIs
        self.logger.info("Confirming the simulation")
        ttft = self.homepage.get_ttft()
        tpot = self.homepage.get_tpot()
        tokens_per_second = self.homepage.get_tokens_per_sec()
        total_power_consumption = self.homepage.get_total_power_consumption()
        tco = self.homepage.get_tco()
        efficiency = self.homepage.get_efficiency()

        if (ttft == ReadKPIs.read_kpi_ttft() and
                tpot == ReadKPIs.read_kpi_tpot() and
                tokens_per_second == ReadKPIs.read_kpi_tokens_per_sec() and
                total_power_consumption == ReadKPIs.read_kpi_total_power_consumption() and
                tco == ReadKPIs.read_kpi_tco() and
                efficiency == ReadKPIs.read_kpi_efficiency()
        ):
            assert True
            self.logger.info("LLM Simulation Run passed with KPIs")
        else:
            self.logger.error("LLM Simulation Run failed with KPIs")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//runSimulation_llm_fail.png")
            assert False

        # Asserting simulation run with output texts
        recogni_output_text = self.homepage.get_recogni_output_text()
        competitor_output_text = self.homepage.get_competitor_output_text()
        # print(recogni_output_text)
        # print(competitor_output_text)
        if recogni_output_text == competitor_output_text:
            assert True
            self.logger.info("Recogni and Competitor output text matched: LLM Simulation Passed")
            self.driver.close()
        else:
            self.logger.error("Recogni and Competitor output text did not match: LLM Simulation Failed")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//runSimulation__llm_fail.png")
            self.driver.close()
            assert False
