import sys
import logging

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import text
from matplotlib import rc

from ConfigReader import ConfigReader
from ConfigGenerator import ConfigGenerator
from SpectrumReader import SpectrumReader
from MoleculePrettyPlotPrinter import MoleculePrettyPrinter

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-6s %(levelname)-4s %(message)s',
    datefmt='%m-%d %H:%M'
)

rc("font", size=14)
rc("text", usetex=True)
rc("font",**{"family":"sans-serif","sans-serif":["Helvetica"]})

C = 2.99792458E+8


class IndividualLinePlotter():
    def __init__(self, data_dir, package_name, config_name, max_y, rest_frequency, savefig=True, vpos=0.4, vlsr=8.0, lines_file_name="lltable.9.json", spectrum_file_name="testCubeStats.tab"):
        self.data_dir = data_dir
        self.package_name = package_name
        self.config_name = config_name
        self.max_y = max_y
        self.rest_frequency = rest_frequency
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
        self.moleculePrettyPlotPrinter = MoleculePrettyPrinter()
        

    def plot_lines(self):
        tex_include = []
        logging.info("generating config YAML file...")
        #self.configGenerator.write_to_config_file()
        logging.info("reading config YAML file...")
        config = self.configReader.read_config()
        for line in config["promising_lines"].keys():
            logging.info("plotting line {}...".format(line))
            line_info = config["promising_lines"][line]
            self.plot_individual_line(
                line_info[0],
                line_info[1],
                config["max_y"],
                line,
                line_info[3],
                self.data_dir, 
                self.package_name,
                line_info[4],
                self.config_name,
                line_info[5],
                tex_include
            )
        logging.info("all lines are plotted")
        for stmt in tex_include:
            print(stmt)


    def plot_individual_line(self, start_chan, end_chan, max_y, name, vpos, data_dir, package_name, formula, prefix, frequency, tex_include):
        x, y = self.spectrumReader.read_cube_spectrum_file()
        a , b = x[start_chan : end_chan], y[start_chan: end_chan]
        plt.plot(a, b)
        plt.axvline(
            frequency - self.calculate_offset(frequency, x[0], x[-1]),
            linewidth=1.0,
            color="r",
            linestyle=":"
        )
        plt.text(
            frequency - self.calculate_offset(frequency, x[0], x[-1]) * 0.98, #compensate for offset brought by Latex
            max_y * vpos,  
            self.moleculePrettyPlotPrinter.pretty_print_molecule(formula),
            rotation=90
        )
        plt.ylim(0, max_y)
        plt.ticklabel_format(useOffset=False)
        plt.xlabel("Frequency (GHz)")
        plt.ylabel("Peak / Noise")
        plt.title("{} ({}), ${}$ GHz".format(
            name,
            self.moleculePrettyPlotPrinter.pretty_print_molecule(formula),
            frequency,
        ))
        if self.savefig:
            plt.savefig("{}_{}.png".format(prefix, formula), dpi=300, bbox_inches="tight")
            tex_include.append(
                "\\includegraphics[width=0.245\\textwidth]{{{}_{}}}".format(
                    self.config_name,
                    formula
                )
            )
        plt.show()


    def calculate_offset(self, frequency, start, end):
        frequency_range = start - end
        rest_wavelength = C / (self.rest_frequency)
        velocity_range_ms = frequency_range * (10 ** 9) * rest_wavelength * (10 ** -3)
        offset = frequency_range * (self.vlsr / velocity_range_ms)
        return offset

        

    def generate_config(self):
        self.configGenerator.write_to_config_file()


    def read_config(self):
        return self.configReader.read_config()
