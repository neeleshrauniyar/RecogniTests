import pyperclip
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    text_title_xpath = "//h1[1]"

    # toggle locators
    text_selectModel_xpath = "//select[1]"
    text_llmModel_xpath = "//select[1]/option[1]"
    text_diffusionModel_xpath = "//select[1]/option[2]"

    # Run Simulation Locators
    dropdown_chooseModel_css = "//select[2]"
    dropdown_options_chooseModel = "//select[2]//option"
    dropdown_choosePrompt_css = "//select[3]"
    dropdown_options_choosePrompt = "//select[3]//option"
    dropdown_batchSize_css = "//select[4]"
    dropdown_options_chooseBatchSize = "//select[4]//option"
    dropdown_tensorParallelism_css = "//select[5]"
    dropdown_options_chooseTensorParallelism = "//select[5]//option"

    # output boxes
    text_outputboxrecogni_xpath = "//pre[1]"
    text_outputboxcompetitor_xpath = "//div[@id='simulationBox']//div[2]//pre[1]"

    # Run Simulation button
    button_runSimulation_xpath = "//button[normalize-space()='Run Simulation']"

    # Copy button
    icon_copyrecogni_xpath = "//div[@id='simulationBox']/div[1]/div/span[2]"
    icon_copycompetitor_xpath = "//div[@id='simulationBox']//div[2]//div[1]//span[2]"

    # Clear Button
    button_clear_xpath = "//button[normalize-space()='Clear']"

    # KPIs Common for LLM and Slider
    kpi_ttft_xpath = "//span[normalize-space()='TTFT']"
    kpi_tpot_xpath = "//span[normalize-space()='TPOT']"
    kpi_tokensPerSec_xpath = "//span[normalize-space()='Tokens/Sec']"

    # KPIs for Diffusion Model
    kpi_latency_xpath = "//span[normalize-space()='Latency']"
    kpi_imagesPerSecond_xpath = "//span[normalize-space()='Images/Sec']"
    kpi_imagesPerSecondPerUser_xpath = "//span[normalize-space()='Images/Sec/User']"

    # Common KPI for all Models
    kpi_tpo_xpath = f"//span[normalize-space()='Total Power Consumption']"
    kpi_tco_xpath = "//span[normalize-space()='TCO']"
    kpi_efficiency_xpath = "//span[normalize-space()='Efficiency']"

    # Toast Messages
    toast_selectmodel_xpath = "//div[@class='Toastify']/div/div/div/div[2]"

    # Slider Demo
    button_sliderDemo_xpath = "//div[@id='simulationNav']/span[2]"

    # slider parameters
    slider_inputTokens_xpath = "//div[starts-with(@class,'slider-custom-box')][1]/span/span[17]"
    slider_outputTokens_xpath = "//div[starts-with(@class,'slider-custom-box')][2]/span/span[17]"
    slider_batchSize_xpath = "//div[starts-with(@class,'slider-custom-box')][3]/span/span[13]"
    slider_tensorParallelism_xpath = "//div[starts-with(@class,'slider-custom-box')][4]/span/span[19]"

    # Actions
    def confirmHomePage(self):
        return self.driver.find_element(By.XPATH, self.text_title_xpath).text

    def selectModelType(self, model_name):
        toggle_models = Select(self.driver.find_element(By.XPATH, self.text_selectModel_xpath))
        toggle_models.select_by_visible_text(model_name)
        return self.driver.find_element(By.XPATH, self.text_diffusionModel_xpath).text

    def selectModel(self, model):
        models = Select(self.driver.find_element(By.XPATH, self.dropdown_chooseModel_css))
        models.select_by_value(model)

    def selectPrompt(self, prompt):
        prompts = Select(self.driver.find_element(By.XPATH, self.dropdown_choosePrompt_css))
        prompts.select_by_value(prompt)

    def selectBatchSize(self, batch_size):
        batchSize = Select(self.driver.find_element(By.XPATH, self.dropdown_batchSize_css))
        batchSize.select_by_value(batch_size)

    def selectTensorParallelism(self, tensor_parallelism):
        tensorflow = Select(self.driver.find_element(By.XPATH, self.dropdown_tensorParallelism_css))
        tensorflow.select_by_value(tensor_parallelism)

    def clickRunSimulation(self):
        runSimulation = self.driver.find_element(By.XPATH, self.button_runSimulation_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", runSimulation)
        self.driver.execute_script("arguments[0].click();", runSimulation)

    # Get KPIs
    def get_ttft(self):
        kpi_name = self.driver.find_element(By.XPATH, self.kpi_ttft_xpath).text
        return kpi_name

    def get_tpot(self):
        kpi_name = self.driver.find_element(By.XPATH, self.kpi_tpot_xpath).text
        return kpi_name

    def get_tokens_per_sec(self):
        kpi_name = self.driver.find_element(By.XPATH, self.kpi_tokensPerSec_xpath).text
        return kpi_name

    def get_total_power_consumption(self):
        kpi_name = self.driver.find_element(By.XPATH, self.kpi_tpo_xpath).text
        return kpi_name

    def get_tco(self):
        kpi_name = self.driver.find_element(By.XPATH, self.kpi_tco_xpath).text
        return kpi_name

    def get_efficiency(self):
        kpi_name = self.driver.find_element(By.XPATH, self.kpi_efficiency_xpath).text
        return kpi_name

    def get_latency(self):
        kpi_name = self.driver.find_element(By.XPATH, self.kpi_latency_xpath).text
        return kpi_name

    def get_images_per_second(self):
        kpi_name = self.driver.find_element(By.XPATH, self.kpi_imagesPerSecond_xpath).text
        return kpi_name

    def get_images_per_second_per_user(self):
        kpi_name = self.driver.find_element(By.XPATH, self.kpi_imagesPerSecondPerUser_xpath).text
        return kpi_name

    def confirm_simulation_diffusion(self):
        return self.driver.find_element(By.XPATH, self.kpi_latency_xpath).is_displayed()

    # Clear button methods
    def clickOnClear(self):
        clear_button = self.driver.find_element(By.XPATH, self.button_clear_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", clear_button)
        self.driver.execute_script("arguments[0].click();", clear_button)

    def confirmClearInputs(self):
        text_model = self.driver.find_element(By.XPATH, self.dropdown_options_chooseModel).text
        text_prompt = self.driver.find_element(By.XPATH, self.dropdown_options_choosePrompt).text
        text_batch_size = self.driver.find_element(By.XPATH, self.dropdown_options_chooseBatchSize).text
        text_tensor = self.driver.find_element(By.XPATH, self.dropdown_options_chooseTensorParallelism).text
        # print(text_tensor, text_model, text_batch_size, text_prompt)
        if text_model == 'Choose Model' and text_prompt == 'Choose Prompt' and text_batch_size == 'Batch Size' and text_tensor == 'Tensor Parallelism':
            return True

    # toast messages when running simulation without providing mandatory fields
    def run_withoutfields_toastmessage(self):
        run_without_fields = self.driver.find_element(By.XPATH, self.toast_selectmodel_xpath).get_attribute("innerHTML")
        return run_without_fields

    # toggle to Slider Demo
    def toggle_slider_demo(self):
        self.driver.find_element(By.XPATH, self.button_sliderDemo_xpath).click()

    def slide_input_token(self):
        act = ActionChains(self.driver)
        slider = self.driver.find_element(By.XPATH, self.slider_inputTokens_xpath)
        act.click_and_hold(slider).move_by_offset(400, 0).release().perform()

    def slide_output_token(self):
        act = ActionChains(self.driver)
        slider = self.driver.find_element(By.XPATH, self.slider_outputTokens_xpath)
        act.click_and_hold(slider).move_by_offset(400, 0).release().perform()

    def slide_batch_size(self):
        act = ActionChains(self.driver)
        slider = self.driver.find_element(By.XPATH, self.slider_batchSize_xpath)
        act.click_and_hold(slider).move_by_offset(400, 0).release().perform()

    def slide_tensor_paralleilism(self):
        act = ActionChains(self.driver)
        slider = self.driver.find_element(By.XPATH, self.slider_tensorParallelism_xpath)
        act.click_and_hold(slider).move_by_offset(400, 0).release().perform()

    # Get text of the recogni and competitor's output box
    def get_recogni_output_text(self):
        recogni_output = self.driver.find_element(By.XPATH, self.text_outputboxrecogni_xpath).text
        return recogni_output

    def get_competitor_output_text(self):
        competitor_output = self.driver.find_element(By.XPATH, self.text_outputboxcompetitor_xpath).text
        return competitor_output

    def confirm_match_output_texts(self):
        recogni_output = self.driver.find_element(By.XPATH, self.text_outputboxrecogni_xpath).text
        competitor_output = self.driver.find_element(By.XPATH, self.text_outputboxcompetitor_xpath).text
        if recogni_output == competitor_output:
            return True

    def click_copy_recogni(self):
        self.driver.find_element(By.XPATH, self.icon_copyrecogni_xpath).click()
        recogni_text = pyperclip.paste()
        return recogni_text

    def click_copy_competitor(self):
        self.driver.find_element(By.XPATH, self.icon_copycompetitor_xpath).click()
        competitor_text = pyperclip.paste()
        return competitor_text
