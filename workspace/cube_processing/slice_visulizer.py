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

DATA_BASE_DIR = "/mnt/documents-local/ASTR4998/data/data/"


if __name__ == "__main__":
    fits_data = fits.open(DATA_BASE_DIR + "SerpS_TC_spw0.pbcor.fits")
    cube = SpectralCube.read(fits_data)
    fits_data.close()
    #print(cube.spectral_axis)
    cube2 = cube.with_spectral_unit(u.km / u.s, velocity_convention='radio', rest_value=337.061 * u.GHz)  
    #print(cube2.spectral_axis)
    cube_slab = cube2.spectral_slab(8. *u.km / u.s, 9. *u.km / u.s)
    print(cube_slab)
    
    moment_0 = cube_slab.with_spectral_unit(u.km/u.s).moment(order=0)
    print(moment_0.wcs)

    hi_column_density = moment_0 * 1.82 * 10**18 / (u.cm * u.cm) * u.s / u.K / u.km

    fig = plt.figure(figsize=(18, 12))
    ax = fig.add_subplot(111, projection=moment_0.wcs)

    # Display the moment map image
    im = ax.imshow(moment_0.hdu.data, cmap='RdBu_r', vmin=0, vmax=200)
    ax.invert_yaxis()  # Flips the Y axis

    # Add axes labels
    ax.set_xlabel("x", fontsize=16)
    ax.set_ylabel("y", fontsize=16)

    # Add a colorbar
    cbar = plt.colorbar(im, pad=.07)
    cbar.set_label('a', size=16)

    # Overlay set of RA/Dec Axes
    overlay = ax.get_coords_overlay('fk5')
    overlay.grid(color='white', ls='dotted', lw=2)
    overlay[0].set_axislabel('Right Ascension (J2000)', fontsize=16)
    overlay[1].set_axislabel('Declination (J2000)', fontsize=16)

    # Overplot column density contours
    levels = (1e20, 5e20, 1e21, 3e21, 5e21, 7e21, 1e22)  # Define contour levels to use
    ax.contour(hi_column_density.hdu.data, cmap='Greys_r', alpha=0.5, levels=levels)