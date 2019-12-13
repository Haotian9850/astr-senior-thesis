import sys
import numpy as np
import math
import logging

import matplotlib.pyplot as plt
from astropy.wcs import WCS
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
import matplotlib.pyplot as plt
from matplotlib import rc

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-6s %(levelname)-4s %(message)s',
    datefmt='%m-%d %H:%M'
)

rc("font", size=12)
rc("text", usetex=True)
rc("font",**{"family":"sans-serif","sans-serif":["Helvetica"]})


class ContourPlotter():
    def __init__(self, fits_name, cutout, channels, contour_levels, background_center, background_size, prefix, savefig):
        self.fits_name = fits_name
        self.cutout = cutout
        self.channels = channels
        self.contour_levels = contour_levels
        self.background_center = background_center
        self.background_size = background_size
        self.prefix = prefix
        self.savefig = savefig


    def plot_slices(self):
        for channel in self.channels:
            self.plot_individual_slice(channel)


    def plot_individual_slice(self, channel):
        cube = get_pkg_data_filename(
            data_name=self.fits_name
        )
        hdu = fits.open(cube)[0]
        plot_area = []
        background = []
        for i in range(self.cutout, len(hdu.data[0][0]) - self.cutout):
            plot_area.append([hdu.data[0][channel][i][j] for j in range(self.cutout, len(hdu.data[0][0]) - self.cutout)])
        for i in range(self.background_center - self.background_size, len(hdu.data[0][0])):
            background.append(
                [hdu.data[0][channel][i][j] for j in range(self.background_center - self.background_size, len(hdu.data[0][0]))]
            )
        logging.info("plotting .fits file of cutout size {} x {}...".format(len(plot_area), len(plot_area)))
        logging.info("calculating background rms from size {} x {} of center {}...".format(self.background_size, self.background_size, self.background_center))
        background_rms = self.calculate_background_rms(background)
        logging.info("slice has a background noise of {}...".format(background_rms))
        fig = plt.figure()
        ax = fig.add_subplot(111)
        cax = ax.matshow(np.asarray(plot_area), interpolation="nearest")
        fig.colorbar(cax)
        plt.xlabel("ICRS Right Ascension")
        plt.ylabel("ICRS Declination")
        plt.title("Channel ${}/{}$ of {}".format(
            channel,
            len(hdu.data[0]),
            self.prefix
        ))
        plt.gca().invert_yaxis()
        plt.gca().xaxis.tick_bottom()
        plt.contour(
            plot_area,
            levels=self.make_contour_levels(background_rms),
            colors="white"
        )
        if self.savefig:
            logging.info("saving plot...")
            plt.savefig("{}_{}".format(self.prefix, channel), dpi=300, bbox_inches="tight")
        plt.show()


    def calculate_background_rms(self, background):
        square_sum = 0
        for row in background:
            for pixel in row:
                square_sum += math.pow(pixel, 2)
        return math.sqrt(square_sum / math.pow(len(background), 2))


    def make_contour_levels(self, rms):
        logging.info("calculating contour levels from levels: {}".format(str(self.contour_levels)))
        return list(map(lambda x: x * rms, self.contour_levels))
        
        
        
