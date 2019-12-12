from IndividualLinePlotter import IndividualLinePlotter


DATA_DIR = "/media/haotian/documents-local/ASTR4998/data/raw"
PACKAGE_NAME = "SerpS_TC_spw0.pbcor_cutout_180_180_100_line.fits.admit_BDP"
CONFIG_NAME = "spw0"
REST_FREQUENCY = 3.37061E+11
MAX_Y = 60
SAVEFIG = False 
VPOS = 0.4
VLSR = 8.0



if __name__ == "__main__":
    plotter = IndividualLinePlotter(
        DATA_DIR,
        PACKAGE_NAME,
        CONFIG_NAME,
        MAX_Y,
        REST_FREQUENCY,
        SAVEFIG,
        VPOS,
        VLSR
    )
    plotter.plot_lines()
