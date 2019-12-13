import numpy as np

from ContourPlotter import ContourPlotter

FITS_NAME = "SerpS_TC_spw0.pbcor_cutout_180_180_100_line.fits"
CUTOUT = 0
CHANNELS = [167, 332, 474, 477, 478, 479, 480, 481, 482, 483, 485, 487]
CONTOUR_LEVELS = np.linspace(2, 20, 10)
BACKGROUND_SIZE = 20
PREFIX = "spw0"
SAVEFIG = True



if __name__ == "__main__":
    plotter = ContourPlotter(
        FITS_NAME,
        CUTOUT,
        CHANNELS,
        CONTOUR_LEVELS,
        BACKGROUND_SIZE,
        PREFIX,
        SAVEFIG
    )
    plotter.plot_slices()

