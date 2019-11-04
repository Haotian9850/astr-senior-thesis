import matplotlib.pyplot as plt
from astropy.wcs import WCS
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
import matplotlib.pyplot as plt
import sys

DATA_BASE_DIR = "/mnt/documents-local/ASTR4998/data/data/"



def plot_slice(slice, dim, fits_name):
    cube = get_pkg_data_filename(fits_name)
    hdu = fits.open(cube)[0]
    print(WCS(hdu.header))
    image_data = hdu.data
    result = []
    for i in range(0, 360):
        result.append([image_data[0][slice][i][j] for j in range(0, dim)])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(result, interpolation="nearest")
    fig.colorbar(cax)
    plt.xlabel("ICRS Right Ascension")
    plt.ylabel("ICRS Declination")

    plt.show()





if __name__ == "__main__":
    plot_slice(
        int(sys.argv[1]),    #slice number
        int(sys.argv[2]),   #fits dimension (side length) 
        sys.argv[3]    #fits name
    )

