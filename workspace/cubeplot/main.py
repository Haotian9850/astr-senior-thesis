import numpy as np

from ContourPlotter import ContourPlotter

FITS_NAME = "SerpS_TC_spw3.pbcor_cutout_180_180_100_line.fits"
CUTOUT = 30
CHANNELS = [932]
CONTOUR_LEVELS = np.linspace(2, 60, 10)
BACKGROUND_CENTER = 90
BACKGROUND_SIZE = 10
PREFIX = "spw3"
SAVEFIG = True



if __name__ == "__main__":
    plotter = ContourPlotter(
        FITS_NAME,
        CUTOUT,
        CHANNELS,
        CONTOUR_LEVELS,
        BACKGROUND_CENTER,
        BACKGROUND_SIZE,
        PREFIX,
        SAVEFIG
    )
    plotter.plot_slices()

