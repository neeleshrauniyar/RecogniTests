import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + "//configurations//config.ini")


class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseUrl')
        return url


class ReadModels:
    @staticmethod
    def get_llm_model():
        model = config.get('model_names', 'llm_model')
        return model

    @staticmethod
    def get_diffusion_model():
        model = config.get('model_names', 'diffusion_model')
        return model


class ReadLLMParameters:
    @staticmethod
    def get_model():
        model = config.get('llm_simulation_parameters', 'model')
        return model

    @staticmethod
    def get_prompt():
        prompt = config.get('llm_simulation_parameters', 'prompt')
        return prompt

    @staticmethod
    def get_batch_size():
        batch_size = config.get('llm_simulation_parameters', 'batch_size')
        return batch_size

    @staticmethod
    def get_tensor_parallelism():
        tensor_parallelism = config.get('llm_simulation_parameters', 'tensor_parallelism')
        return tensor_parallelism


class ReadDiffusionParameters:
    @staticmethod
    def get_model():
        model = config.get('diffusion_simulation_parameters', 'model')
        return model

    @staticmethod
    def get_prompt():
        prompt = config.get('diffusion_simulation_parameters', 'prompt')
        return prompt

    @staticmethod
    def get_batch_size():
        batch_size = config.get('diffusion_simulation_parameters', 'batch_size')
        return batch_size

    @staticmethod
    def get_tensor_parallelism():
        tensor_parallelism = config.get('diffusion_simulation_parameters', 'tensor_parallelism')
        return tensor_parallelism


class ReadSliderDemoParameters:
    @staticmethod
    def get_model():
        model = config.get('slider_demo_parameters', 'model')
        return model


class ReadKPIs:
    @staticmethod
    def read_kpi_ttft():
        ttft = config.get('kpi', 'ttft')
        return ttft

    @staticmethod
    def read_kpi_tpot():
        tpot = config.get('kpi', 'tpot')
        return tpot

    @staticmethod
    def read_kpi_tokens_per_sec():
        tokens_per_sec = config.get('kpi', 'tokens_per_sec')
        return tokens_per_sec

    @staticmethod
    def read_kpi_total_power_consumption():
        tpo = config.get('kpi', 'total_power_consumption')
        return tpo

    @staticmethod
    def read_kpi_tco():
        tco = config.get('kpi', 'tco')
        return tco

    @staticmethod
    def read_kpi_efficiency():
        efficiency = config.get('kpi', 'efficiency')
        return efficiency

    @staticmethod
    def read_kpi_latency():
        latency = config.get('kpi', 'latency')
        return latency

    @staticmethod
    def read_kpi_images_per_second():
        images_per_second = config.get('kpi', 'images_per_second')
        return images_per_second

    @staticmethod
    def read_kpi_images_per_second_per_user():
        images_per_second_per_user = config.get('kpi', 'images_per_second_per_user')
        return images_per_second_per_user
