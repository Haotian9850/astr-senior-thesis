import matplotlib.pyplot as plt
from astropy.wcs import WCS
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
import matplotlib.pyplot as plt
import sys
import numpy as np

DATA_BASE_DIR = "/media/haotian/documents-local/ASTR4998/data/products"
SAVE_IMG_DIR = ""
C = 2.99792458E+8


def calculate_slice_channel(line_freq, rest_freq, num_channel, min_speed, max_speed):
    speed_offset = (line_freq - rest_freq) * (C / rest_freq)
    print(speed_offset)
    return num_channel * ((speed_offset - min_speed) / (max_speed - min_speed))


def calculate_slice_channel_from_admit(start, end):
    return (start + end) // 2


def plot_slice(slice, dim, fits_name, cutout):
    cube = get_pkg_data_filename(fits_name)
    hdu = fits.open(cube)[0]
    print(WCS(hdu.header))
    result = []
    for i in range(cutout, dim - cutout):
        result.append([hdu.data[0][int(slice)][i][j] for j in range(cutout, dim - cutout)])
    print(len(result))
    print(len(result[0]))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(np.asarray(result), interpolation="nearest")
    fig.colorbar(cax)
    plt.xlabel("ICRS Right Ascension")
    plt.ylabel("ICRS Declination")
    plt.gca().invert_yaxis()
    plt.gca().xaxis.tick_bottom()
    plt.contour(result, levels=np.logspace(-2, 4, num=8, endpoint=False), colors='white', alpha=0.5)
    plt.savefig("spw3_{}".format(slice), dpi=300)
    plt.show()


def plot(startchan, endchan, fits_name, dim, cutout):
    plot_slice(calculate_slice_channel_from_admit(startchan, endchan), dim, fits_name, cutout)



if __name__ == "__main__":
    plot(
        943,    #startchan
        944,    #endchan
        "SerpS_TC_spw3.pbcor_cutout_180_180_100_line.fits",    #fits file name
        100,    #fits file dimension
        0
    )


