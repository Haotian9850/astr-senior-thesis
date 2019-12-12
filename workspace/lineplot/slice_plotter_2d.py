import matplotlib.pyplot as plt
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import text
import sys

from config_reader import read_config


matplotlib.rc("font", size=12)

DATA_BASE_DIR = "/media/haotian/documents-local/ASTR4998/data/raw"
TAB_FILE_NAME = "testCubeStats.tab"

C = 2.99792458E+8


def read_cube_spectrum_file(data_dir, package_name, file_name):
    x = []
    y = []
    for pair in [line.rstrip() for line in open("{}/{}/{}".format(data_dir, package_name, file_name),'r').read().split('\n')[1:-1]]:
        x.append(float(pair.split()[0].strip()))
        y.append(10 ** float(pair.split()[1].strip()))
    return x, y



def plot(data_dir, package_name, file_name, config_name, prefix):
    print("-------- reading config YAML file... --------")
    config = read_config(config_name)
    latex_include = []
    for line in config["promising_lines"].keys():
        print("-------- plotting line {}... --------".format(line))
        line_info = config["promising_lines"][line]
        plot_individual_line(
            line_info[0],
            line_info[1],
            config["max_y"],
            line_info[2],
            line,
            line_info[3],
            data_dir, 
            package_name,
            file_name,
            line_info[4],
            prefix,
            line_info[5],
            latex_include
        )
    print("-------- all lines are plotted --------")
    for entry in latex_include:
        print(entry)




def plot_individual_line(start_chan, end_chan, y_range, offset_size, name, vpos, data_dir, package_name, file_name, formula, prefix, frequency, latex_include):
    x, y = read_cube_spectrum_file(data_dir, package_name, file_name)
    offset = int((((end_chan - start_chan) // 2) * offset_size))
    x , y = x[max(0, start_chan - offset) : min(len(x), end_chan + offset)], y[max(0, start_chan - offset) : min(len(x), end_chan + offset)]
    plt.plot(x, y)
    plt.axvline(frequency, linewidth=1.0, color="r", linestyle=":")
    plt.text(frequency, y_range * vpos, formula, rotation=90)
    plt.ylim(0, y_range)
    plt.ticklabel_format(useOffset=False)
    plt.xlabel("Frequency (GHz)")
    plt.ylabel("Peak / Noise")
    plt.savefig("{}_{}.png".format(prefix, formula), dpi=300)
    #plt.show()
    latex_include.append("\\includegraphics[width=0.33\\textwidth]{}".format("{" + prefix + "_" + formula + "}"))
    


def find_peak_x(x, y):
    return x[y.index(max(y))]



if __name__ == "__main__":
    plot(
        DATA_BASE_DIR,
        "SerpS_TC_spw0.pbcor_cutout_180_180_100_line.fits.admit_BDP",
        TAB_FILE_NAME,
        "config_spw0.yaml",
        "spw2"
    )


