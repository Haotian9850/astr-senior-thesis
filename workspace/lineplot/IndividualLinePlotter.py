import matplotlib.pyplot as plt
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import text

from ConfigReader import ConfigReader
from ConfigGenerator import ConfigGenerator
from SpectrumReader import SpectrumReader


class IndividualLinePlotter():
    def __init__(self, data_dir, package_name, cube_name, config_name, max_y, savefig=True, vpos=0.4, vlsr=8.0, lines_file_name="lltable.9.json", spectrum_file_name="testCubeStats.tab"):
        self.data_dir = data_dir
        self.package_name = package_name
        self.cube_name = cube_name
        self.config_name = config_name
        self.max_y = max_y
        self.savefig = savefig
        self.vpos = vpos 
        self.vlsr = vlsr
        self.lines_file_name = lines_file_name
        self.spectrum_file_name = spectrum_file_name
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
        self.spectrumReader = SpectrumReader(self.data_dir, self.package_name, self.spectrum_file_name)
        

    def plot_lines(self):
        print("-------- generating config YAML file... --------")
        self.configGenerator.write_to_config_file()
        print("-------- reading config YAML file... --------")
        config = self.configReader.read_config()
        for line in config["promising_lines"].keys():
            print("-------- plotting line {}... --------".format(line))
            line_info = config["promising_lines"][line]
            self.plot_individual_line(
                line_info[0],
                line_info[1],
                config["max_y"],
                line_info[2],
                line,
                line_info[3],
                self.data_dir, 
                self.package_name,
                line_info[4],
                self.config_name,
                line_info[5]
            )
        print("-------- all lines are plotted --------")


    def plot_individual_line(self, start_chan, end_chan, max_y, offset_size, name, vpos, data_dir, package_name, formula, prefix, frequency):
        x, y = self.spectrumReader.read_cube_spectrum_file()
        offset = int((((end_chan - start_chan) // 2) * offset_size))
        x , y = x[max(0, start_chan - offset) : min(len(x), end_chan + offset)], y[max(0, start_chan - offset) : min(len(x), end_chan + offset)]
        plt.plot(x, y)
        plt.axvline(frequency, linewidth=1.0, color="r", linestyle=":")
        plt.text(frequency, max_y * vpos, formula, rotation=90)
        plt.ylim(0, max_y)
        plt.ticklabel_format(useOffset=False)
        plt.xlabel("Frequency (GHz)")
        plt.ylabel("Peak / Noise")
        plt.savefig("{}_{}.png".format(prefix, formula), dpi=300)
        plt.show()


    def generate_config(self):
        self.configGenerator.write_to_config_file()


    def read_config(self):
        return self.configReader.read_config()
