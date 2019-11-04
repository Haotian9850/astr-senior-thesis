import matplotlib.pyplot as plt
from astropy.wcs import WCS
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
import matplotlib.pyplot as plt
import sys

DATA_BASE_DIR = "/mnt/documents-local/ASTR4998/data/data/"
C = 2.99792458E+8


def calculate_slice_channel(line_freq, rest_freq, num_channel, min_speed, max_speed):
    speed_offset = (line_freq - rest_freq) * (C / rest_freq)
    print(speed_offset)
    return num_channel * ((speed_offset - min_speed) / (max_speed - min_speed))


def calculate_slice_channel_from_admit(start, end):
    return (start + end) // 2


def plot_slice(slice, dim, fits_name):
    cube = get_pkg_data_filename(fits_name)
    hdu = fits.open(cube)[0]
    print(WCS(hdu.header))
    result = []
    for i in range(0, dim):
        result.append([hdu.data[0][slice][i][j] for j in range(0, dim)])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(result, interpolation="nearest")
    fig.colorbar(cax)
    plt.xlabel("ICRS Right Ascension")
    plt.ylabel("ICRS Declination")

    plt.show()


def plot(startchan, endchan, fits_name, dim):
    plot_slice(calculate_slice_channel_from_admit(startchan, endchan), dim, fits_name)



if __name__ == "__main__":
    plot(
        int(sys.argv[1]),    #startchan
        int(sys.argv[2]),    #endchan
        sys.argv[3],    #fits file name
        int(sys.argv[4])     #fits file dimension
    )
    


