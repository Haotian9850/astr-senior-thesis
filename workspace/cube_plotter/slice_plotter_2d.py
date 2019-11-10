import matplotlib.pyplot as plt
from astropy.wcs import WCS
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
import matplotlib.pyplot as plt
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


def plot(startchan, endchan, data_dir, package_name, file_name):
    x, y = read_cube_spectrum_file(data_dir, package_name, file_name)
    print(x)
    plt.plot(x, y)
    plt.show()



if __name__ == "__main__":
    plot(-1, -1, DATA_BASE_DIR, "SerpS_TC_spw0.pbcor_cutout_180_180_100_line.fits.admit", "testCubeStats.tab")


