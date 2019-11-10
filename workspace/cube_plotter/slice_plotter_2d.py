import matplotlib.pyplot as plt
from astropy.wcs import WCS
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
import matplotlib.pyplot as plt
from matplotlib.pyplot import text
import sys

DATA_BASE_DIR = "/mnt/documents-local/ASTR4998/data/raw/"
C = 2.99792458E+8


def read_cube_spectrum_file(data_dir, package_name, file_name):
    x = []
    y = []
    for pair in [line.rstrip() for line in open("{}/{}/{}".format(data_dir, package_name, file_name),'r').read().split('\n')[1:-1]]:
        x.append(float(pair.split()[0].strip()))
        y.append(10 ** float(pair.split()[1].strip()))
    return x, y


def plot(data_dir, package_name, file_name):
    x, y = read_cube_spectrum_file(data_dir, package_name, file_name)
    print(x)
    plt.plot(x, y)
    plt.show()


def plot_individual_line(start_chan, end_chan, freq, y_range, offset_size, name, data_dir, package_name, file_name):
    x, y = read_cube_spectrum_file(data_dir, package_name, file_name)
    offset = int((((end_chan - start_chan) // 2) * offset_size))
    x , y = x[max(0, start_chan - offset) : min(len(x), end_chan + offset)], y[max(0, start_chan - offset) : min(len(x), end_chan + offset)]
    plt.plot(x, y)
    fake_freq = (x[0]+x[-1])/2.0    #TODO: make sure where to put vline
    plt.axvline(x=fake_freq, linewidth=1.0, color="r", linestyle=":")
    plt.ylim(0, y_range)
    plt.ticklabel_format(useOffset=False)
    plt.xlabel("Frequency (GHz)")
    plt.ylabel("Peak / Noise")
    plt.show()
    



if __name__ == "__main__":
    plot_individual_line(839, 875, 336.959, 25, 0.4, "sample annotation", DATA_BASE_DIR, "SerpS_TC_spw0.pbcor_cutout_180_180_100_line.fits.admit", "testCubeStats.tab")


