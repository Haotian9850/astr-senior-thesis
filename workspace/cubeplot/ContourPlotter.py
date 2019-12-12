import sys
import numpy as np

import matplotlib.pyplot as plt
from astropy.wcs import WCS
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
import matplotlib.pyplot as plt
from matplotlib import rc

rc("font", size=12)
rc("text", usetex=True)
rc("font",**{"family":"sans-serif","sans-serif":["Helvetica"]})


class ContourPlotter():
    def __init__(self, data_dir, fits_name, cutout, channels, background_center, background_size, prefix, savefig):
        self.data_dir = data_dir
        self.fits_name = fits_name
        self.cutout = cutout
        self.channels = channels
        self.background_center = background_center
        self.background_size = background_size
        self.prefix = prefix
        self.savefig = savefig


    def plot_slices(self):
        for channel in self.channels:
            self.plot_individual_slice(channel)


    def plot_individual_slice(self, channel):
        cube = get_pkg_data_filename(self.fits_name)
        hdu = fits.open(cube)[0]
        print(WCS(hdu.header))
        print(len(hdu.data[0][0]))
        plot_area = []
        background = []
        for i in range(self.cutout, len(hdu.data[0][0]) - self.cutout):
            plot_area.append([hdu.data[0][channel][i][j] for j in range(self.cutout, len(hdu.data[0][0]) - self.cutout)])
        for i in range(self.background_center - self.background_size, len(hdu.data[0][0])):
            background.append(
                [hdu.data[0][channel][i][j] for j in range(self.background_center - self.background_size, len(hdu.data[0][0]))]
            )
        print(plot_area)
        print(len(plot_area))
        print(len(plot_area[0]))
        print(background)
        print(len(background))
        print(len(background[0]))
        fig = plt.figure()
        ax = fig.add_subplot(111)
        cax = ax.matshow(np.asarray(plot_area), interpolation="nearest")
        fig.colorbar(cax)
        plt.xlabel("ICRS Right Ascension")
        plt.ylabel("ICRS Declination")
        plt.gca().invert_yaxis()
        plt.gca().xaxis.tick_bottom()
        plt.contour(plot_area, levels=np.logspace(-2, 4, num=8, endpoint=False), colors='white', alpha=0.5)
        if self.savefig:
            plt.savefig("spw3_{}".format(channel), dpi=300)
        plt.show()


    def calculate_background_rms(self, background):
        pass

        
        
