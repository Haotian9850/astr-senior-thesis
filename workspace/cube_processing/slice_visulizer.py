import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

import astropy.units as u
from astropy.utils.data import download_file
from astropy.io import fits

from astropy.utils import data
data.conf.remote_timeout = 60

from spectral_cube import SpectralCube

from astroquery.esasky import ESASky
from astroquery.utils import TableList
from astropy.wcs import WCS

DATA_BASE_DIR = "/mnt/documents-local/ASTR4998/astr-senior-thesis/workspace/statcont_admit_pipeline/data/"


if __name__ == "__main__":
    fits_data = fits.open(DATA_BASE_DIR + "SerpS_TC_spw0.pbcor.fits")
    cube = SpectralCube.read(fits_data)
    fits_data.close()
    print(cube)

