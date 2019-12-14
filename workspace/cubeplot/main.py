import numpy as np

from ContourPlotter import ContourPlotter

FITS_NAME = "SerpS_TC_spw5.pbcor_cutout_180_180_100_line.fits"
CUTOUT = 0
CHANNELS_SPW0 = [167, 332, 474, 477, 478, 479, 480, 481, 482, 483, 485, 487]
CHANNELS_SPW1 = [177, 594, 602, 605, 611, 633]
CHANNELS_SPW2 = [269, 636, 639, 642]
CHANNELS_SPW3 = [920, 926, 933, 936, 942, 944]
CHANNELS_SPW4 = [438, 448, 465, 482, 510, 516]
CHANNELS_SPW5 = [474, 476, 477, 478, 479, 480, 481, 482, 483]
CONTOUR_LEVELS = np.linspace(2, 20, 10)
BACKGROUND_SIZE = 20
PREFIX = "spw5"
SAVEFIG = True



if __name__ == "__main__":
    plotter = ContourPlotter(
        FITS_NAME,
        CUTOUT,
        CHANNELS_SPW5,
        CONTOUR_LEVELS,
        BACKGROUND_SIZE,
        PREFIX,
        SAVEFIG
    )
    plotter.plot_slices()

