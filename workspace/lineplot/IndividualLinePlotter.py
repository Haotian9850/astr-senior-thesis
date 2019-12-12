from ConfigReader import ConfigReader



class IndividualLinePlotter():
    def __init__(self, data_dir, package_name, cube_name, config_name, max_y, vpos=0.4, vlsr=8.0, lines_file_name="lltable.9.json"):
        self.data_dir = data_dir
        self.package_name = package_name
        self.cube_name = cube_name
        self.config_name = config_name
        self.max_y = max_y
        self.vpos = vpos 
        self.vlsr = vlsr
        self.lines_file_name = lines_file_name
        self.configReader = ConfigReader(self.config_name)
        

    def generate_config()


    def read_config(self):
        result = dict()
        with open(self.config_name) as config:
            result = yaml.safe_load(config)
        return result
