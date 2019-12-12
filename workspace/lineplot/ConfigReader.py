import yaml 


class ConfigReader():
    def __init__(self, config_name):
        self.config_name = config_name

    def read_config(self):
        result = dict()
        with open(self.config_name) as config:
            result = yaml.safe_load(config)
        return result
