import os
import pytest

from pageObjects.homePage import HomePage
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig, ReadDiffusionParameters, ReadKPIs, ReadModels


class TestDiffusionSimulation:
    logger = LogGen.loggen()
    baseURL = ReadConfig.getApplicationURL()
    read_diffusion_parameters = ReadDiffusionParameters()

    @pytest.mark.regression
    def test_runSimulation(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("Testing Diffusion Model Simulation")

        # Opening Homepage
        self.homepage = HomePage(self.driver)

        # Select diffusion model
        self.logger.info("Select Diffusion Mode")
        self.homepage.selectModelType(ReadModels.get_diffusion_model())

        # Select the inputs
        self.logger.info("Selecting the fields")
        self.homepage.selectModel(self.read_diffusion_parameters.get_model())
        self.homepage.selectPrompt(self.read_diffusion_parameters.get_prompt())
        self.homepage.selectBatchSize(self.read_diffusion_parameters.get_batch_size())
        self.homepage.selectTensorParallelism(self.read_diffusion_parameters.get_tensor_parallelism())

        # Run Simulation
        self.logger.info("Running Diffusion Simulation")
        self.homepage.clickRunSimulation()

        # Confirm Simulation Run with KPIs
        self.logger.info("Confirming the Diffusion Simulation")
        latency = self.homepage.get_latency()
        images_per_second = self.homepage.get_images_per_second()
        images_per_second_per_user = self.homepage.get_images_per_second_per_user()
        total_power_consumption = self.homepage.get_total_power_consumption()
        tco = self.homepage.get_tco()
        efficiency = self.homepage.get_efficiency()
        if (latency == ReadKPIs.read_kpi_latency() and
                images_per_second == ReadKPIs.read_kpi_images_per_second() and
                images_per_second_per_user == ReadKPIs.read_kpi_images_per_second_per_user() and
                total_power_consumption == ReadKPIs.read_kpi_total_power_consumption() and
                tco == ReadKPIs.read_kpi_tco() and
                efficiency == ReadKPIs.read_kpi_efficiency()
        ):
            assert True
            self.logger.info("Diffusion Simulation Run Completed Successfully")
            self.driver.close()
        else:
            self.logger.error("Diffusion Simulation Run could not be completed")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//run_diffusion_simulation_fail.png")
            self.driver.close()
            assert False
