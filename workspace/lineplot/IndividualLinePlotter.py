from ConfigReader import ConfigReader
from ConfigGenerator import ConfigGenerator



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
        self.configGenerator = ConfigGenerator(
            self.data_dir,
            self.package_name,
            self.lines_file_name,
            self.max_y,
            self.vpos,
            self.vlsr,
            self.config_name
        )
        self.configReader = ConfigReader(self.config_name)
        

    def generate_config(self):
        self.configGenerator.write_to_config_file()


    def read_config(self):
        return self.configReader.read_config()
