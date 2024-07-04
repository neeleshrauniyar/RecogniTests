import os
import pytest

from pageObjects.homePage import HomePage
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig, ReadKPIs


class TestSliderDemoSimulation:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_slider_demo_simulation(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.logger.info("Testing Slider Demo Simulation Functionality")

        # Opening Homepage
        self.homepage = HomePage(self.driver)

        # Toggle to Slider Demo
        self.logger.info("Toggle to slider mode")
        self.homepage.toggle_slider_demo()

        # Move the slider parameters
        self.logger.info("Move sliders in all fields")
        self.homepage.slide_input_token()
        self.homepage.slide_output_token()
        self.homepage.slide_batch_size()
        self.homepage.slide_tensor_paralleilism()

        self.driver.implicitly_wait(5)

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
            self.logger.info("Slider Demo Simulation Run passed with KPIs")
            self.driver.close()
        else:
            self.logger.error("Slider Demo Simulation Run failed with KPIs")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//slider_demo_simulation_fail.png")
            self.driver.close()
            assert False
