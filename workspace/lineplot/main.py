from IndividualLinePlotter import IndividualLinePlotter


DATA_DIR = "/media/haotian/documents-local/ASTR4998/data/raw"
PACKAGE_NAME = "SerpS_TC_spw3.pbcor_cutout_180_180_100_line.fits.admit_BDP"
CONFIG_NAME = "spw3"

REST_FREQUENCY_SPW0 = 3.37061E+11
REST_FREQUENCY_SPW1 = 3.366619E+11
REST_FREQUENCY_SPW2 = 3.35913E+11
REST_FREQUENCY_SPW3 = 3.455527E+11


MAX_Y_SPW0 = 60
MAX_Y_SPW1 = 30
MAX_Y_SPW2 = 115
MAX_Y_SPW3 = 220

SAVEFIG = True 
VPOS = 0.6
VLSR = 8.0



if __name__ == "__main__":
    plotter = IndividualLinePlotter(
        DATA_DIR,
        PACKAGE_NAME,
        CONFIG_NAME,
        MAX_Y_SPW3,
        REST_FREQUENCY_SPW3,
        SAVEFIG,
        VPOS,
        VLSR
    )
    plotter.plot_lines()
